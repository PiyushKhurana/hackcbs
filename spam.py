import pycurl
from StringIO import StringIO
import certifi
from urlparse import urlparse
import socket
import binascii
import xml.etree.ElementTree as ET


def check_connectivity(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((str(host), int(port)))
        s.close()
    except socket.timeout:
        print("SPAM")
        return False
    except:
        print("SPAM")
        return False

    return True



fileout = open("output.txt","w")

urllist = open("input.txt","r")
for url in urllist:
    print (url)
    if not url.strip():
        print ("empty")
    else:
        url = url.strip()
        port = 80
        if urlparse(url)[0] == "https":
            port = 443
        elif urlparse(url)[0] == "http":
            port = 80
        if check_connectivity(urlparse(url)[1],port):
            try:
                url = url+"/?"+msgs[0].strip()
                buffer = StringIO()
                c = pycurl.Curl()
                c.setopt(pycurl.CAINFO, certifi.where())
                c.setopt(c.URL,str(url))
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                code = c.getinfo(pycurl.RESPONSE_CODE)
                c.close()                        
                fileout.write(str(url)+"|"+str(code))
                fileout.write("\n")
            except:
                fileout.write(str(url)+"|"+str("All clear go ahead"))
                fileout.write("\n")
        else:
            fileout.write(str(url)+"|"+str("Hold On ! It may contains malicious content"))
            fileout.write("\n")

       
fileout.close()    
