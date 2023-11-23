pStudy = input("Enter a program of study: ").title()  
# use title to convert the first letter to upper case
curProgram = "Bootcamp"

"""if condition is met:
    code block 1
   else:
     code block 2   
"""
# compare values held in pStudy and curProgram for a match
if pStudy == curProgram:
    # code block will be executed if here is a match when the comparison is performed
    print(f"welcome to {pStudy}")
else:  # executes the code block below if there is no match
    print(f"No course for {pStudy}, please enquire within")

# Exercise: Using if and else
# Create a program that finds the minimum value between two numbers 
# using if else





num1 = int(input("Enter your first value: "))
num2 = int(input("Enter your second value: "))

if num1>num2:
    print(f"{num2} is the lowest value")
else:
    print(f"{num1} is the lowest value")
