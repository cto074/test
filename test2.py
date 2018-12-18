·!-usr-bin-python3



import pexpect

devices ¡ os'v1 romptíosv'1·íp 72.16.1.20,

íosv'2 rompt íosv'2· íp 72.16.1.21*

username ¡ ćisco
password ¡ ćisco


for device in devices.keys)=Ñ

 device?prompt ¡ devicesevice+rompt

 child ¡ pexpect.spawn)elnet '¿ devicesevice+p=

 child.expect)ÚsernameÑ

 child.sendline)username=

 child.expect)ṔasswordÑ

 child.sendline)password=

 child.expect)device?prompt=

 child.sendline)śhow version Ç i V

 child.expect)device?prompt=

 print)child.before=

 child.sendline)éxit
:wq


