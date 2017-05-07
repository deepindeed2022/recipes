
@echo The script use to add a system variables into system 
@echo off

:start
set /p name=Please input variable name.
set /p value=Please input variable value.

if not defined %name%  (set %name%=%value%)
set /p swith=Add the variable into system path? Y or N

if %switch% =="Y" set path=%path%;%name%\bin
else
	echo "not add varibles to system path"


set /p end=End?Y or N

if %end%=="N"
	goto start
else
	goto end

:end


