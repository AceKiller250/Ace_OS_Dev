#Error Tracker
#TODO: Add error tracker when program is finished
#import sentry_sdk
#sentry_sdk.init(
#    dsn="https://5082b3d9abac4d8db434b1da5b7bc811@o1362474.ingest.sentry.io/6653986",
#
#    # Set traces_sample_rate to 1.0 to capture 100%
#    # of transactions for performance monitoring.
#    # We recommend adjusting this value in production.
#    traces_sample_rate=1.0
#)


#Import requirements
from logging import exception
from turtle import clear
from urllib.error import HTTPError
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
import socket
import webbrowser
from time import sleep
import smtplib
import socket
import json
import requests
import subprocess




#Setup system settings and config
if platform == "linux" or platform == "linux2":
    #linux
    gameExtension = None
    print("Sorry, linux is currently not supported. Please check back at a later date or go to the github to get current status on linux version.")
    sleep(2)
    input("Press any key to continue...")
    sys.exit()
elif platform == "darwin":
    # OS X
    gameExtension = ".dmg"
elif platform == "win32":
    # Windows
    gameExtension = ".exe"



#Define clear console
def consoleClr():
    if platform == "linux" or platform == "linux2":
        #linux
        os.system("clear")
    elif platform == "darwin":
        # OS X
        os.system("clear")
    elif platform == "win32":
        # Windows...
        os.system("cls")


#Checks for any incompatiblity issues within the program (i.e. OS, bugs, etc...)
if platform == "darwin":
    print("MacOS is not fully supported. You can still login, signup, and reset your password but booting games does not work atm. Please check back at a later date or go to the github to check the status of MacOS")
    sleep(5)
    print("Would you like to continue?[y/n]")
    macPauseAns = input("> ")
    if macPauseAns == "y" or macPauseAns == "Y":
        print("Continuing...")
        consoleClr()
    elif macPauseAns == "n" or macPauseAns == "N":
        sys.exit()



#File location and locater
pathname = os.path.dirname(sys.argv[0])
if os.path.exists(pathname + "/games"):
    ##Move on
    print("Loading game directory...")
    sleep(1)
    print("File location loaded successfully.")
else:
    gamespath = os.path.join(pathname, "games")
    print(gamespath)
    os.makedirs(gamespath)


#Configure and Connect to Firebase

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

#storage = firebase.storage()
# as admin
#
#storage.child("games/test.json").download("settings.json")

#Sets up error handler 
class error(Exception):
    pass

class EmailExists(error):
    pass


#Define Proggresbar
import progressbar

def creating_account():
        for i in tqdm(range(100),
                  desc="Creating Account...",
                  ascii=False, ncols=75):
            time.sleep(0.01)

def spinny_marker(text, delay):
    widgets = [text + ":", progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(delay):
        time.sleep(0.1)
        bar.update(i)

def loading_bar(text, load_delay):
        for i in tqdm(range(load_delay),
                  desc= text + "...",
                  ascii=False, ncols=75):
            time.sleep(0.01)






#setup download function



#from downloader import downloadLink
#downloadLink("https://speed.hetzner.de/1GB.bin")





#TODO: 2/3 done. Change link to perma hosting and fix new download check

from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://firebasestorage.googleapis.com/v0/b/ace-os-auth.appspot.com/o/settings.json?alt=media&token=5287407f-f879-4680-964d-4932b34df67a"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
print(data_json)

#Main
foldername = os.path.abspath(pathname)




spinny_marker("Checking Version", 20)

print(data_json.get("version"))

currentVersion = data_json.get("current_version")

data_json.close()





#Get version from json file

f = open(foldername + "/settings.json")

data = json.load(f)

print(data.get("version"))

#Get CurrentVersion from aceprints.co/version.json

LocalVersion = data.get("version")

f.close()

#Check if CurrentVersion is less than ACEversion



if currentVersion >= LocalVersion:
    print("Version is up to date")
else:
    print("Version is not up to date")
    time.sleep(2)
    print("Attempting to Update...")
    os.system("")
    #TODO Check for newer version on website and download using downloader.py
    #url = requests.get("https://jsonplaceholder.typicode.com/users")
    #text = url.text
    #print(type(text))
    #sys.exit()





    






def checkforFile(filename, folder):
    for root, dirs, files in os.walk(pathname+"/"+folder, topdown=True):
        for name in files:
            print(os.path.join(root, name))
            if name == filename:
                return True
        for name in dirs:
            print(os.path.join(root, name))
    return False







#Animated Marker
def animated_marker():
    widgets = ['Sending Reset email: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(10):
        time.sleep(0.1)
        bar.update(i)












#Temportary Launcher

def LauncherRun():
    import socket
    import webbrowser
    import os
    import time
    from time import sleep
    import sys
    import smtplib
    import subprocess
    import socket
    pathname = os.path.dirname(sys.argv[0])



    foldername = os.path.abspath(pathname)

    def mindustryserverrun():    
        mindustryserverpath = str(foldername + r"\mindustry" + r"\server" r"\run_server.bat")
        mindustryserverpath2 = str(foldername + r"\mindustry" + r"\server")
        os.startfile(mindustryserverpath)
        print("I can only do so much for you :( So your going to have to do a few steps on your own to start the server. Please press windows key + r " +
        "and in the new bar copy and paste " + mindustryserverpath2 + "in the new box. After that click run_server (Either one).")    




    def mindustry():
        mindustrypath = str(foldername + r"\mindustry" + r"\Mindustry.exe")
        os.startfile(mindustrypath)


    def mindustrysurvey():
        print("Would you like to start a multiplayer server aswell?[y/n]")
        survey = input("> ")
        if survey == "Y" or survey == "y":
            mindustryserverrun()
            mindustry()
        elif survey == "N" or survey == "n":
            mindustry()



    #print('\n')
    #print(foldername)
    #print('\n')
    #print(pathname)
    #print('\n')
    #print(foldername + "\calcv3.py")
    #print('\n')


    while True:


        userchoice = ("")
        print("Calculator | Snake Game | Dino Game | Aeroblaster | Flappy Bird | Chess | Mindustry | Gladihoppers | Control Room")


        while True:
                while True:
                    userchoice = str(input("Choose an option from the list above: "))
                    if userchoice in ('Calculator', 'Snake Game', 'Dino Game', 'Calc','Dino', 'Snake', 'Flappy Bird', 'Shadow Tower', 'Aeroblaster', "Chess", "Mindustry", "Gladihoppers", "Control Room", "CR", "cr"):
                        break
                    print("Not a program. (Please make sure it is spelled exactly as stated including caps).")
                if userchoice == "Calculator" or userchoice == "Calc":
                    print("Booting Calculator...")
                    os.system(foldername + "\calcv3.exe")
                    sleep(2)

                elif userchoice == "Snake Game" or userchoice == "Snake":
                    print("Not avalible yet. Sorry! :(")

                elif userchoice == "Dino Game" or userchoice == "Dino":
                    from dino_main import dinostart
                    print("Booting Dino game...")
                    dino = (foldername + "\main.exe")
                    os.startfile(dino)

                elif userchoice == "Aeroblaster" or userchoice == "aeroblaster":
                    print("Booting Aeroblaster...")
                    Aeroblaster = str(foldername + r"\aeroblaster" + r"\Aeroblaster.exe")
                    os.startfile(Aeroblaster)
                elif userchoice == "Flappy Bird":
                    print("Booting Flappy Bird...")
                    flappypath = str(foldername + r"\flappy_bird" + r"\flappy_update.exe")
                    os.startfile(flappypath)
                elif userchoice == "Chess" or userchoice == "chess":
                    print("Booting Chess...")
                    chesspath = str(foldername + r"\chess" + r"\chess.exe")
                    os.startfile(chesspath)
                elif userchoice == "Shadow Tower" or userchoice == "Shadow":
                    print("Booting Shadow Tower")
                    shadowpath = str(foldername + r"\shadow_tower" + r"\Shadow_tower.exe")
                    os.startfile(shadowpath)
                elif userchoice == "Mindustry" or userchoice == "mindustry":
                    mindustrysurvey()
                elif userchoice == "Control room" or userchoice == "Control Room" or userchoice == "control room" or userchoice == "CR" or userchoice == "cr":
                    controlroompath = str(foldername + r"\controlroom" + r"\ControlRoom_v1.62.exe")
                    os.startfile(controlroompath)
                elif userchoice == "Gladihoppers" or userchoice == "gladihoppers":
                    gladihopperpath = str(foldername + r"\gladihoppers\Gladihoppers_Win_v_2_2_0\Gladihoppers.exe")
                    os.startfile(gladihopperpath)

                # Left over trash code
                #elif userchoice == "Shadow":
                #    print("Booting Shadow Tower...")
                #    os.system(foldername + "\shadow_tower" + "\Shadow_Tower.py")
                #    break




    # flappypath = str(foldername + "\flappy_bird" + "\flappy_update.py")



# s.systems.path.dirname(sys.argv[0]) + '\calcv3.py




















#Reset Password
def resetpass():
    print("Reseting Password...")
    print("Please Enter your Email Below: ")
    email = input("> ")
    animated_marker()
    auth.send_password_reset_email(email)
    print("Success! If there was an Account associated with this email it will be sent a reset link. Check your inbox.")
    sleep(3)
    consoleClr()
    menu()


def is_any_user_email_verified(accountinfo):
    return any(u for u in accountinfo['users'] if u['emailVerified'])


#Login function

def login():
    consoleClr()
    while True:
        print("Login:")
        email=input("Enter email: ")
        password=input("Enter password: ")
        consoleClr()
        #Sign in
        try:
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
            LauncherRun()

            #Old launch file

            #chooseosstart = (pathname + "/choose.py")
            #opener = "open" if sys.platform == "darwin" else "xdg-open"
            #subprocess.call([opener, chooseosstart])
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "INVALID_EMAIL":
                print("Account/Email does not exist. Please check your email address below or create another account.")
                sleep(1)
                print("Entered email: \n \n" + email + "\n")
                sleep(1)
                print("Would you like to create a new account?[y/n]")
                answer = input("> ")
                if answer == "yes" or answer == "y":
                    resetpass()
                elif answer == "n" or answer == "no":
                    consoleClr()
                continue
                signup()
            elif error == "INVALID_PASSWORD":
                print("Password is invalid.")

                print("Would you like to reset your passowrd?[y/n]")
                answer = input("> ")
                if answer == "yes" or answer == "y":
                    resetpass()
                elif answer == "n" or answer == "no":
                    consoleClr()
                continue
        return
#        except:
#            
#            print("Invalid email or password")
#            print("Would you like to reset your passowrd?[y/n]")
#            answer = input("> ")
#            if answer == "yes" or answer == "y":
#                resetpass()
#            elif answer == "n" or answer == "no":
#                consoleClr()
#            continue
#        return
#
#

#INVALID_EMAIL
#INVALID_PASSWORD


#Signup Function
def signup():
    consoleClr()
    while True:
        print("Signup:")
        email = input("Enter email: ")
        password=input("Enter password: ")
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user = auth.refresh(user['refreshToken'])
            auth.send_email_verification(user['idToken'])
            print("Account created! Please verify it with the email sent.")
            sleep(5)
            ask=input(f"Do you want to login?[y/n] \n")
            if ask=='y':
                login()
            else:
                menu()
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "EMAIL_EXISTS":
                print(f"An account with the email of {email} already exists. Please login or use a different email.")
                sleep(3)
                print("Would you like to log in?[y/n]")
                retunValue = input("> ")
                if retunValue == 'y':
                    login()
                else:
                    login()
                signup()
            elif error == "WEAK_PASSWORD":
                print(f"{password} is too weak of a password. Please create a stronger password.")
        print("If you are getting this message an error has occurred, please try again and if this persists then please contact AceKiller250 or a dev")
        return





#Menu

def menu():
    while True:
        print("Please Choose an option from the list below")
        print("Login | Signup | Reset Password")

        ans = input("> ")

        if ans == 'Login' or ans == 'login' or ans == "l":
            consoleClr()
            login()
            break
        elif ans == 'Signup' or ans == 'signup' or ans == "s":
            consoleClr()
            signup()
            break
        elif ans == 'Reset Password' or ans == 'Reset' or ans == 'r':
            consoleClr()
            resetpass()
            continue





#Main
while True:
    print("Please Choose an option from the list below")
    print("Login | Signup | Reset Password")

    ans = input("> ")

    if ans == 'Login' or ans == 'login' or ans == "l":
        consoleClr()
        login()
        break
    elif ans == 'Signup' or ans == 'signup' or ans == "s":
        consoleClr()
        signup()
        break
    elif ans == 'Reset Password' or ans == 'Reset' or ans == 'r':
        consoleClr()
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
#            consoleClr()
#        continue
#    return


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


#TODO: Game launcher

