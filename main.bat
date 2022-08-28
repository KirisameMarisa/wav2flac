echo off
SET /P INPUT="Input wav directory:"
call python main.py "%INPUT%"

pause
