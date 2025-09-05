# STRINGS:

'''

Strings in python are surrounded by either single quotation marks, or double quotation marks, 'hello' is the same as "hello".
You can display a string literal with the print() function.

When there is no value for a string, it will be assigned value 'None'. Here 'None' serves as a placeholder which signifies a variable
currently holds no data but will be assigned a value later based on functions return, calculation or user input. It is important to
initialize this value because python compiles code line by line.

'''

# Slicing String:

'''

b = "Hello, World!"
print(b[2:5])

Slice from start:

b = "Hello, World!"
print(b[:5])

Slice from end:

b = "Hello, World!"
print(b[2:])

'''

# STRING MODIFICATION:

# Python has a set of built-in methods that you can use on strings.

# Upper Case:

'''

The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

'''

# Lower Case:

'''

The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

'''

# Remove Whitespace:

'''

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

'''

# Replace String:

'''

The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

'''

# Split String:

'''

The split() method splits the string into substrings if it finds instances of the separator.

returns ['Hello', ' World!']:

a = "Hello, World!"
print(a.split(","))

'''