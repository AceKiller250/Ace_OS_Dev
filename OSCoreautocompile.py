import os
import sys
import subprocess
import time




pathname = os.path.dirname(sys.argv[0])

pyinstaller = str("pyinstaller --onefile ")



def choosecompile():
    subprocess.call(pyinstaller + "choose.py")
def logincompile():
    subprocess.call(pyinstaller + "login.py")
def calccompile():
    subprocess.call(pyinstaller + "calcv3.py")


print("Are you sure your ready to compile?[y/n]")
ans = input("> ")
if ans == "Y" or ans == "y":
    choosecompile()
    calccompile()
else:
    print("Alright have fun coding")
    sys.exit()


#with Progress() as progress:
#
#    task1 = progress.add_task("[red]Compiling choose script...", total=1000)
#    task2 = progress.add_task("[green]Compiling login script...", total=1000)
#    task3 = progress.add_task("[cyan]Compiling calc script...", total=1000)
#
#    while not progress.finished:
#        progress.update(task1, choosecompile())
#        progress.update(task2, logincompile())
#        progress.update(task3, calccompile())
#        time.sleep(0.02)





