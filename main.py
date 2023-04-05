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
            pass
        elif mode == "add":
            pass
        else:
            print("Invalid Input")
            continue


# Run Our main() function
main()
