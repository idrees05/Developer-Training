cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value: ").title()
chkCardSuit = input("Enter card suit: ").title()

# Add the condition to use the "and" operator to check card value & suit to users inputs
if cardvalue == chkCardSuit and suitOfcards == chkCardSuit:
  # King == User Input      and   Hearts    == User Input  
    print("Winner!")
else:
    print("Try Again")

# Exercise modify the code above to use the OR & NOT logical operator





#if not(cardvalue == chkCardValue or suitOfcards == chkCardSuit)


#or = One condtion must be True
#and = Both condtions must be True

# Extension Exercise (may require some additional independent research!!):
# 1) Use if else to find item from a list
# 2) print the index value if the item is found
# 3) otherwise print a message "item not in list/not found"