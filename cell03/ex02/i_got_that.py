while True:
    user_input = input("Enter something (type STOP to end): ")
    if user_input == "STOP":
        print("Program stopped.")
        break
    else:
        print(f"You entered: {user_input}")
