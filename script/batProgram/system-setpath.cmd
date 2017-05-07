@REM The script use to add a path into system path
@REM user could running with a parameter 

@echo off
if not "%path%" == ""  @echo %path%>>%CD%/system_path_backup.txt

if not "%1" == "" goto setPath
goto end
:setPath
set path=%path%;%1
:end
