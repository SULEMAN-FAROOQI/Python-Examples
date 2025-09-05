# Time Module:

'''

Can be initialized by "Import time"

import time

Statement                                   Function  

1. print(time.ctime(0))                     States THe time in seconds when our computer thinks time begin.
2. print(time.time())                       Returns time passed since our computer thinks begins.
3. print(time.ctime(time.time()))           Prints cureent date and time
4. time.sleep(Number)                       Prints the statement before after Number interval of time
5. print(time.perf_count())                 Prints the time taken to execute the program 

FUNCTIONS:

1. asctime() Configuration = (year, month, day, hours, mins, secs, day of the week, day of the year, daylight saving time)

Example:

import time

time_tuple = (2020 , 11 , 3 , 22 , 12 , 9, 0 , 0 , 0)
time_config = time.asctime(time_tuple)
print(time_config)

2. mktime() Configuration = (year, month, day, hours, mins, secs, day of the week, day of the year, daylight saving time)

It converts time to the time passed since our computer thinks time begins.

Example:

import time

time_tuple = (2020 , 11 , 3 , 22 , 12 , 9, 0 , 0 , 0)
time_config = time.mktime(time_tuple)
print(time_config)

'''