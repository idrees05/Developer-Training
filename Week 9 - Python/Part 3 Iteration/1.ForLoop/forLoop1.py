from time import sleep

"""
use a for loop when the number of iteration is known(how many times you want/going 
to do something for). A for loop also controls the flow of execution in a program
"""

# Iteration means to repeat in programming

# what characters can you find in the variable called name below
name = "Tim" # string ,list (list, tuple), range
for letter in name: # letter = selecting based on index value, which starts at 0
    print(letter) 
#T
#i
#m

# i = index (zero-based)
array = (0,1,2,3,4,5)
for i in array: # name could be replace with list or range
    print(i)


for i in range(1,7):
    print(i)

#NAME   TUPLE   RANGE    
#T      0       1
#i      1       2
#m      2       3
#       3       4
#       4       5
#       5       6





"syntax "
# for variablename in range method(numberofIteration)

numbers= [1,2,3,4,5,6,7,8] #How do I access the values in this list?
#         0,1,2,3,4,5,6,7 # by using the index value it's associated with

for number in numbers:
    print(number) # number in this example would give us the Index value

    # How would I access the data instead of the index?
   





for findNumber in range(10):  # we specify the number of iterations
    print(findNumber) # 0 - 9


print("Two values")
"Modify the code to pass in a second value in the braces as a parameters and comment your code to explain it"
# range(start number, stop number)


for findNumber in range(1, 11):
    print(findNumber)
# 1,2,3,4,5,6,7,8,9,10


print("Three values")
"""Modify the code to pass two more values in the braces as a parameters but the second value must 
be a bigger number than the first and third values and comment your code to explain it"""
#range(start number, stop number, step)
for findNumber in range(1,6,2):
    print(findNumber) #1,3,5
    # 1,3,5

for findNumber in range(0,11,5):
    print(findNumber) 
    # 0,5,10

"Modify the code above to countdown"
print("count down")














for findNumber in range(5, -1, -1):
    print(findNumber)
#5,4,3,2,1,0