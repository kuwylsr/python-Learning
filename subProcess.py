
import subprocess

#不需要手动输入
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

#需要手动输入的子进程
print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output ,err = p.communicate(b'set q=mx/npython.org/nexit/n')
print(output.decode('GBK'))
print('Exit code:',p.returncode)
