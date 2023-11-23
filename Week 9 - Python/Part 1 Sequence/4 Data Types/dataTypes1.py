# Data types are nothing but variables you use to reserve some space in memory.
# Python variables do not need an explicit declaration to reserve memory space. 
# The declaration happens automatically when you assign a value to a variable.


# String data types
# String are identified as a contiguous set of characters represented in 
# the quotation marks. Python allows for either  pairs of single or double
#  quotes. Strings are immutable sequence data type, i.e each time one makes 
# any changes to a string, completely new string object is created.

# use "" for single line string value assigment 
s1 = "I love python, with double qu0tes!" 
# use '' for single line string value assigment 
s2 = 'Python is the in demand programming language, with single quote'
# use """""" for multi line string value assigment 
s3 = """
This is multiline, 
This is multiline, 
This is multiline, 
This is multiline 
"""

s4 = "a"

# ~string comments
"This is a comment"

"""
This is a multiline comment 
This is a multiline comment 
This is a multiline comment 
"""

# Boolean data types
# Boolean is yes/no or true or false (0 = off and 1 = on)
bVal1 = True # declare and assign a boolean type variable with value True
bVal2 = False # declare and assign a boolean type variable with value False


# Numeric data types
num1 = 20.5 # float(decimal) variable declaration and assigment 
num2 = 20 # integer variable declaration and assigment
num3 = 1j # complex

# type() function is used to know the class of a value or variable.
print(type(bVal1)) # bool
print(type(bVal2))

print(type(s1)) # str
print(type(s2))
print(type(s3))
print(s3)

print(type(num1)) #float
print(type(num2)) #int