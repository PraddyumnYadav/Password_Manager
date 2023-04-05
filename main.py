# Create our main Function
def main():
    # Getting the Master Password
    pwd = input("Enter the Master Password: ")

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

            account = password.split("|")[0]
            userName = password.split("|")[1]
            pwd = password.split("|")[2]

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


# Run Our main() function
main()
