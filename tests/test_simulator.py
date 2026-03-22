import matplotlib
import pytest

from pytentiostat.simulator import (
    SimulatedBoard,
    SimulatedPotentiostat,
    simulated_startup,
)

matplotlib.use("Agg", force=True)


# ---------------------------------------------------------------------------
# Shared config used by experiment integration tests
# ---------------------------------------------------------------------------
@pytest.fixture()
def config_data():
    return {
        "general_parameters": {
            "experiment_type": "CA",
            "data_output_filename": "test",
            "data_output_path": "desktop",
            "rest_time": 0.1,
            "step_number": 5,
        },
        "chronoamperometry": {"voltage": 0.5, "time": 1.0},
        "linear_sweep_voltammetry": {
            "start_voltage": 0.0,
            "end_voltage": 0.1,
            "sweep_rate": 100.0,
        },
        "cyclic_voltammetry": {
            "start_voltage": 0.0,
            "first_turnover_voltage": 0.1,
            "second_turnover_voltage": -0.1,
            "sweep_rate": 100.0,
            "number_of_cycles": 1,
        },
        "advanced_parameters": {
            "average_number": 1,
            "conversion_factor": 5.0,
            "setpoint_gain": 1.0,
            "setpoint_offset": 0.0,
            "shunt_resistor": 1000.0,
            "time_step": 0.01,
        },
    }


# ---------------------------------------------------------------------------
# Unit tests for SimulatedPotentiostat
# ---------------------------------------------------------------------------
class TestSimulatedPotentiostat:
    def test_default_construction(self):
        sim = SimulatedPotentiostat()
        assert sim.d9 is not None
        assert sim.a0 is not None
        assert sim.a2 is not None
        assert sim.board is not None

    def test_read_a0_returns_float_in_range(self):
        sim = SimulatedPotentiostat(seed=42)
        sim.d9.write(0.5)
        val = sim.a0.read()
        assert isinstance(val, float)
        assert 0.0 <= val <= 1.0

    def test_read_a2_returns_float_in_range(self):
        sim = SimulatedPotentiostat(seed=42)
        sim.d9.write(0.5)
        val = sim.a2.read()
        assert isinstance(val, float)
        assert 0.0 <= val <= 1.0

    def test_duty_cycle_clamped(self):
        sim = SimulatedPotentiostat(seed=0)
        sim.set_duty_cycle(-0.5)
        assert sim._duty == 0.0
        sim.set_duty_cycle(1.5)
        assert sim._duty == 1.0

    def test_reproducible_with_seed(self):
        sim1 = SimulatedPotentiostat(seed=7)
        sim2 = SimulatedPotentiostat(seed=7)
        sim1.d9.write(0.6)
        sim2.d9.write(0.6)
        assert sim1.a0.read() == sim2.a0.read()
        assert sim1.a2.read() == sim2.a2.read()

    def test_voltage_recovery(self):
        """The voltage read back from a0 should approximately match the
        setpoint after the operator's conversion formula is applied."""
        cf = 5.0
        sim = SimulatedPotentiostat(conversion_factor=cf, seed=0)
        duty = 0.7
        sim.d9.write(duty)
        a0_val = sim.a0.read()
        recovered_v = (a0_val - 0.5) * -cf
        expected_v = duty * 5.0 - 2.5  # 1.0 V
        assert abs(recovered_v - expected_v) < 0.1

    def test_board_exit_does_not_raise(self):
        board = SimulatedBoard()
        board.exit()  # should be a no-op


# ---------------------------------------------------------------------------
# Test simulated_startup() helper
# ---------------------------------------------------------------------------
class TestSimulatedStartup:
    def test_returns_correct_tuple(self):
        com, board, a0, a2, d9 = simulated_startup()
        assert com == "SIMULATED"
        assert hasattr(board, "exit")
        assert hasattr(a0, "read")
        assert hasattr(a2, "read")
        assert hasattr(d9, "write")


# ---------------------------------------------------------------------------
# Integration: run each experiment type through the simulator
# ---------------------------------------------------------------------------
def _run_experiment(config_data, exp_type, monkeypatch):
    from pytentiostat.operator import experiment

    config_data["general_parameters"]["experiment_type"] = exp_type
    monkeypatch.setattr(
        "pytentiostat.operator.time.sleep", lambda *a, **kw: None
    )
    sim = SimulatedPotentiostat(
        conversion_factor=config_data["advanced_parameters"][
            "conversion_factor"
        ],
        shunt_resistor=config_data["advanced_parameters"]["shunt_resistor"],
        seed=0,
    )
    return experiment(config_data, sim.a0, sim.a2, sim.d9)


def test_simulated_ca_experiment(config_data, monkeypatch):
    times, voltages, currents, interrupt = _run_experiment(
        config_data, "CA", monkeypatch
    )
    assert not interrupt
    assert len(times) == len(voltages) == len(currents)
    assert len(times) > 0


def test_simulated_lsv_experiment(config_data, monkeypatch):
    times, voltages, currents, interrupt = _run_experiment(
        config_data, "LSV", monkeypatch
    )
    assert not interrupt
    assert len(times) == len(voltages) == len(currents)
    assert len(times) > 0


def test_simulated_cv_experiment(config_data, monkeypatch):
    times, voltages, currents, interrupt = _run_experiment(
        config_data, "CV", monkeypatch
    )
    assert not interrupt
    assert len(times) == len(voltages) == len(currents)
    assert len(times) > 0
