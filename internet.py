import urllib.request
import socket

# print(urllib.request.urlopen('https://google.com'))  # Python 3.x


def ping(host='https://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        print('ping - ' + host + ' --succeed')
        return True
    except:
        print('ping - ' + host + ' --failed')
        return False


def defaultGateway():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipadd = s.getsockname()[0]
    ipadds = ipadd.split('.', 3)
    ipadds[3] = '1'

    ipadd_default = ".".join(ipadds)
    s.close()

    return ipadd_default
