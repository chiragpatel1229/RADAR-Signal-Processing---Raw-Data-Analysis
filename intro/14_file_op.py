#!/usr/bin/python

import os, sys

pwd=os.getcwd()         # get current path string
dirs=os.listdir(pwd)    # list file in path/dir

# # Open a file
# path="D:\\Python\\Uni_HWI\\!intro"



# This would print all the files and directories
for file in dirs:
   print(file)
   



# Open a file for writing a string
fo = open("file_str.txt", "w")
fo.write( "Writing a string into the file... \n")

# Close opend file
fo.close()


fo = open("file_dir.txt", "w")
print("Name of the file: ", fo.name)

fo.write(str(dirs))
# Close opend file
fo.close()


# Open a file

## Open a file
#fo = open("foo.txt", "wb")
#print "Name of the file: ", fo.name
#print "Closed or not : ", fo.closed
#print "Opening mode : ", fo.mode
#print "Softspace flag : ", fo.softspace



