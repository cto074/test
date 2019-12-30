#!/usr/bin/pexpect

import pexpect

devices = {'iosv-1':{'prompt':'R1#','ip':'192.168.17.135'}}
username = 'cisco'
password = 'cisco'

for device in devices.keys():
	 device_prompt = devices[device]['prompt']
	 child = pexpect.spawn('telnet ' + devices[device]['ip'])
	 child.logfile = open('debug', 'wb')
	 child.expect('Username:')
	 child.sendline(username)
	 child.expect('Password:')
	 child.sendline(password)
	 child.expect(device_prompt)
	 child.sendline('show version | i V')
	 child.expect(device_prompt)
	 print(child.before)
	 child.sendline('exit')



