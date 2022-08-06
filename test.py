from sys import platform
import os
print(platform)
if platform == "linux" or platform == "linux2":
    # linux
    os.system("clear")
elif platform == "darwin":
    # OS X
    os.system("clear")
elif platform == "win32":
    # Windows...
    os.system("cls")
