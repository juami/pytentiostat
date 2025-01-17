:: This batch script will build html files from the ReStructuredtext files in docs
@echo off
cd docs
make html
cd ..
@pause
goto:eof
