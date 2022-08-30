import os
import sys
from time import sleep
print("Entering Root...")
print("Please enter password for this PC User: ")
pathname = os.path.dirname(sys.argv[0]) + "/mac_spoof_loop.py"


os.system("spoof-mac list --wifi")
sleep(2)
while True:
    os.system("sudo spoof-mac randomize wi-fi")
    sleep(5)