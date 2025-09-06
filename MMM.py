# Mean:

'''

The mean value is the average value.

Example:

Use the NumPy mean() method to find the average speed:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

'''

# Median:

'''

The median value is the value in the middle, after you have sorted all the values.

Example:

Use the NumPy median() method to find the middle value:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

'''

# Mode:

'''

The Mode value is the value that appears the most number of times.

Example:

Use the SciPy mode() method to find the number that appears the most:

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

'''