""" Python Password Check """
import hashlib
import sys

password = "2034f6e32958647fdff75d265b455ebf"

def main():
    # Code goes here
    print("Doing some stuff")
    sys.exit(0)


while True:
    userinput = input("Enter password: ")
    if userinput == password:
        print("welcome to the program")
        main()
    else:
        print("Wrong Password")