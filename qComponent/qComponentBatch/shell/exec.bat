:: init
@echo off

:main
set /p command=QCB-Shell /qcomponentdir^>^>

:: verifica comando
if /i "%command%"=="help" goto help
if /i "%command%"=="pausa" goto user_pausa
if /i "%command%"=="cls" goto cmd_cls

:: comando sconosciuto
echo Comando %command% sconosciuto.
goto pausa

:: lista comandi

:: help
:help
echo.
echo help              [:]        Mostra questo menu
echo pausa             [:]        Test della pausa
echo cls               [:]        Pulisce schermo
goto pausa

:: pausa (cmd)
:user_pausa
echo.
echo Test: comando pausa
goto pausa

:: cls
:cmd_cls
cls
goto main

::ALTRI

:: pausa
:pausa
echo.
pause
goto main
