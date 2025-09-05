# Threading:

'''

A Thread is like a flow of execution like a separate form of instruction a program can follow. 
However each threads takes a turn running because of GIL (Global integrating lock) which only allows one thread to hold the control of
python interpreter. 

There are 2 types of threads:

1. cpu bound: Programs or Task which spends most of it's time waiting for internal events like programs perform by ALU.
2. io bound: Programs or Task which spends most of its time waiting for external events like user input.

Statement                                              Function

1. print(threading.active_count())                     Prints the Number of thread working in program
2. print(threading.enumerate())                        Prints the enumeration of threads

Example:

Without threading:

import threading 
import time

def wakeup():
    print("You wake up!")
    time.sleep(3)

def wash():
    print("You wash yourself!")
    time.sleep(6)

def breakfast():
    print("You ate breakfast!")
    time.sleep(10)

wakeup()
wash()
breakfast()

With threading:

import threading 
import time

def wakeup():
    print("You wake up!")
    time.sleep(3)

def wash():
    print("You wash yourself!")
    time.sleep(6)

def breakfast():
    print("You ate breakfast!")
    time.sleep(10)

x = threading.Thread(target=wakeup)
x.start()

y = threading.Thread(target=wash)
y.start()

z = threading.Thread(target=breakfast)
z.start()

'''

# Demon Threads:

'''

A Demon thread is a thread that runs in the background, Your real program will not wait for demon threads to complete. If not specified
to end, the demon thread will still run.

Example:

import threading
import time

def timer():
    print()
    count = 0 
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: " +str(count)+ "seconds")

x = threading.Thread(target = timer , daemon = True)
x.start()

answer = input("Would you like to log out?" +"\n")

'''