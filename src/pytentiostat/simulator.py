from __future__ import annotations

import math
import random
import time
from dataclasses import dataclass


def _clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


@dataclass
class SimulationParams:
    """Parameters controlling the simulated potentiostat signal shape."""

    noise_std: float = 0.0008  # noise in duty-cycle units (0-1)
    r_solution_ohm: float = 220.0  # effective solution resistance
    e0_v: float = 0.2  # "redox" midpoint, used for a smooth I-V curve
    i_lim_ma: float = 2.0  # limiting current magnitude
    ca_tau_s: float = 1.5  # decay constant for CA-like behavior


class SimulatedBoard:
    """Minimal board-like object compatible with routines.closing_routine()."""

    def exit(self) -> None:  # pragma: no cover
        return


class _SimulatedD9:
    def __init__(self, sim: "SimulatedPotentiostat"):
        self._sim = sim

    def write(self, duty_cycle: float) -> None:
        self._sim.set_duty_cycle(duty_cycle)


class _SimulatedAnalog:
    def __init__(self, sim: "SimulatedPotentiostat", channel: str):
        self._sim = sim
        self._channel = channel

    def read(self) -> float:
        if self._channel == "a0":
            return self._sim.read_a0()
        if self._channel == "a2":
            return self._sim.read_a2()
        raise ValueError(f"Unknown channel {self._channel!r}")


class SimulatedPotentiostat:
    """A lightweight simulator that mimics pyFirmata pin IO.

    It provides three pin-like objects:
    - d9.write(duty) to set the PWM duty cycle (0..1)
    - a0.read() analog "voltage" feedback (0..1)
    - a2.read() analog "current" sense (0..1)

    The transformation mirrors operator.read_write():
      real_voltage = (a0 - 0.5) * -cf
      real_current = (a2 - 0.5) * -cf / sr
    """

    def __init__(
        self,
        *,
        conversion_factor: float = 5.0,
        shunt_resistor: float = 1000.0,
        params: SimulationParams | None = None,
        seed: int | None = 0,
    ):
        self._cf = float(conversion_factor)
        self._sr = float(shunt_resistor)
        self._p = params or SimulationParams()
        self._rng = random.Random(seed)

        # The ADC pin (a2) returns values in [0, 1].  The operator recovers
        # current as: i = (a2 - 0.5) * -cf / sr.  So the maximum current
        # the ADC can represent is 0.5 * cf / sr (mA).  Scale the limiting
        # current to ~60% of that so the signal is clearly visible but
        # never clips.
        self._p.i_lim_ma = 0.6 * (0.5 * self._cf / self._sr)

        self._duty = 0.5
        self._prev_duty = 0.5
        self._t0 = None  # type: float | None
        self._last_write_t = None  # type: float | None
        self._ca_start_t = None  # type: float | None

        self.d9 = _SimulatedD9(self)
        self.a0 = _SimulatedAnalog(self, "a0")
        self.a2 = _SimulatedAnalog(self, "a2")
        self.board = SimulatedBoard()

    def set_duty_cycle(self, duty: float) -> None:
        now = time.time()
        if self._t0 is None:
            self._t0 = now
        self._last_write_t = now
        new_duty = _clamp(float(duty), 0.0, 1.0)
        if abs(new_duty - self._duty) > 1e-6:
            # Voltage is changing — not a constant-potential experiment
            self._ca_start_t = None
        elif self._ca_start_t is None:
            # Voltage held constant — start tracking CA decay time
            self._ca_start_t = now
        self._prev_duty = self._duty
        self._duty = new_duty

    def _elapsed_s(self) -> float:
        if self._t0 is None:
            self._t0 = time.time()
            self._last_write_t = self._t0
        return time.time() - self._t0

    def _setpoint_v(self) -> float:
        # Matches the project's normalization: duty 0..1 ↔ -2.5..+2.5 V
        return self._duty * 5.0 - 2.5

    def _iv_current_ma(self, v: float, t: float) -> float:
        # Smooth limiting I-V curve plus mild time-dependent drift.
        # Not electrochemistry-accurate, but stable and
        # "realistic enough" for UI/dev/testing.
        ilim = self._p.i_lim_ma
        v0 = self._p.e0_v
        # tanh gives a nice saturation and monotonic behavior.
        base = ilim * math.tanh((v - v0) / 0.25)
        # add some ohmic drop and slow drift
        drift = 0.05 * ilim * math.sin(2 * math.pi * (t / 12.0))
        return base + drift

    def _ca_current_ma(self, v: float, t: float) -> float:
        # Exponential decay with a small steady-state offset.
        amp = self._iv_current_ma(v, 0.0)
        return 0.15 * amp + 0.85 * amp * math.exp(-t / self._p.ca_tau_s)

    def _model_current_ma(self) -> float:
        t = self._elapsed_s()
        v = self._setpoint_v()
        # If the duty cycle has been held constant, produce CA-like decay.
        if self._ca_start_t is not None:
            ca_t = time.time() - self._ca_start_t
            return self._ca_current_ma(v, ca_t)
        return self._iv_current_ma(v, t)

    def read_a0(self) -> float:
        # Return value so read_write recovers setpoint voltage.
        v = self._setpoint_v()
        a0 = 0.5 + (-v / self._cf)
        a0 += self._rng.gauss(0.0, self._p.noise_std)
        return _clamp(a0, 0.0, 1.0)

    def read_a2(self) -> float:
        # Return value so read_write recovers modeled current.
        i_ma = self._model_current_ma()
        a2 = 0.5 + (-(i_ma * self._sr) / self._cf)
        a2 += self._rng.gauss(0.0, self._p.noise_std)
        return _clamp(a2, 0.0, 1.0)


def simulated_startup(
    *,
    conversion_factor: float = 5.0,
    shunt_resistor: float = 1000.0,
    seed: int | None = 0,
) -> tuple[str, SimulatedBoard, object, object, object]:
    """Drop-in replacement for routines.startup_routine() for simulation
    mode."""

    sim = SimulatedPotentiostat(
        conversion_factor=conversion_factor,
        shunt_resistor=shunt_resistor,
        seed=seed,
    )
    return "SIMULATED", sim.board, sim.a0, sim.a2, sim.d9
