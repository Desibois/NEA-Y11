import random


def login(usertocheck, passtocheck):
    access = False
    f = open("User+Pass", "r+")
    user = f.readline.strip()
    key = f.readline.strip()
    while user != "done":
        if usertocheck == user and passtocheck == key:
            print("Welcome " + user + "You have been authorised to play.")
            access = True
            break
        elif usertocheck == user and passtocheck != key:
            print("Wrong password")
            user = f.readline.strip()
            key = f.readline.strip()
        elif usertocheck != user and passtocheck == key:
            print("Wrong username")
            user = f.readline.strip()
            key = f.readline.strip()
        else:
            print("Wrong login credentials")
            user = f.readline.strip()
            key = f.readline.strip()
    return access


def roll():
    dice = random.randint(1, 6)
    return dice


username = input("Username: ")
password = input("Password: ")
login(username, password)


