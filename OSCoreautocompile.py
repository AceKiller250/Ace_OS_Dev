import os
import sys
import subprocess
import time
from sys import platform
import requests
import io
from mediafire import MediaFireApi
import json
from mega import Mega

mega = Mega()






pathname = os.path.dirname(sys.argv[0])


pyinstaller = str("pyinstaller --onefile ")




if platform == "darwin":
    # OS X
    builtOS = pathname + "/login.pkg"
elif platform == "win32":
    # Windows...
    builtOS = pathname + "/login.exe"



def PublishOS():
    #Get version from version.json
    f = open(pathname + "/version.json")
    data = json.load(f)
    print(data.get("version"))
    version = data.get(("version"))
    print("Version: " + version)
    print("Updating to new version...")
    data.parse("version", version)
PublishOS()
print("Are you sure your ready to compile?[y/n]")
ans = input("> ")
if ans == "Y" or ans == "y":
    os.system(pyinstaller + "login.py")
    ans = input("Do you want to compile the server?[y/n]")
    if ans == "Y" or ans == "y":
       PublishOS()
else:
    print("Alright have fun coding")
    sys.exit()







