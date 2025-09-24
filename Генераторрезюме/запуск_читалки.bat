@echo off
chcp 65001
cd /d "%~dp0"
echo Запуск читалки резюме...
python src\resume_reader.py
pause