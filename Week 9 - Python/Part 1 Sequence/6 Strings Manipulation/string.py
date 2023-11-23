s1="I am a python programmer" #string 

s2='I am a python programmer with single quote' # string

s3="""I am a python programmer with single quote I am a python programmer with 
single quote I am a python programmer with single quote"""


# print characters as per index position
print(s1[5], s1[7] , s1[12], s2[10] )

# return the length of the string
print(len(s1))

# slice the string
print(s1[5:12]) # start and end index postion
print(s1[5:]) # specify start index position and every character that follows
print(s1[5: -1])# use - with value to specify character from the end that should be omitted
print(s1[5: -12])

#Exercise print up to the 12th item as per index position

print(s1[:12]) #end index position, values 0-11 would be obtain, stop the slice at value 12

print(s1[5: -1])

print(s3[5:]) # specify start index position and every character that follows

print(s3[5:-15]) # specify start index position and every character that follows


s5="This is it, I am a python programmer" #string 
print("\n")
print(s5)
print(s5[-29:15]) # we write this 
print(s5[:15]) # python see this

# print specific characters within the start and end index position specified
print(s5[1:22:2]) # start index , end index and print every second character

# use find method to find /locate a substring within a given string
#s1="I am a python programmer" #string 
print(s1.find("a"))

s5 = " It is a beautiful day A wonder " 
#strip string of white spaces
print(s5)
print(s5.lstrip()) #strip before the sentence
print(s5.rstrip()) # strips after the sentence
print(s5.strip()) # strips before and after the sentence

# count a specific character
print(s5.count("a"))
# use upper, lower, and title function  to change the character to upper lower or title case
print("This is lower case: ",s5.lower())
print("This is UPPER case: ",s5.upper())

print("This is Title case: ",s5.title())
# replace substring within a string 
print(s5.replace("day", "Weather")) # use replace function to replace a subsstring
print(s5[1::3]) # without specifying the end index position [start::step]

# split strings
stringToSplit = "Welcome to Python"
print(stringToSplit)
subStrings = stringToSplit.split()
print(subStrings)

# use the split and join method
s4="How are you"
jointxt = "".join(s4.split())
print("line 71")
print(jointxt)

# replace a substring
print(s4.replace("How", "Where"))
print(s4)

# use Upper, lower and title
print(f"Upper case: {s4.upper()}")
print(f"Lower case: {s4.lower()}")
print(f"Title case: {s4.title()}")

#f-string (template literal in JS)
print(f"Hello, {s4}. You are {s1}.")
