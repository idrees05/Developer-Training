# Exercise: Using if and else
# Create a program that find the minimum value between two numbers using if else
num1 = 10  # int(input("Enter first number: "))
num2 = 20  # int(input("Enter second number: "))
if num1 < num2:
    minimum = num1
else:
    minimum = num2
print("minimum number =", minimum)

userAge = 21  # int(input("Enter your age: "))
ageLimit = 16
passCode = "gcma4dev"
# Exercise: Modify the code above to use else for both if condition
if (
    userAge > ageLimit
):  # compare the value held in userAge against the value held in ageLimit
    print(
        "You met the minimum age requirement"
    )  # execute if the condition above is met
    userCode = "gcma4dev"  # input("Enter code: ")
    if userCode == passCode:  # this block is nested inside the first if
        print(f"Your code {userCode} is valid. Access granted !")
    else:
        print(f"Your code {userCode} is invalid. Access Denied !")

else:
    print(f"You are {userAge} years old and below the age limit!")

# Exercise: Using if Elif and else
# Create a Menu program that allow user to select between three subject choices
print("Subject Menu\n1. Music\n2. History\n3. Software Developer\n4. Exit")

choice = input("\nPlease enter your choice: ")

if choice == "1":
    print("Sing me a song....")
elif choice == "2":
    print("When you know your history, you know your greatness")
elif choice == "3":
    print("Happy coding....0101010101010101010")
else:
    print("Goodbye")

input("\nPress Enter to exit ")

# Exercise:
# Use if else to find item from a list
numList = [56, 78, 100, 45, 88, 71]

if 100 in numList:
    print("100 is at position ", numList.index(100))
else:
    print("100 not in list")


input("\nPress Enter to exit ")
