**Added:**

* ``scripts/build_local_install.py`` to build an offline install bundle
  (pytentiostat wheel + dependency wheels) on an internet-connected machine
  for use on an air-gapped lab computer.

**Changed:**

* Rewrote ``scripts/install_from_local.bat`` to install pytentiostat offline
  from the bundled wheels into a virtual environment via
  ``pip install --no-index --find-links`` (Python 3.12, ``pip`` instead of the
  removed ``setup.py install``), and updated ``local-install/instructions.rst``
  to match.

**Deprecated:**

* <news item>

**Removed:**

* <news item>

**Fixed:**

* <news item>

**Security:**

* <news item>
