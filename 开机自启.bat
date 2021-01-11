@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin
C:
cd C:\Users\pc\Desktop\自动打卡
python 打卡.py