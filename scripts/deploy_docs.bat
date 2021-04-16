:: This batch script will build html files from the ReStructedtext files in docs
@echo off
cd docs
make html
cd ..
@pause
goto:eof