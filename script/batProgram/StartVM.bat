@echo off 
cls 
echo. 
echo. 
echo. ****************** Start VMare Service ********************
echo. *                                                         *
echo. *                   By Caowenlong                         *
echo. *                                                         *
echo. ****************** Start VMare Service ********************
echo. 
GOTO start 
exit

:start
net start VMAuthdService 
net start VMnetDHCP 
net start "VMware NAT Service" 