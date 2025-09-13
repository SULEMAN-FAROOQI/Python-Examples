
# Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.

# Series:

'''

A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type. We can also give it index which complies
to values in the column and using that index we can access that column. Index is like giving serial number to each row in your dataset.
We can also plot our dataset by manuplating our data with panda module.

Example:

import pandas as pd
import numpy as np

x = [3,4,5,6]

y = pd.Series(x, index=["X","Y","Z","O"])

print(y)

Example (Key/Value object in series):

import pandas as pd
import numpy as np

x = {
    "day1" : 900,
    "day2" : 1000,
    "day3" : 1100
}

y = pd.Series(x)

print(y)

'''

# DataFrame:

'''

Some Datasets contains text and data in the form of arrays. To extract this data, we use DataFrame.
A python dataframe is a 2D datasetof a 2D array or a 2D matrix. If we want to access a specific row, we can use loc() function.
If a dataframe is created using a dictionary, then the keys will be the column names.
We can use multiple arguments with our dataset:

1. head() : Prints first 5 rows of the dataset when used with print function.
2. tail() : Prints last 5 rows of the dataset when used with print function.
3. info():  Gives information about our dataset.
4. corr(): Calculates relation between each column in the datasets.

Eliminating and Replacing Wrong Data:

1. The variable.dropna(inplace = True) function will remove all the rows with null values.

2. The variable.fillna(number, inplace = True) will replace empty cells with a value. It can also replace values for specified columns with a 
specified number.

3. A common way to replace empty cells is to calculate mean, median and mode of the columns.

4. variable.replace(new_val, old_val, inplace = TRUE) : This will change the value at the location, it was given. We can also set conditions to
manupilate our data.

5. The variable.drop_duplicates(inplace = True) function will remove all the duplicates from the dataset.

6. the variable.isna() function will tell you how many null values are in dataset.

7. If there are multiple arrays in a dataset, we can use the variable.astype() function to convert them into a single datatype.

8. If there are multiple arrays in a dataset having different keys (columns), we can use 'columns' parameter to set the columns we want 
in our dataframe.

9. We can use the variable.shape function to get the number of rows and columns in our dataframe made from our dataset.

Example:

import pandas as pd
import numpy as np

data = {
    "Calories" : [500,600,800],
    "Protein" : [32,45,52]
}

dataframe = pd.DataFrame(data, index = [1,2,3])

print(dataframe)

Example (Dictionary in DataFrame):

import pandas as pd

data = {
    "Duration" : {
       "0":60,
       "1":50,
       "2":40
    },
    "Pulse": {
        "0":110,
        "1":120,
        "2":130
    }
}

frame = pd.DataFrame(data)
print(frame)

'''

# Comma Seprated Files (CSV) and JSON Files:

'''

A simple way to load big data is to use csv files. It is a plain text format and can be used by pandas.

Example (CSV):

import pandas as pd
import numpy as np

x = pd.read_csv("test.csv")
print(x)

Example (JSON):

import pandas as pd
import numpy as np

x = pd.read_csv("test.json")
print(x)

'''
