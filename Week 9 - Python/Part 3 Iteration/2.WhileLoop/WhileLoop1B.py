# While loop keeps looping/iterating until a condition is met
"Run this loop and explain what it is doing "
userGuess = input("Enter guess word: ")  # first attempt at guessing the guess word
guessWord = "gcma5dev"
guessAttempts = 1  # flag variable = 1

# first attemmpt + two more attempts
while userGuess != guessWord and guessAttempts < 3:
    userGuess = input(f"Try again!: You have guessed {guessAttempts} / 3 attempts\n: ")
    guessAttempts += 1  # guessAttempts = guessAttempts + 1
    

if userGuess == guessWord:
    print(f"You guessed {userGuess} correctly")
else:
    print(f"You have guessed {guessAttempts} / 3 attempts")
