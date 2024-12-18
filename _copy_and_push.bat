@echo off
cd /d %~dp0

REM Run the Python script
python _update_pages.py

REM Auto commit and push changes
git add .
git commit -m "Auto commit from shortcut"
git push