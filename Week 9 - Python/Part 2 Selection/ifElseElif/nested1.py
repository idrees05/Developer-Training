from time import sleep

"""
Nested selection/nesting is when a selection block(if/else) is placed within another selection 
block
"""

userAge = 17  # int(input("Enter your age: "))
ageLimit = 16
passCode = "dfe1w3dev"


"""if condition 1 is met:
    code block 1
    if nested condition 2 is met: 
    code block 2
    else: nested condition 2
     code block2
  else:
    code block1
"""

"""
# compare the value held in userAge against the value held in ageLimit
if userAge > ageLimit:
    # execute if the condition above is met
    print("You met the minimum age requirement")
    userCode = input("Enter code: ")

    if userCode == passCode:  # this block is nested inside the first if
        print(f"Your code {userCode} is valid. Access granted !")
    else:
        print("Your code wasn't valid")
        
elif userAge > ageLimit:
    print("You met the minimum age requirement")
else:
    print("You haven't met the minimum age requirement")

print("closing ")

# Exercise: Modify the code above to use else for both if condition



# Pub Policy 25 & Over
customerAge = int(input("What is your age?:"))

if customerAge>35:
    print("Accessed granted")
elif customerAge<=35 and customerAge>=18:
        customerID = bool(input("Do you have ID? \nType '1' for yes\n Type '0' for no:"))
        if customerID == True and customerAge>=25:
             print("ID checked and age verified")
        else:
             print("No ID or checked and not over 25")
else:
     print("No access, underage")

"""

#nested if else statements 


# +, -, / , *
print("Operations = +, -, /, *")
def calculate(userSelection, num1, *args):

    sleep(2)
    if userSelection == "+":
        #num1 = int(input("type your first value:"))
        for i in args:
            sleep(3)
            num2=int(i)
            answer = num1 + num2

            if answer%2 == 0:
                print (f"{answer} is an even number")
            else:
                print (f"{answer} is an odd number")
         

    elif userSelection == "-":
        num1 = int(input("type your first value:"))
        num2 = int(input("type your second value:"))
        answer = num1 - num2

        if answer%2 == 0:
            print(f"{answer} is an even number")
        else:
            print(f"{answer} is an odd number")
    elif userSelection == "/":
        num1 = int(input("type your first value:"))
        num2 = int(input("type your second value:"))
        answer = int(num1 / num2)

        if answer%2 == 0:
            print(f"{answer} is an even number")
        else:
            print(f"{answer} is an odd number")
    elif userSelection == "*":
        num1 = int(input("type your first value:"))
        num2 = int(input("type your second value:"))
        answer = num1 * num2

        if answer%2 == 0:
            print(f"{answer} is an even number")
        else:
            print(f"{answer} is an odd number")
    else:
        print("Error, that operation isn't an option")


calculate(input("Type the operation you wish to use:"), int(input("type your first value:")),2, 3,6,7, 89,1)
