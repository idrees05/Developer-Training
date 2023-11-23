"""use a while loop when the number of iterations is unknown
(dont know how many times you want/going to do something for)
A while loop also controls the flow of execution in a program"""

"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to"""

# While loop keeps looping/iterating until a condition is met
"Run this loop and explain what it is doing "
userGuess = input("Enter guess word: ")
guessWord = "gcma5dev"

while userGuess != guessWord:
    if userGuess == "please":
        break
    userGuess = input("Guess again!: ")
    
print(f"You guessed {userGuess} correctly")
