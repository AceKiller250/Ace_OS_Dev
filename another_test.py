import os, sys, subprocess
from subprocess import DEVNULL, STDOUT, check_call
systeminfo = subprocess.call(["ls", "-l"], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
print(systeminfo)