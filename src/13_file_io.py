"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# assign a variable to the file and open it with r to 
# read only
text_file = open("foo.txt", "r")

# print the file contents with the read method
print(text_file.read())

#always close the file so there is no unused memory
text_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open("bar.txt", "w+")

for i in range(3):
    f.write(f"this is a line {i+1}\n")

f.close()