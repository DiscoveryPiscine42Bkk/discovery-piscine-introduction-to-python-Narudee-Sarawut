number = int(input("Enter a number: "))
if number > 25:
    print("Error\n")
else:
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1
