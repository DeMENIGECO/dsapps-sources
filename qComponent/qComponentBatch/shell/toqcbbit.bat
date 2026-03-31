@echo off
echo Strumento To-QCBBit
set /p "file=File: (percorso completo) "

:: Variabili
set "tmp=%file%"
set "dir=%LOCALAPPDATA%\qComponent\qcb\temp"
set "eseg=%LOCALAPPDATA%\qComponent\qcb\eseguiti"

:: Crea cartelle se non esistono
if not exist "%dir%" mkdir "%dir%"
if not exist "%eseg%" mkdir "%eseg%"

:: Copia file nella cartella temp
xcopy "%tmp%" "%dir%\" /y >nul

:: Copia file nella cartella eseguiti
xcopy "%tmp%" "%eseg%\" /y >nul

:: Nome senza estensione
for %%F in ("%file%") do set "semplified=%%~nF"

:: Rinomina file nella temp con estensione .qcb
rename "%dir%\%%~nxF" "%semplified%.qcb"

echo Fatto!
pause
