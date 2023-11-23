score = int(input("Enter your score: "))

"""
if condition 1 is met:
    code block 1    
elif condition 2 is met: # else if
    code block 2
elif condition 3 is met:
    code block 3
else:
    code block ...n   
"""

if score >= 75:  # check if score is greater than equal to
    grade = "A"  # create a variable and assign it a value 'A'

elif score >= 60: #else if (JS) ---- elif(Python)
    grade = "B"  # re-assign the value held in grade variable to 'B'

elif score >= 50:
    grade = "C"  # re-assign the value held in grade variable to 'C'

else:
    grade = "F"  # re-assign the value held in grade variable to 'F'

print(f"You scored {score} and your grade is: {grade}")

# What do you think is the equivalent of JS else if in python?

# Exercise: Using if Elif and else
# Create a Menu program that allows user to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice






# Solution
# Exercise: Using if Elif and else
# Create a Menu program that allow user to select between three subject choices
print("Subject Menu\n1. Music\n2. History\n3. Software Development \n4. Exit")

choice = input("\nPlease enter your choice: ")
# elif == ELse IF

if choice == "1":
    print("Sing me a song....")
elif choice == "2":
    print("When you know your history, you know your greatness")
elif choice == "3":
    print("Happy coding....0101010101010101010")
else:
    print("Goodbye")

input("\nPress Enter to exit ")
