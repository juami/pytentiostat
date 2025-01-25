@echo off
call :s_which py.exe

if not "%_path%" == "" (
  if "%1" == "--version" (
    py -3 -c "import pytentiostat; print(pytentiostat.__version__)"
  ) else (
    py -3 -m pytentiostat %*
  )
) else (
  if "%1" == "--version" (
    python -c "import pytentiostat; print(pytentiostat.__version__)"
  ) else (
    python -m pytentiostat %*
  )
)

goto :eof

:s_which
  setlocal
  endlocal & set _path=%~$PATH:1
  goto :eof
