@echo off
chcp 65001
cd /d "%~dp0"
echo Запуск генератора резюме...
python src\gui.py
pause