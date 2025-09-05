# FUNCTIONS:

'''

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.
A function can return data as a result. In Python a function is defined using the 'def' keyword

To call a function, use the function name followed by curly brackets.

Example:

def my_function():
  print("Hello from a function")

my_function()

'''

# Arguments:

'''

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the curly brackets. You can add as many arguments as you want, 
just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, 
we pass along a first name, which is used inside the function to print the full name:

Example:

def my_function(name):
  print(name + " Refsnes")

my_function("Emil")
my_function("Tobias")

'''

# GLOBAL VARIABLE DEFINED WITHIN A FUNCTION:

'''

def func():
    global x
    x = "fantastically boring"

func()
print("PYTHON IS " +x)

'''

# ARBITARY ARGUMENTS:
# ARGS:

'''

An Argument should start with a '*' sign. In contrary we can name our argument anything.

Example 1:

def add(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum

print(add(1,2,2,23,56,78))

Example 2:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

Example 3:

def my_function(*food):
  for x in food:
    print(x, end = " ")

fruits = ["apple", "banana", "cherry"]
Vegetables = ("potato", "garlic", "chilli")
crockery = ("spoon", "fork", "plate", "bowl")

my_function(fruits, Vegetables)

'''

# ARBITARY KEYWORD ARGUMENTS:
# KWARGS:

'''

Example:

Keyword Argument should start from '**' sign. In contrary we can name our keyword argument anything.

def names(**name):
    print("Hello", end = " ")
    for key,value in name.items():
        print(value, end = " ")

names(start = "SULEMAN", middle = "HUSSAIN", end = "FAROOQI")

'''

# DEFAULT PARAMETERS VALUE:

'''

If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

'''

# List as an Argument:

'''

You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.

Example:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

'''

# Return Values:

'''

To let a function return a value, use the 'return' statement:

Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

'''

# Functions as Variables:

'''

def hello():
  print("Hello")

hi = hello
hi()
print(hi)

say = print
say("Hello, My Nigga")

'''

# Higher Order Functions:

'''

A Higher order function is a function is a function that accepts another function as an argument or returns a function.

Example 1:

def loud(text):
   return text.upper()

def quite(text):
   return text.lower()

def Greetings(func):
    text = func("Hello")
    print(text)

Greetings(loud)
Greetings(quite) 

Example 2:

def divisor(x):
    def divident(y):
        return y / x
    return divident

divide = divisor(2)
print(divide(10))

'''

# Lambda Function:

'''

A Lambda function is a function that is written in only one line. It can accept multiple arguments but has only 
one expression.

Examples: 

add = lambda x , y : x + y
print(add(2 , 3))

divide = lambda x , y : x / y
print(divide(30 , 3))

greetings = lambda first , last : first+" "+last
print(greetings("Suleman" , "Farooqi"))

age = lambda x : ("Can Drive") if x>=18 else ("Cannot drive")
print(age(19))

'''

# Map Function:

'''

The map function applies a function to an iterable (list, tuple, dictionary etc).

[map(Function , Iterable)]

Example:

Items = [("Shirt" , 300),
         ("Pants" , 500),
         ("Trousers" , 450),
         ("Socks" , 200)
         ]

Dollars = lambda item : (item[0] , item[1] * 300)

Changed = map(Dollars , Items)

for i in Changed:
    print(i)

'''

# Filter Function:

'''

It creates a collection of elements from an iterable based on a function's condition, if it returns True.

[ filter(Function , Iterable) ]

Example:

Persons = [("Suleman" , 19),
           ("Ibrahim" , 17),
           ("Yousuf" , 16),
           ("Ahmed" , 14),
           ("Kamran" , 56)
           ]

age = lambda x : x[1] >= 18

drive = list(filter(age , Persons))
drive.sort()

for drivers in drive:
    print(drivers)

'''

# Reduce Function:

'''

It performs a function on an iterable and reduce it until 1 value remains.

Example 1:

import functools

Letters = ["A","P","P","L","E"]
append = lambda x , y : x + y
appended = functools.reduce(append , Letters)

print(appended)

Example 2:

import functools

Numbers = [10,9,8,7,6,5,4,3,2,1]
multiply = lambda x , y : x * y
factorial = functools.reduce(multiply , Numbers)

print(factorial)

'''

# List Comprehension:

'''

It is a way to create new list with less syntax.

1. list = [ (Expression) (for item in iterable) ]
2. list = [ (Expression) (for item in iterable) (if condition) ]
3. list = [ (Expression) (if-else condition) (for item in iterable) ]

Example 1:

squares = [i * i for i in range(1,11)]
print(squares)

Example 2:

Numbers = [100,80,70,60,50,40,30,20]
passing_marks = [i for i in Numbers if i>=50]

print(passing_marks)

Example 3:

Numbers = [100,80,70,60,50,40,30,20]
passing_marks = [i if i>=50 else "Failed" for i in Numbers]

print(passing_marks)

'''

# Dictionary Comprehension:

'''

It creates dictionaries using an expression.

1. dictionary = { (key : ) (expression) (for key,value in iterable) }
2. dictionary = { (key : ) (expression) (for key,value in iterable) (if condition) }
3. dictionary = { (key : ) (if/else condition) (expression) (for key,value in iterable) }
4. dictionary = { (key : ) (function(value)) (for key,value in iterable) }

Example 1:

meters = {"karachi" : 500,
          "lahore" : 400,
          "peshawar" : 700,
          "quetta" : 900
          }

kilometers = {key : (value / 1000) for key,value in meters.items()}
print(kilometers)

Example 2:

cities = {"karachi" : 25,
          "lahore" : 30,
          "jacobabad" : 58,
          "sawat" : 5,
          "islamabad" : 12
          }

cold_cities = {key: (value) for key,value in cities.items() if value <=15 }
print(cold_cities)

Example 3:

cities = {"karachi" : 25,
          "lahore" : 30,
          "jacobabad" : 58,
          "sawat" : 5,
          "islamabad" : 12
          }

cold_cities = {key: ("Cold!" if value <=15 else "Hot !!!")  for key,value in cities.items()}
print(cold_cities)

Example 4:

cities = {"Karachi" : 25,
          "Lahore" : 30,
          "Jacobabad" : 58,
          "Sawat" : 5,
          "Islamabad" : 12
          }

def temperature(value):
    if value <= 15:
        return "COLD!"
    elif value < 40:
        return "Hot!"
    elif value > 40:
        return "Very HOT!"

cold_cities = {key: temperature(value) for key,value in cities.items()}
print(cold_cities)

'''

# Zip Function:

'''

It aggregates elements from two or more iterables and combine(zip) them into a single iterable. The new iterable, if not
given new data type will have zip data type.

iterable_3 = zip(iterable_1, iterable_2)

Example 1:

users = ["Nigga 1" , "Nigga 2" , "Nigga 3"]
passwords = (1234, 5678, 8901)

users_info = dict(zip(users,passwords))

for (key , value) in users_info.items():
    print(key+" : "+str(value))

Example 2:

users = ["Nigga_1" , "Nigga_2" , "Nigga_3"]
passwords = (1234, 5678, 8901)
login_date = {"1/2/21" , "2/2/21" , "3/2/21"}

users_info = zip(users,passwords,login_date)

for i in users_info:
    print(i)

'''

# The sorted() Function:

'''

The 'sorted()' function can be used in any iterables. It has a keyword argument reverse which reverses the order. 
The reverse argument has a value of 'True' and 'False'.

Example 1:

students = (Ali, Hamza, saim, Ahmed)
sorted = sorted(students)

for items in sorted:
  print(items)

Example 2:

Persons = [("Kamran Husaain Farroqi" , 56),
           ("Nazish Kamran" , 42),
           ("Suleman Husaain Farooqi" , 19),
           ("Ibrahim Hussain Farooqi" , 17),
           ("Mohammed Yousuf Hussain Farooqi" , 16),
           ("Ahmed Hussain Farooqi" , 15)
           ]

age = lambda x : x[1]
sorted = sorted(Persons , key=age)

for items in sorted:
    print(items)

'''