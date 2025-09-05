
# LIST EXAMPLE:

'''

Lists are used to store multiple items in a single variable. A List is a collection which is ordered but changeable. It allows duplicates.
Lists are created using square brackets

Example 1:

food = ["pizza", "burger", "pasta", "salad"]
food[0]= "pudding"

food.append("ice cream")
food.insert(2, "sushi")
food.remove("salad")
food.sort()

'sort()' method can not be used with other iterables like tuple, sets or dictionary. It has a keyword argument reverse which 
reverses the order. The reverse argument has a value of 'True' and 'False'.

for items in food:
    print(items) 

Example 2: 

drinks = ["water", "soda", "juice", "tea"]
dinners = ["pizza", "burger", "pasta", "salad"]
desserts = ["cake", "ice cream", "pie", "pudding"]

food = [drinks, dinners, desserts]

for items in food:
    print(items)

Example 3:

Persons = [("Kamran Husaain Farroqi" , 56),
           ("Nazish Kamran" , 42),
           ("Suleman Husaain Farooqi" , 19),
           ("Ibrahim Hussain Farooqi" , 17),
           ("Mohammed Yousuf Hussain Farooqi" , 16),
           ("Ahmed Hussain Farooqi" , 15)
           ]

age = lambda x : x[1]
Persons.sort(key=age)

for items in Persons:
    print(items)

'''

# TUPLE EXAMPLE:

'''

Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. It allows duplicates.

Tuples are written with round brackets

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "strawberry")

for items in fruits:
  print(items)

print(len(fruits))
print(fruits.index("kiwi"))  
print(fruits.count("melon")) 

'''

# SETS EXAMPLE:

'''

Sets are used to store multiple items in a single variable. A set is a collection which is unordered and unindexed.
Set items are unchangeable, but you can remove items and add new items. It does not allow duplicates.

Sets are written with curly brackets.

vegetables = {"carrot", "broccoli", "spinach", "potato", "tomato"}
vegetables.add("cucumber")
vegetables.remove("potato")

for items in vegetables:
    print(items)

'''

# DICTIONARY EXAMPLE:

'''

Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, 
changeable and do not allow duplicates.

Dictionaries are written with curly brackets

capitals = {'USA':'washington dc','india':'new delhi'}

for key,value in capitals.items():
    print(key, value)


def country(name , capital):
    print("the name of the country is " +name)
    print("the capital of the country is " +capital)

country("Pakistan", "Islamabad")

'''
