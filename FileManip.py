
# CHECK WHETHER A FILE EXISTS AND WHAT IS IT'S LOCATION AND TYPE:

'''

import os

path = "C:\\Users\\dell\\Desktop\\DESIGNING\\S.DOC"

if os.path.exists(path):
    print("The location exists!", end = " ")
    if os.path.isfile(path):
        print("and this is a file")
    elif os.path.isdir(path):
        print("and this is a folder")
else:
    print("The location does not exsist!")

'''

# READ A FILE:

'''

By using 'with open()' keywords the file will close automatically.

try:
  with open("C:\\Users\\dell\\Desktop\\DESIGNING\\S.DOC") as file:
    print(file.read())

except PermissionError:
  print("You don't have the permission to excess the file.")

except FileNotFoundError: 
  print("File not found :(")

'''

# WRITE A FILE:

'''

with open("test.txt", 'w') as file:
    file.write("")

Keyword 'w' is used to write some stuff in the file.
keyword 'a' is used to append(Add more stuff) in the file.
Use '\n' to write the code in new line.

Also the file 'test.txt' was deleted    

'''

# COPY A FILE:

'''

copyfile('src','dst') : Copies data from one file to another file.
copy('src','dst') : Copies data from one file to another file into a folder or directory.
copy2('src','dst') : Copies data from one file to another file into a folder or directory and can also give it creation time and date.

Example: 

import shutil
shutil.copyfile('text.txt','copy.txt')

In other words, it is used to copy data from source to destination in the most efficient way possible.
Both text.txt and copy.txt were deleted.

'''

# MOVE A FILE:

'''

You need to edit the destination after the name of the device, like adding the folder and the name of the file
you want to move.

import os

source = "test.txt"
destination = "C:\\Users\\dell\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("This file already exsists!")
    elif os.replace(source,destination):
        print("The file is successfully moved!")

except FileNotFoundError:
    print("Sorry", end = " " +source+ " does not exsist")

test.txt was deleted    

'''

# DELETE A FILE:

'''

import os

try:
    os.remove('test.txt')

except FileNotFoundError:
    print("File not found")

'''

# DELETE AN EMPTY FOLDER:

'''

import os

If we try 'os.remove' keyword, the compiler will give us PermissionError.

try:
    os.rmdir('niga')

except FileNotFoundError:
    print("Folder not found")

except PermissionError:
    print("You don't have the permission to delete this folder")

else:
    print("The folder was deleted")

'''

# DELETE A FOLDER CONTAINING FILES:

'''

import shutil

try:
    shutil.rmtree('fol')

except FileNotFoundError:
    print("Folder not found")

except PermissionError:
    print("You don't have the permission to delete this folder")

else:
    print("The folder was deleted")
    
'''