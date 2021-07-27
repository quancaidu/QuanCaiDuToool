import json, sys, os, time,re
from datetime import datetime as dt
from datetime import date
from datetime import datetime,timedelta
try:
  import requests
except:
  os.system("pip install requests")
  import requests
session = requests.Session()
today = date.today()
str2 = today.strftime("%d-%m-%Y")
headers = {
      		'Connection': 'keep-alive',
      		'Keep-Alive': '300',
      		'authority': 'tuongtaccheo.com',
      		'ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
      		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      		'cache-control': 'max-age=0',
      		'upgrade-insecure-requests': '1',
      		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      		'sec-fetch-site': 'none',
      		'sec-fetch-mode': 'navigate',
      		'sec-fetch-user': '?1',
      		'sec-fetch-dest': 'document',
      		}

ch = 0
while (ch==0):
  os.system("clear")
  print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Vào Tool.',end="\r")
  time.sleep(1)
  print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Vào Tool..',end="\r")
  time.sleep(1)
  print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Vào Tool...',end="\r")
  time.sleep(1)
  print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Vào Tool....',end="\r")
  time.sleep(1)
  print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mTương Tác Chéo")
  time.sleep(0.1)
  print("\033[1;31m      ██║██║████╗ ██║ \033[1;96mVersion:\033[1;37m0.1")
  time.sleep(0.1)
  print("\033[1;32m      ██║██║██╔██╗██║ \033[1;96mTool Free")
  time.sleep(0.1)
  print("\033[1;96m ██╗  ██║██║██║╚████║ \033[1;96mNgày:\033[1;37m", str2)
  time.sleep(0.1)
  print("\033[1;95m ╚█████╔╝██║██║ ╚███║ \033[1;96m@Copyright: \033[1;33mQuân 2K7")
  time.sleep(0.1)
  print("\033[1;97m  ╚════╝ ╚═╝╚═╝  ╚══╝ ")
  time.sleep(0.1)
  print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - -")
  if (not os.path.isfile('tkmk.txt')):
    user = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Tài Khoản TTC: \033[1;95m')
    pasw = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Mật Khẩu TTC: \033[1;95m')
  else:
    h = input(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhấn\033[1;33m Enter\033[1;32m Để Vào Tài Khoản Cũ, \033[1;32mNhấn\033[1;33m No\033[1;32m Để Vào Tài Khoản Mới: \033[1;95m")
    if (h==""):
      re=open('tkmk.txt', 'r', encoding='utf-8').read().split('\n')
      try:
        user = re[0]
        pasw = re[1]
      except:
        print(' \033[1;37m➻\033[1;96m❥ \033[1;32mLỗi Khi Lấy Tài Khoản. Hãy Chạy Lại Tool')
        os.remove("tkmk.txt")
        sys.exit(0)
    else:
      user = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Tài Khoản TTC: \033[1;95m')
      pasw = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Mật Khẩu TTC: \033[1;95m')
  data = {
    'username': user,
    'password': pasw,
    'submit': ' ĐĂNG NHẬP',
  }
  try:
    s = session.post('https://tuongtaccheo.com/login.php', headers=headers, data=data)
    reg = s.text
    t = session.cookies.get_dict()
    ph = t['PHPSESSID']
    if int(reg.count('Sai tài khoản'))>0:
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập.',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập..',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập...',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập....',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;31mSai Tài Khoản TTC')
      os.remove('tkmk.txt')
      ch = 0
      time.sleep(1)
    else:
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập.',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập..',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập...',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Đăng Nhập....',end="\r")
      time.sleep(1)
      print(' \033[1;37m➻\033[1;96m❥ \033[1;32mĐăng Nhập Thành Công')
      ch = 1
      co = user+"\n"+pasw
      c=open('tkmk.txt','w+')
      c.write(co)
      c.close()
  except:
    print(' \033[1;37m➻\033[1;96m❥ \033[1;31mXảy Ra Lỗi Vui Lòng Đăng Nhập Lại',end="\r")
    ch = 0
    time.sleep(2)
    print('                                           ', end='\r')
keyttc = '_ga=GA1.2.1500701940.1621419545; _fbp=fb.1.1621419545996.7138875; __tawkuuid=e::tuongtaccheo.com::Q9Wp0PpxdaPPSauZ9+vwmtdM1UA2gWlyG0GIFEjkSr9HkXAOJNzqsTAdYqmPdrkS::2; _gid=GA1.2.239860297.1623436076; PHPSESSID=' +ph+'; _gat_gtag_UA_88794877_6=1'
cookiettc= {'cookie':keyttc}
requeststtc = requests.get("https://tuongtaccheo.com/home.php", headers = cookiettc).text
xr1 = requeststtc.split('id="soduchinh">')
xr2 = xr1[1].split('</strong>')
xu = xr2[0]
os.system("clear")
print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mTương Tác Chéo")
time.sleep(0.1)
print("\033[1;31m      ██║██║████╗ ██║ \033[1;96mVersion:\033[1;37m0.1")
time.sleep(0.1)
print("\033[1;32m      ██║██║██╔██╗██║ \033[1;96mTool Free")
time.sleep(0.1)
print("\033[1;96m ██╗  ██║██║██║╚████║ \033[1;96mNgày:\033[1;37m", str2)
time.sleep(0.1)
print("\033[1;95m ╚█████╔╝██║██║ ╚███║ \033[1;96m@Copyright: \033[1;33mQuân 2K7")
time.sleep(0.1)
print("\033[1;97m  ╚════╝ ╚═╝╚═╝  ╚══╝ ")
time.sleep(0.1)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - -")
print(" \033[1;37m➻\033[1;96m❥ \033[1;33mẤn \033[1;31mEnter \033[1;33mĐể Dừng")
i=0
access_token = 'tai'
mangtoken = []
while (access_token!=''):
  i=i+1
  access_token = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Token Facebook \033[1;33m'+ str(i) +': \033[1;37m')
  if (access_token!=''):
    mangtoken.append(access_token)
time.sleep(1)



os.system("clear")
print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mTương Tác Chéo")
time.sleep(0.1)
print("\033[1;31m      ██║██║████╗ ██║ \033[1;96mVersion:\033[1;37m0.1")
time.sleep(0.1)
print("\033[1;32m      ██║██║██╔██╗██║ \033[1;96mTool Free")
time.sleep(0.1)
print("\033[1;96m ██╗  ██║██║██║╚████║ \033[1;96mNgày:\033[1;37m", str2)
time.sleep(0.1)
print("\033[1;95m ╚█████╔╝██║██║ ╚███║ \033[1;96m@Copyright: \033[1;33mQuân 2K7")
time.sleep(0.1)
print("\033[1;97m  ╚════╝ ╚═╝╚═╝  ╚══╝ ")
time.sleep(0.1)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - -")
time.sleep(0.1)

print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Kiểm Tra Xu.',end="\r")
time.sleep(1)
print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Kiểm Tra Xu..',end="\r")
time.sleep(1)
print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Kiểm Tra Xu...',end="\r")
time.sleep(1)
print(' \033[1;37m➻\033[1;96m❥ \033[1;96mĐang Kiểm Tra Xu....',end="\r")
time.sleep(1)
print(' \033[1;37m➻\033[1;96m❥ \033[33mTài Khoản: \033[1;37m' + user + ' \033[33mCó: \033[1;37m' + str(xu)+'\033[33m Xu')
time.sleep(0.1)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - -")
time.sleep(0.1)
print(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập \033[1;37m[\033[1;33m1\033[0m\033[1;37m] \033[1;33m=> \033[1;32mChạy Nhiệm Vụ Follow")
time.sleep(0.1)
print(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập \033[1;37m[\033[1;33m2\033[0m\033[1;37m] \033[1;33m=> \033[1;32mChạy Nhiệm Vụ Share")
time.sleep(0.1)
print(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập \033[1;37m[\033[1;33m3\033[0m\033[1;37m] \033[1;33m=> \033[1;32mChạy Nhiệm Vụ Like")
time.sleep(0.1)
print(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập \033[1;37m[\033[1;33m4\033[0m\033[1;37m] \033[1;33m=> \033[1;32mChạy Nhiệm Vụ Comment")
time.sleep(0.1)
print(" \033[1;37m➻\033[1;96m❥ \033[1;33mMuốn Random Thì Ghép Số Lại (Ví Dụ 1+2)")
time.sleep(0.1)
chonnv = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mVui Lòng Chọn Nhiệm Vụ: \033[1;95m')
delay = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Thời Gian Delay Mỗi Job: \033[1;95m')
sl = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mSau Bao Nhiêu Nhiệm Vụ Dừng Tránh Block: \033[1;95m')
delaybl = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mDừng Tránh Block Bao Nhiêu Giây: \033[1;95m')
if (int(len(mangtoken))>1):
  doiacc = input(' \033[1;37m➻\033[1;96m❥ \033[1;32mSau Bao Nhiêu Nhiệm Vụ Thì Đổi Acc: \033[1;95m')
time.sleep(1)
os.system("clear")
print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mTương Tác Chéo")
time.sleep(0.1)
print("\033[1;31m      ██║██║████╗ ██║ \033[1;96mVersion:\033[1;37m0.1")
time.sleep(0.1)
print("\033[1;32m      ██║██║██╔██╗██║ \033[1;96mTool Free")
time.sleep(0.1)
print("\033[1;96m ██╗  ██║██║██║╚████║ \033[1;96mNgày:\033[1;37m", str2)
time.sleep(0.1)
print("\033[1;95m ╚█████╔╝██║██║ ╚███║ \033[1;96m@Copyright: \033[1;33mQuân 2K7")
time.sleep(0.1)
print("\033[1;97m  ╚════╝ ╚═╝╚═╝  ╚══╝ ")
time.sleep(0.1)
print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - -")

def follow(uid, access_token):
  link = 'https://graph.facebook.com/' + uid + '/subscribers'
  data = {
  	'access_token': access_token,
  	}
  headers = {
  		'Connection': 'keep-alive',
  		'Keep-Alive': '300',
  		'authority': 'm.facebook.com',
  		'ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
  		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  		'cache-control': 'max-age=0',
  		'upgrade-insecure-requests': '1',
  		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  		'sec-fetch-site': 'none',
  		'sec-fetch-mode': 'navigate',
  		'sec-fetch-user': '?1',
  		'sec-fetch-dest': 'document',
  		}
  response = requests.post(link, headers=headers, data=data)
  return response
def like(uid, access_token):
  link = 'https://graph.facebook.com/'+ uid + '/likes'
  data = {
  	'access_token': access_token,
  	}
  headers = {
  		'Connection': 'keep-alive',
  		'Keep-Alive': '300',
  		'authority': 'm.facebook.com',
  		'ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
  		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  		'cache-control': 'max-age=0',
  		'upgrade-insecure-requests': '1',
  		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  		'sec-fetch-site': 'none',
  		'sec-fetch-mode': 'navigate',
  		'sec-fetch-user': '?1',
  		'sec-fetch-dest': 'document',
  		}
  response = requests.post(link, headers=headers, data=data)
  return response
def cmt(uid,msg,access_token):
  link = 'https://graph.facebook.com/'+uid+'/comments'
  data = {
  	'access_token': access_token,
  	'message': msg,
  	}
  headers = {
  		'Connection': 'keep-alive',
  		'Keep-Alive': '300',
  		'authority': 'm.facebook.com',
  		'ccept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
  		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  		'cache-control': 'max-age=0',
  		'upgrade-insecure-requests': '1',
  		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  		'sec-fetch-site': 'none',
  		'sec-fetch-mode': 'navigate',
  		'sec-fetch-user': '?1',
  		'sec-fetch-dest': 'document',
  		}
  response = requests.post(link, headers=headers, data=data)
  return response
def share(uid,access_token):
  link = 'https://mbasic.facebook.com/' + uid
  data = {
	'privacy': '{"value":"EVERYONE"}',
	'link': link,
	'access_token': access_token,
	}
  response = requests.post('https://graph.facebook.com/v2.0/me/feed', data=data)
  return response

def hoanthanh(url, tokentds):
  try:
    n = requests.get(url).text
    nn = json.loads(n)
    nnn = nn['success']
    if (hhh == 200):
      return nn['data']['xu']
  except:
    return 0
def rundelay(k):
  while (k>0):
    print('                                        ', end='\r')
    print(' \033[1;37m➻\033[1;96m❥ \033[1;32m Đang Chờ Delay Nhiệm Vụ \033[1;33m' + str(k), end='\r')
    time.sleep(1)
    k=k-1
    print(' \033[1;37m➻\033[1;96m❥ \033[1;32m Đang Chờ Delay Nhiệm Vụ \033[1;33m' + str(k), end='\r')
def rundelaybl(b):
  while (b>0):
    print('                                            ', end='\r')
    print(' \033[1;37m➻\033[1;96m❥ \033[1;32m Đang Chờ Delay Block \033[1;33m' + str(b), end='\r')
    time.sleep(1)
    b=b-1
    print(' \033[1;37m➻\033[1;96m❥ \033[1;32m Đang Chờ Delay Block \033[1;33m' + str(b), end='\r')
def getnv(url,referer,cookie):
  headers = {
    'Host': 'tuongtaccheo.com',
    'accept': '*/*',
    'origin': 'https://tuongtaccheo.com',
    'x-requested-with': 'XMLHttpRequest',
    'save-data': 'on',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'referer': referer,
    'accept-language': 'vi-VN, vi;q=0.9,fr-FR;q=0.8,fr;q=0.7, en-US;q=0.6,en;q=0.5,zh-CN;q=0.4.zh;q=0.3',
    'cookie': cookie,
  }
  try:
    m = requests.get(url,headers=headers).text
  except:
    m = ''
  return m
def nhantien(idnv,url,referer,cookie):
  data = {"id": idnv}
  headers = {
    'Host': 'tuongtaccheo.com',
    'accept': '*/*',
    'origin': 'https://tuongtaccheo.com',
    'x-requested-with': 'XMLHttpRequest',
    'save-data': 'on',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'referer': referer,
    'accept-language': 'vi-VN, vi;q=0.9,fr-FR;q=0.8,fr;q=0.7, en-US;q=0.6,en;q=0.5,zh-CN;q=0.4.zh;q=0.3',
    'cookie': cookie,
  }
  try:
    m = requests.post(url,data=data,headers=headers).text
  except:
    m = ''
  return m
stt = 0
if int(chonnv.count('1'))>0:
  co_sub = 1
else:
  co_sub = 0
if int(chonnv.count('2'))>0:
  co_share = 1
else:
  co_share = 0
if int(chonnv.count('3'))>0:
  co_like = 1
else:
  co_like = 0
if int(chonnv.count('4'))>0:
  co_cmt = 1
else:
  co_cmt = 0
while (True):
  if (int(len(mangtoken))==0):
    print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTất Cả Token Facebook Đã Die Hoặc Bị Block')
    break
  for sttacc in range(len(mangtoken)):
    try:
      access_token = mangtoken[sttacc]
    except:
      continue
    try:
      iid = requests.get(f'https://graph.facebook.com/me/?access_token={access_token}').text
      idfb = json.loads(iid)['id']
      tenfb = json.loads(iid)['name']
    except:
      print(' \033[1;37m➻\033[1;96m❥ \033[1;31mToken Facebook Die')
      mangtoken.remove(access_token)
      continue
    try:
      data = {
        'iddat[]': idfb, 
        'loai': 'fb',
      }
      headers = {
        'Host': 'tuongtaccheo.com',
        'accept': '*/*',
        'origin': 'https://tuongtaccheo.com',
        'x-requested-with': 'XMLHttpRequest',
        'save-data': 'on',
      	'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      	'referer': 'https://tuongtaccheo.com/cauhinh/index.php',
      	'accept-language': 'vi-VN, vi;q=0.9,fr-FR;q=0.8,fr;q=0.7, en-US;q=0.6,en;q=0.5,zh-CN;q=0.4.zh;q=0.3',
      	'cookie': keyttc,
      }
      s = requests.post('https://tuongtaccheo.com/cauhinh/datnick.php',data=data, headers=headers).text
      if (s=='1'):
        print(' \033[1;37m➻\033[1;96m❥ \033[1;32mĐang Chạy Nick Facebook \033[1;33m' + tenfb)
      else:
        int('taihandsome')
    except:
      print(' \033[1;37m➻\033[1;96m❥ \033[1;31mCấu Hình Thất Bại. Hãy Thêm ' + tenfb + ' Vào Cấu Hình Web')
      mangtoken.remove(access_token)
      continue
    spam = 0
    while (True):
      if (spam == 1):
        break
      if (co_sub == 1):
        try:
          urlsub = 'https://tuongtaccheo.com/kiemtien/subcheo/getpost.php'
          referer = 'https://tuongtaccheo.com/kiemtien/subcheo'
          m = getnv(urlsub,referer,keyttc)
          nvsub1 = json.loads(m)
        except:
          print('                                        ', end='\r')
          print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTạm Thời Hết Nhiệm Vụ Follow')
      if (co_like == 1):
        try:
          url_like = 'https://tuongtaccheo.com/kiemtien/getpost.php'
          referer = 'https://tuongtaccheo.com/kiemtien/'
          m = getnv(url_like,referer,keyttc)
          nvlike1 = json.loads(m)
        except:
          print('                                        ', end='\r')
          print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTạm Thời Hết Nhiệm Vụ Like')
      if (co_cmt == 1):
        try:
          url_cmt = 'https://tuongtaccheo.com/kiemtien/cmtcheo/getpost.php'
          referer = 'https://tuongtaccheo.com/kiemtien/cmtcheo'
          m = getnv(url_cmt,referer,keyttc)
          nvcmt1 = json.loads(m)
        except:
          print('                                        ', end='\r')
          print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTạm Thời Hết Nhiệm Vụ Comment')
      if (co_share == 1):
        try:
          url_share = 'https://tuongtaccheo.com/kiemtien/sharecheo/getpost.php'
          referer = 'https://tuongtaccheo.com/kiemtien/sharecheo'
          m = getnv(url_share,referer,keyttc)
          nvshare1 = json.loads(m)
        except:
          print('                                        ', end='\r')
          print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTạm Thời Hết Nhiệm Vụ Share')
      for i in range(20):
        if (co_sub == 1):
          try:
            idsub = nvsub1[i]['idpost']
          except:
            break
          try:
            m = follow(idsub,access_token)
          except:
            pass
          try:
            c = json.loads(m.text)
            cc = c['error']['code']
            if (cc == 190):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mToken Facebook Die')
              mangtoken.remove(access_token)
              spam = 1
              sttacc = sttacc-1
              break
            if (cc == 405):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTài Khoản Bị Checkpoint')
              mangtoken.remove(access_token)
              spam = 1
              sttacc = sttacc-1
              break
            if (cc == 368):
              ms = c['error']['message']
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31m'+ms)
              mangtoken.remove(access_token)
              spam = 1
              sttacc = sttacc-1
              break
          except:
            pass
          tg=datetime.now().strftime('%H:%M')
          mess = nhantien(idsub,"https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php","https://tuongtaccheo.com/kiemtien/subcheo/",keyttc)
          if mess.find("Thành công") <1:
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31m [' + str(stt) + '] ● ' +tg +' ● FOLLOW ' + '● ' + idsub + ' ● ' + 'ERROR', end='\r')
          else:
            stt = stt+1
            xu = int(xu) + 600
            print('                                                   ', end='\r')
            print(' \033[1;33m[\033[1;37m' + str(stt) + '\033[1;33m]\033[1;37m <> \033[93m[\033[1;36m' +tg +'\033[33m]\033[1;37m <>\033[33m [\033[1;32mFOLLOW\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + idsub + '\033[33m]\033[1;37m <> \033[1;33m[\033[37m+600\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + str(xu) +'\033[33m]')
            k = int(delay)
            if (stt%int(sl) == 0):
              rundelaybl(int(delaybl))
            if (int(len(mangtoken))>1):
              if (stt%int(doiacc) == 0):
                spam = 1
                break
            rundelay(k)
        if (co_share == 1):
          try:
            idshare = nvshare1[i]['idpost']
          except:
            break
          try:
            m = share(idshare,access_token)
          except:
            pass
          try:
            c = json.loads(m.text)
            cc = c['error']['code']
            if (cc == 190):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mToken Facebook Die')
              mangtoken.remove(access_token)
              spam = 1
              break
            if (cc == 405):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTài Khoản Bị Checkpoint')
              mangtoken.remove(access_token)
              spam = 1
              break
            if (cc == 368):
              ms = c['error']['message']
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31m'+ms)
              mangtoken.remove(access_token)
              spam = 1
              break
          except:
            pass
          tg=datetime.now().strftime('%H:%M')
          mess = nhantien(idshare,"https://tuongtaccheo.com/kiemtien/sharecheo/nhantien.php","https://tuongtaccheo.com/kiemtien/sharecheo",keyttc)
          if mess.find("Thành công") <1:
            print(' \033[1;37m➻\033[1;96m❥ \033[1;31m [' + str(stt) + '] ● ' +tg +' ●  SHARE ' + '● ' + idshare + ' ● ' + 'ERROR', end='\r')
          else:
            stt = stt+1
            xu = int(xu)+600
            print('                                                   ', end='\r')
            print(' \033[1;33m[\033[1;37m' + str(stt) + '\033[1;33m]\033[1;37m <> \033[93m[\033[1;36m' +tg +'\033[33m]\033[1;37m <>\033[33m [\033[1;32mSHARE\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + idshare + '\033[33m]\033[1;37m <> \033[1;33m[\033[37m+600\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + str(xu) +'\033[33m]')
            k = int(delay)
            if (stt%int(sl) == 0):
              rundelaybl(int(delaybl))
            if (int(len(mangtoken))>1):
              if (stt%int(doiacc) == 0):
                spam = 1
                break
            rundelay(k)
        if (co_like == 1):
          try:
            idlike = nvlike1[i]['idpost']
          except:
            break
          try:
            m = like(idlike,access_token)
          except:
            pass
          try:
            c = json.loads(m.text)
            cc = c['error']['code']
            if (cc == 190):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mToken Facebook Die')
              mangtoken.remove(access_token)
              spam = 1
              break
            if (cc == 405):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTài Khoản Bị Checkpoint')
              mangtoken.remove(access_token)
              spam = 1
              break
            if (cc == 368):
              ms = c['error']['message']
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31m'+ms)
              mangtoken.remove(access_token)
              spam = 1
              break
          except:
            pass
          tg=datetime.now().strftime('%H:%M')
          mess = nhantien(idlike,"https://tuongtaccheo.com/kiemtien/nhantien.php","https://tuongtaccheo.com/kiemtien/",keyttc)
          if mess.find("Thành công") <1:
            print(' \033[1;37m➻\033[1;96m❥ \033[1;31m [' + str(stt) + '] ● ' +tg +' ●  LIKE  ' + '● ' + idlike + ' ● ' + 'ERROR', end='\r')
          else:
            stt = stt+1
            xu = int(xu)+300
            print('                                                   ', end='\r')
            print(' \033[1;33m[\033[1;37m' + str(stt) + '\033[1;33m]\033[1;37m <> \033[93m[\033[1;36m' +tg +'\033[33m]\033[1;37m <>\033[33m [\033[1;32mLIKE\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + idlike + '\033[33m]\033[1;37m <> \033[1;33m[\033[37m+300\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + str(xu) +'\033[33m]')
            k = int(delay)
            if (stt%int(sl) == 0):
              rundelaybl(int(delaybl))
            if (int(len(mangtoken))>1):
              if (stt%int(doiacc)== 0):
                spam = 1
                break
            rundelay(k)
        if (co_cmt == 1):
          try:
            idcmt = nvcmt1[i]['idpost']
            msgg = nvcmt1[i]['nd']
            msg = json.loads(msgg)[0]
          except:
            break
          try:
            m = cmt(idcmt,msg,access_token)
          except:
            pass
          try:
            c = json.loads(m.text)
            cc = c['error']['code']
            if (cc == 190):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mToken Facebook Die')
              mangtoken.remove(access_token)
              spam = 1
              break
            if (cc == 405):
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31mTài Khoản Bị Checkpoint')
              mangtoken.remove(access_token)
              spam = 1
              break
            if (cc == 368):
              ms = c['error']['message']
              print(' \033[1;37m➻\033[1;96m❥ \033[1;31m'+ms)
              mangtoken.remove(access_token)
              spam = 1
              break
          except:
            pass
          tg=datetime.now().strftime('%H:%M')
          mess = nhantien(idcmt,"https://tuongtaccheo.com/kiemtien/cmtcheo/nhantien.php","https://tuongtaccheo.com/kiemtien/cmtcheo",keyttc)
          if mess.find("Thành công") <1:
            print(' \033[1;31m [' + str(stt) + '] ● ' +tg +' ●  CMT  ' + '● ' + idcmt + ' ● ' + 'ERROR', end='\r')
          else:
            stt = stt+1
            xu= int(xu)+600
            print('                                                   ', end='\r')
            print(' \033[1;33m[\033[1;37m' + str(stt) + '\033[1;33m]\033[1;37m <> \033[93m[\033[1;36m' +tg +'\033[33m]\033[1;37m <>\033[33m [\033[1;32mCMT\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + idcmt + '\033[33m]\033[1;37m <> \033[1;33m[\033[37m+600\033[33m]\033[1;37m <> \033[33m[\033[1;37m' + str(xu) +'\033[33m]')
            k = int(delay)
            if (stt%int(sl) == 0):
              rundelaybl(int(delaybl))
            if (int(len(mangtoken))>1):
              if (stt%int(doiacc) == 0):
                spam = 1
                break
            rundelay(k)
