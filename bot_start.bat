@echo off

call @~dp0Labs_With_Loves\venv\Scripts\activate

cd %~dp0Labs_With_Loves

set TOKEN=

python telegram_bot.py

pause