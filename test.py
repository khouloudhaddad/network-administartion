import pexpect
print("The current working directory: \n%s"
%pexpect.run('pwd').decode("utf-8"))
ssh = pexpect.spawn('ssh
developer@sandbox-iosxe-latest-1.cisco.com -y')
ssh.expect('Password:')
ssh.sendline('C1sco12345')
ssh.expect('#')
ssh.sendline('enable')
ssh.expect('#')
ssh.sendline('sh ip int br')
ssh.expect('--More--')
print(ssh.before.decode('utf-8'))
ssh.close()