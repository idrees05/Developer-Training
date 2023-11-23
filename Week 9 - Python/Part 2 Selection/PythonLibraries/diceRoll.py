from random import randint

dice1 = randint(1, 6)
dice2 = 6  # randint(1, 6)


print(f"Dice 1: {dice1} | Dice 2: {dice2}")

dice = dice1 + dice2  # adding the values of both dice

if dice == 12:  # check if the total of both dice is 12
    dice = dice * 2  # double the total from both dice
    print(f"You threw {dice}")
else:
    if dice1 == dice2:
        dice = dice  # 10 = 10
        print(f"You threw {dice}")
# diceThrow = dice
# print(f"You threw a total {diceThrow}")
print(f"You threw a total {dice}")


# a message that you threw a double if both number on the two dice are a match
# multiply the total value of both dice by 2 if the total is 12
