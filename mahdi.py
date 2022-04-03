try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests, uuid
    from multiprocessing.pool import ThreadPool
    from datetime import datetime
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Mcra3k.py')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('git pull')
if not os.path.isfile('/data/data/com.termux/files/home/cepat/ok/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    os.system('clear')
elif os.path.isfile('/data/data/com.termux/files/home/cepat/ok/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd Mohammad && node index.js &')
    os.system('clear')
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
N = '\x1b[0m'
G = '\x1b[0;32m'
GL = '\x1b[32;91m'
B = '\x1b[0;36m'
BL = '\x1b[36:1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'
my_color = [
 N, G, GL, B, BL, R, W, H, Y, YL]
warna = random.choice(my_color)
logo = '\n\n\n##     ##    ##    ## #### ##    ##  ######   \n###   ###    ##   ##   ##  ###   ## ##    ##  \n#### ####    ##  ##    ##  ####  ## ##        \n## ### ##    #####     ##  ## ## ## ##   #### \n##     ##    ##  ##    ##  ##  #### ##    ##  \n##     ##    ##   ##   ##  ##   ### ##    ##  \n##     ##    ##    ## #### ##    ##  ######   \n\n--------------------------------------------------\x1a\n\x1a Author      : Mohammad Sultani \n\x1a GitHub      : https://github.com/Mohammadjan1122\n\x1a YouTube     : Termux Master\n\x1a Telegram    : https://t.me/sultani1122\n Blogspot    : https://mohammadsultani.blogspot.com\n--------------------------------------------------\n'

def ip():
    os.system('clear')
    print logo
    print
    print '\tCollecting device info'
    print
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print 47 * '-'
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print 47 * '-'
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(1)
    print 47 * '-'
    print ' \x1b[1;92mYour network: ' + network
    time.sleep(1)
    print 47 * '-'
    print ' Loading ...'
    time.sleep(1)
    mohammad()


def mohammad():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = ('-').join(uuid)
    print logo
    print '\x1b[37;1mYour ID : ' + id
    try:
        httpCaht = requests.get('https://github.com/Mohammadjan1122/Mking1/blob/main/public.txt').text
        if id in httpCaht:
            print '\x1b[37;1mYOUR ID IS ACTIVE.........'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[37;1mYOUR ID IS NOT ACTIVE.........'
            time.sleep(1)
            sys.exit()
        try:
            open('.login.txt', 'r')
            b_menu()
        except IOError:
            login()

    except:
        sys.exit()
        if name == '__main__':
            mohammad()


def method_menu():
    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] Start Crack\n[ 2 ] update Script \n" | lolcat')
