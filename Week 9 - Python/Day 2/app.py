"""
cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition to use the "and" operator to check card value & suit to user's inputs
if chkCardValue == cardvalue and chkCardSuit == suitOfcards:
    print("Winner!")
else:
    print("Try Again")
"""

cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Use the "OR" and "NOT" operators to check if either the card value or suit does NOT match the user's input
if not (chkCardValue == cardvalue or chkCardSuit == suitOfcards):
    print("Try Again")
else:
    print("Winner!")