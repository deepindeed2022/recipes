@echo *********************************************
@echo ***********Wifi start up ......**************
@echo *This is caowenlong's wifi start bat program*
@echo *********************************************
netsh wlan start hostednetwork
@echo ***********Wifi have started.****************

@echo off
echo Starting goagent
D:\Program Files\Over the wall\goagent-3.0\local\goagent.exe
exit


