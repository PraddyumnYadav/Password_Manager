# Create our main Function
def main():
    # Getting the Master Password
    pwd = input("Enter the Master Password: ")

    # Printing the Mode Message
    print(
        """
		Mode: 
			Add a new Password: add
			View Existing Passwords: view
			Press q to Quit.
		"""
    )

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
    pass


# Run Our main() function
main()
