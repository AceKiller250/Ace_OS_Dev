import os
from sys import platform
import time
import progressbar

def animated_marker():
    widgets = ['Sending Reset email: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(10):
        time.sleep(0.1)
        bar.update(i)



print("Made by AceKiller250")
if platform == "linux" or platform == "linux2":
    #linux
    NewAddress = os.system("openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'")
    print("New MAC address is " + NewAddress)

elif platform == "darwin":
    # OS X
    os.system("clear")
elif platform == "win32":
    # Windows...
    os.system("cls")