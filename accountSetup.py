import json
import time

#Creates a Username
def userNameCreation():
    global userName
    userName = input("Please Enter A Valid Username: ")
    if type(userName) != str:
        print("The Username You Have Choosen Is Invalid.")
        time.sleep(0.1)
        print("Please Try Again")
        time.sleep(0.1)
        userNameCreation()
    else:
        print(f"Your Username is now: {userName}")

#Creates a Password
def passwordCreation():
    global password
    password = input("Please Enter A Valid Password: ")
    if type(password) != str:
        print("The Password You Have Choosen Is Invalid")
        time.sleep(0.1)
        print("Please Try Again")
        time.sleep(0.1)
        passwordCreation()
    else:
        passwordLen = int(len(password))
        passwordDisplay = ""
        for x in range(passwordLen):
            passwordDisplay = passwordDisplay + "*"
        print(f"Your password is now: {passwordDisplay}")

#Stores Username and Password in characters.json
def loginStorage():
    print("Storing Username and Password In Local Database")

def accountCreation():
    print("Welcome to ---- Text Based RPG")
    time.sleep(0.15)
    print("This is for creating a new Account!")
    time.sleep(0.15)

    userNameCreation()
    passwordCreation()

    loginStorage()