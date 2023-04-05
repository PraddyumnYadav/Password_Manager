# Importing Essentials
from cryptography.fernet import Fernet


# Create our main Function
def main():
    # Getting the Master Password
    master_pwd = input("Enter the Master Password: ")

    # Loading the Key and passing it to Fernet
	key = load_key() + master_pwd.bytes
	fer = Fernet(key)

    # Printing the Mode Message
    msg = "Mode:\n    Add a new Password: add \n    View Existing Passwords: view \n    Press q to Quit."
    print(msg)

    # Getting the mode and do Operations
    while True:
        mode = input("Mode: ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid Input")
            continue


# Define more Functions
def view():
    sep = "------------------------------------------------------------------------------------------"
    print(sep)
    with open("passwords.txt") as f:
        f = f.read().split("\n")
        for password in f:
            if password == "":
                continue

            account, userName, pwd = password.split("|")

            print("Account Name: " + account)
            print("User Name: " + userName)
            print("Password: " + pwd)
            print(sep)


def add():
    name = input("Account Name: ")
    userName = input("User Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + userName + "|" + password + "\n")


"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Run Our main() function
main()
