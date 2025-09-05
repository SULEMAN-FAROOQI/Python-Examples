# POOP (PYTHON OBJECT ORIETED PROGRAMMING): 

'''

OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP:

1) Provides a clear structure to programs
2) Makes code easier to maintain, reuse, and debug
3) Helps keep your code DRY (Don't Repeat Yourself)
4) Allows you to build reusable applications with less code

'''

# CLASSES AND OBJECTS:

'''

Classes and objects are the two core concepts in object-oriented programming.
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
You can also import classes from module which has that class.

A class defines what an object should look like, and an object is created based on that class. For example:

CLASS	           OBJECTS

Fruit	           Apple, Banana, Mango
Car	             Volvo, Audi, Toyota

When you create an object from a class, it inherits all the variables and functions defined inside that class.
Here the class 'Fruit' has objects 'Apple, Banana, Mango'.

'''

# The __init__() Method:

'''

To understand the meaning of classes we have to understand the built-in __init__() method.
All classes have a method called __init__(), which is always executed when the class is being initiated.

We Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object 
is being created. The __init__() method is called automatically every time the class is being used to create a new object.

Example:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

'''

# Instance variable and Class variable:

'''

An instance variable is declared within a class and inside the constructor (such as function like '__init__()').
A class variable is declared within in a class but outside the constructor(such as function like '__init__()').

'''

# OOP'S EXAMPLE:

# Example no 1:

'''

class Car:

    def __init__(self,maker,model,year,color):
        
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The " +self.model+ " is being drive")

    def stopped(self):
        print("The " +self.model+ " has stopped")

car1 = Car("Toyota","Corolla",2022,"Black")
car2 = Car("Honda","Civic",2023,"Red")

print(car1.maker)
print(car1.model)
print(car1.year)
print(car1.color)

print("\n")

print(car2.maker)
print(car2.model)
print(car2.year)
print(car2.color)

print("\n")

car1.drive()
car2.stopped()

'''

# Example no 2:

'''

class Animals:

    def __init__(self,name,habitat,food):

        self.name = name
        self.habitat = habitat
        self.food = food

    def ecosystem(self):

        if self.habitat ==  "Jungle":
            print("The " +self.name+ " lives in " +self.habitat)

        elif self.habitat == "Sky":
            print("The " +self.name+ " soars in " +self.habitat)

        elif self.habitat == "Ocean":
            print("The " +self.name+ " swims in " +self.habitat)


animal1 = Animals("Tiger","Jungle","Meat")
animal2 = Animals("Falcon","Sky","Meat")
animal3 = Animals("Sharks","Ocean","Meat")

animal1.ecosystem()
animal2.ecosystem()
animal3.ecosystem()

'''

# The self Parameter:

'''

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
In Example 1, self is reffered to as car1 variable which is assigned all the properties of Car Class.

'''

# Inheritance of classes:

'''

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

Example:

class Organism:

    alive = True

    def eat(self):
        print("This oraganism can eat")

    def synthesization(self):
        print("This organism makes food from sunlight")

class Rabbit(Organism):
        
    def graze(self):
        print("The rabbit eats grass")

class Elysia(Organism):

    def synthesize(self):
        print("This organism uses sunlight to makes food")

rabbit = Rabbit()
elysia = Elysia()

print("There are two ways an oraganism makes food")

print(rabbit.alive)
rabbit.eat()
rabbit.graze()
print("---------------------------")
print(elysia.alive)
elysia.synthesization()
elysia.synthesize()

'''

# Multilevel Inheritance:

'''

class predator:

    def hunts(self):
      print("This animal hunts")

class prey:

    def runs(self):
      print("This animal flees")

class Rabbit(prey):
    print("Rabbits are cute!")

class Hawk(predator):
    print("Hawks are bold")

class Fish(predator, prey):
    print("Fishes are gentle")


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.runs()
hawk.hunts()
fish.hunts()
fish.runs()

'''

# Method Over writing:

'''

class animal:

    def eat(self):
        print("This animal can eat")

class Rabbit(animal):

    def eat(self):
        print("This animal eats carrot")

rabbit = Rabbit()
rabbit.eat()

'''

# Method Chaining:

'''

It is a method of calling multiple functions according to their sequence, with each function performing operation on same object 
and returns self.

Example:

class Person():

    def Getup(self):
        print("The person got up from the bed")
        return self
    
    def Work(self):
        print("The person started to perform some work")
        return self
    
    def Sleep(self):
        print("The person went to sleep after a lot of hardwork")
        return self
    

person = Person()

person.Getup().Work().Sleep()

'''

# Abstract class:

'''

An Abstract class is a class which contains one or more abstract methods. An abstarct method is a method that has a declaration but not an
implemantion in the program. The Abstarct method can be over written by a method in a child class that is why, It has no implemantion.
The 'abstractmethod' is a decorator which prevents the user from creating an object (variable) of that class.
A decorator is essentially a function that takes another function as an argument. 
After defining 'abstarctmethod' in the parent class, The child class should have same number of abstract methods.

'abc' means abstract base class. 

'''

# Example 1:

'''

from abc import ABC, abstractmethod

class Vechile(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):

    def go(self):
        print("This Car is moving!")

    def stop(self):
        print("This Car has stopped!")

class Cycle(Vechile):

    def go(self):
        print("This Cycle is moving!")

    def stop(self):
        print("This Cycle has stopped!") 


car =  Car()
cycle = Cycle()

car.stop()
cycle.go()

'''

# Example 2:

'''

from abc import ABC, abstractmethod

class Shape(ABC):
     
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 3.146 * self.radius
    
    def perimeter(self):
        return self.radius * 2
    
class Rectangle(Shape):

    def __init__(self, width, length):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
circle = Circle(6)
rectangle = Rectangle(3, 3)

print("The Area of circle is: " +str(circle.area()))
print("The Perimeter of circle is: " +str(circle.perimeter()))
print("/n")
print("The Area of rectangle is: " +str(rectangle.area()))
print("The Perimeter of rectangle is: " +str(rectangle.perimeter()))

'''