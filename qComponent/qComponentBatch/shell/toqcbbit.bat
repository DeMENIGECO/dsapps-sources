@echo off

echo Strumento To-QCBBit
set /p file=File: (percorso conpleto)

tmp = %file% 
dir = %LOCALAPPDATA%\qComponent\qcb\temp
xcopy %tmp% %dir%

total_dir = %dir%\%tmp%
eseg = :: Cartella file eseguito
xcopy %file% %eseg%

semplified = %remove[ext] file%

rename %tmp% %semplified%.qcb
