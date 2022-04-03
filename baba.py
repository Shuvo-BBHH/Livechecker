# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
import requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json, requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json
from multiprocessing.pool import ThreadPool
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    os.system('pip2 install requests')
    os.system('python2 jmbf.py')

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
os.system('clear')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
my_color = [
 O, U, B, K, H, M, P]
warna1 = random.choice(my_color)
my_color = [
 M, H, P, K, U, B, O]
warna2 = random.choice(my_color)
my_color = [
 U, O, K, P, H, K, B]
warna3 = random.choice(my_color)
__author__ = 'Mr.Jutt'
__copyright = 'All rights reserved . Copyright  Mr.Jutt'
try:
    os.mkdir('/sdcard/Jutt')
except OSError:
    pass

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for o in titik:
        print '\r %s[%s+%s] Please wait %s' % (P, O, P, o),
        sys.stdout.flush()
        time.sleep(1)


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s\xc3\x97%s] Delete token %s' % (P, M, P, x),
        sys.stdout.flush()
        time.sleep(1)


IP = requests.get('https://api.ipify.org').text
logo = '  \n %s\xe2\x95\xa6\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\xac \xe2\x94\xac\xe2\x94\xac \xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\xac  \xe2\x95\x94\xe2\x95\x97 \xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\n %s\xe2\x95\x91\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82  \xe2\x94\x82   \xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82  \xe2\x94\x82 \xe2\x94\x82  \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\xa4 \n%s\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4  \xe2\x94\xb4   \xe2\x95\xa9 \xe2\x95\xa9\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' % (P, warna, P)
logo2 = '%s \n     ___  __   __  _______  _______ \n    |   ||  | |  ||       ||       |\n    |   ||  | |  ||_     _||_     _|\n    |   ||  |_|  |  |   |    |   |  \n ___|   ||       |  |   |    |   |  \n|       ||       |  |   |    |   |  \n|_______||_______|  |___|    |___|  \n          %s *%s JuttBadshah Brand %s*\n%s--------------------------------------------------\n' % (warna, O, H, O, N)
host = 'https://mbasic.facebook.com'
ua = 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()

def reg():
    os.system('clear')
    print logo
    try:
        to = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://juttkey.000webhostapp.com/30day.txt').text
    if to in r:
        notice()
    else:
        os.system('clear')
        print logo
        print ''
        print '\t\t \x1b[4;31mApproved Failed'
        print ''
        print '\t%s    Your Api Is Not %sApproved' % (N, warna1)
        print ''
        print ' \t\x1b[1;92mCopy Your Api: \x1b[1;91m' + to
        print ''
        raw_input('\t\x1b[1;97m  And Press \x1b[1;91menter \x1b[1;97mto Input Api')
        os.system('xdg-open https://juttkey.000webhostapp.com/30day.php')
        time.sleep(5)
        print ''
        raw_input('\t\x1b[1;93m Press \x1b[1;96menter\x1b[1;93m To Check Approval ')
        os.system('xdg-open https://t.me/joinchat/3Ls9bUMjqpJkN2Jk')
        reg()


def reg2():
    os.system('clear')
    print logo2
    print '\t\t \x1b[4;31mApproval Not Detected'
    print ''
    print '\t%s   Your Api Is Not %sApproved' % (N, warna1)
    print ''
    id = uuid.uuid4().hex[:20]
    print ' \t\x1b[1;92mCopy Your Api: \x1b[1;91m' + id
    print ''
    raw_input('\t\x1b[1;97m  And Press \x1b[1;91menter \x1b[1;97mto Input Api')
    print ''
    os.system('xdg-open https://juttkey.000webhostapp.com/30day.php')
    time.sleep(5)
    sav = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'w')
    sav.write(id)
    sav.close()
    raw_input('\t\x1b[1;93m Press \x1b[1;96menter\x1b[1;93m To Check Approval ')
    reg()


from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 
   'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')

def yayanxd():
    os.system('clear')
    print logo2
    print '\n %s[%s1%s] Login Cookis Facebook' % (P, O, P)
    print ' %s[%s2%s] Login Token Facebook' % (P, O, P)
    pilih()


def pilih():
    m = raw_input('\n [*] choose : ')
    if m == '':
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        yayanxd()
    elif m == '1':
        os.system('clear')
        cokis()
    elif m == '2':
        token()
