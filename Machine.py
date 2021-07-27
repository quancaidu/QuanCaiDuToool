import os,sys, requests, threading,time,re,random
from datetime import datetime as dt
from datetime import date
from datetime import datetime,timedelta
try:
  import requests
except:
  import requests
session = requests.Session()
today = date.today()
str2 = today.strftime("%d-%m-%Y")
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
color=[red,yellow,green,blue]
jo=random.randint(0,3)
def hack(r,id,ti):
	home=requests.get("https://www.machine-liker.com/",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"}).headers["Set-Cookie"].split(";")[0]
	l=requests.get("https://www.machine-liker.com/login/",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","cookie":home}).text
	link="https://www.facebook.com/device?user_code="+l.split("https://www.facebook.com/device?user_code=")[1].split('"')[0]
	print("\033[1;33m[\033[1;96m+\033[1;33m]\033[1;37m "+link)
	print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - -")
	time.sleep(ti)
	login=requests.get("https://www.machine-liker.com/auth/verify-login/",headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36","cookie":home})
	if login.json()["status"]=="ok":
		os.system("clear")
		print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mMachine")
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
		print(color[jo]+"User:"+login.json()["user"]["name"])
		cookie=login.headers["Set-Cookie"].split(";")[0]
		while True:
			try:
				buff=requests.post("https://www.machine-liker.com/api/send-reactions/",headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36","cookie":cookie},data={"post_id":id,"reactions":r,"limit":"100"})
				if buff.json()["status"]=="ok":
					print("\033[1;33m[\033[1;37m"+login.json()["user"]["name"]+"\033[1;33m]\033[1;37m <> \033[33m[\033[1;32m+"+buff.json()["info"]["message"].split(" ")[0]+" Reactions\033[33m]\033[1;37m <> \033[33m[\033[1;96m"+id+"\033[33m]")
					print(" \033[1;37m➻\033[1;96m❥ \033[1;32mVui Lòng Đợi \033[1;33m10 Phút", end='\r')
					time.sleep(600)
				else:
					time.sleep(600)
			except:
				pass
os.system("clear")
print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mMachine")
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
user=input(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập User-Agent: \033[1;95m")
luong=int(input(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Số Luồng: \033[1;95m"))
ti=int(input(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Số Giây Để Login Tất Cả: \033[1;95m"))
print(" \033[1;37m➻\033[1;96m❥ \033[1;31mSau Khi Hết Thời Gian Tự Đăng Nhập Và Buff")
print(" \033[1;37m[\033[1;33m1\033[0m\033[1;37m] \033[1;37m➻\033[1;96m❥ \033[1;32mBuff Like")
print(" \033[1;37m[\033[1;33m2\033[0m\033[1;37m] \033[1;37m➻\033[1;96m❥ \033[1;32mBuff Love")
print(" \033[1;37m[\033[1;33m3\033[0m\033[1;37m] \033[1;37m➻\033[1;96m❥ \033[1;32mBuff Wow")
print(" \033[1;37m[\033[1;33m4\033[0m\033[1;37m] \033[1;37m➻\033[1;96m❥ \033[1;32mBuff Haha")
print(" \033[1;37m[\033[1;33m5\033[0m\033[1;37m] \033[1;37m➻\033[1;96m❥ \033[1;32mBuff Sad")
print(" \033[1;37m[\033[1;33m6\033[0m\033[1;37m] \033[1;37m➻\033[1;96m❥ \033[1;32mBuff Angry")
r=input(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập Cảm Xúc Muốn Buff: \033[1;95m")
id=input(" \033[1;37m➻\033[1;96m❥ \033[1;32mNhập ID_POST: \033[1;95m")
os.system("clear")
print("\033[1;37m      ██╗██╗███╗  ██╗ \033[1;96mTool: \033[1;37mMachine")
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
for i in range(luong):
	threading.Thread(target=hack,args=(r,id,ti)).start()