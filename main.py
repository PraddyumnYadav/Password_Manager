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
    pass


def add():
    name = input("Accound Name: ")
    userName = input("User Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + userName + "|" + password)


# Run Our main() function
main()
