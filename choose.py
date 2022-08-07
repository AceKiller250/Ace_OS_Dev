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