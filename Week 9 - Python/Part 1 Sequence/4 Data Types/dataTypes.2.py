#List is an ordered sequence of items. It is a very flexible data type in python
# The values in a list doesn't have to be of the same type
# items in a list can be modified
# declare a list1 variable and assign values of different datatypes in the list
# items can be accessed based on their index position
list1 = [1,5,9.9, 5, "list", "list", False] 
list2 = [1,3,4,5,10,20] 
print("\nThis is a List")
print(type(list1))
print(list1)
print(type(list2))
print(list2)
# 0 1 2 3 4 5 6



# Tuple is a sequence of items that are in order
# and it is not possible to modify the tuples. Therefore,
# tuples are faster than list and the primary use of tuples 
# is to create, write and protect data
# items can be accessed based on their index position

# declare a tuple1 variable and assign values of different datatpes in the tuple
tuple1 = (6, -4, "Tuple", -4, 3.2, "Tuple")
print("\nThis is a Tuple")
print(type(tuple1))
print(tuple1)


#Set is a  collection of unique items that are not in order, 
# it is an unordered datatype. Duplicates are eliminated in a set
# Set items cannot be accessed based on their index position

# declare a set1 variable and assign values of different datatpes in the set
set1 = {4,5,5,5,5,5,5, 10, "xyz", 1.3, 5, "xyz", True, True, False} # 1.3, 4, 5, 10, "xyz"
print("\nThis is a Set")
print(type(set1))
print(set1) # 4, 5, 10.5, xyz, 1.3

#expected output
# duplicate items will be printed only once
# items in the list will be displayed in no particular order

# Dictionary stores data as key value pairs 
# to retrieve a specific value from a dictionary you need to know the key

dictionary1 = {1:"John", 2:"Anna", 3:"Peter"}
dictionary2 = {"age":23, "homeOwner":True}

print("\nThis is a Dictionary")
print(type(dictionary1))
print(dictionary1)

print("printing values from lists, tuples & dictionaries")
print("Dictionary:")
print(dictionary1[2])
print(dictionary2["homeOwner"])
print("List:")
print(list1[2])
print("Tuple:")
print(tuple1[3])


