# LOOPS: 

# FOR LOOPS: 

'''

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as 
found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
Square brackets are used to define the index within a loop.

'''

# Print each fruit in list:

'''

Example:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

'''

# Use of "break" and "continue" commands:

'''

Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
    
Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''

# Range parameter:

'''

Example:

for x in range(6):
  print(x)

Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value 
by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment 
value by adding a third parameter: range(2, 30, 3):


Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

'''

# Max value finder:

'''

def max(n1, n2):
    if n1>n2:
        print("NUMBER 1 IS GREATER THAN NUMBER 2")
    else:
        print("NUMBER 2 IS GREATER THAN NUMBER 1")

x = input("ENTER THE VALUE OF X: ")
y = input("ENTER THE VALUE OF Y: ")

max(x,y)

'''

# Min value finder:

'''

def min(n1, n2):
    if n1<n2:
        print("NUMBER 1 IS LESS THAN NUMBER 2")
    else:
        print("NUMBER 2 IS LESS THAN NUMBER 1")

x = input("ENTER THE VALUE OF X: ")
y = input("ENTER THE VALUE OF Y: ")

min(x,y)

'''

# WHILE LOOPS:

'''

With the while loop we can execute a set of statements as long as a condition is true. 

The while loop requires relevant variables to be ready. In this example we need to define an indexing variable, 
i, which we set to 1.

Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

remember to increment i, or else the loop will continue forever.

'''

# Use of "break" and "continue" commands:

'''

Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

'''