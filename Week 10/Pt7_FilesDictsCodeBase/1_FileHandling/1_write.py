"""
Session objectives
●	Write to text files
●	Read data from a text file
●	Append to text files
●   Use context manager to handle resource usage
Key vocabulary
Data files, text files

"""
"Spend 3 minutes to read the comments in green"
# In order to read the data stored in a text file, you must open it first. ​

# Just like a book. You can’t read what is inside if you don’t open it first.​

# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files

"""
Key file-handling techniques are:Open, Read ,Close, Write
The text file must be saved in the same location as your Python file for the program to work. 
"""

"1_FileHandling_ReadWrite/myfile.txt","w"
# Syntax: varName = openMethod('pathToFileOrFolder/partToFileOrFolder/fileName.txt', 'w')
filePath1 = open('Software Bootcamp/Week 10/Pt7_FilesDictsCodeBase/1_FileHandling/file1.txt', 'r')  # folder/folder, fileName

# Method 1
# print(filePath1.read())

# Method 2
# readContents = filePath1.read()
# readContents = filePath1.readline()  # Only the first line of the file
# readContents = filePath1.readlines() # Prints out everything but as a list on one line "['Python Programming\n', 'Today is Monday\n', 'Tomorrow is Tuesday\n', 'some text\n', 'another']"
readContents = filePath1.readable()
print(readContents)

filePath1.close


# Software Bootcamp/Week 10/Pt7_FilesDictsCodeBase/1_FileHandling/file1.txt
"To Do: Refer to the example code above to create a file called yourName.txt and Write your name to the file" 
# If stuck refer to the example above
"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html




