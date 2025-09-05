# Exception: 

'''

Events occur during the execution which interrupt the flow of program, Such as dividing a number by zero.
1) The 'try' block lets you test a block of code for errors.
2) The 'except' block lets you handle the error.
3) The 'else' block lets you execute code when there is no error.

Example:

try:
  numerator = int(input("Enter the first number: "))
  denominator = int(input("Enter the second number: "))
  divison = numerator / denominator

except Exception:
  #print("Something went Wrong :(")

except ZeroDivisionError:
  print("You can't divide by zero! Baka!")

except ValueError:
  print("Enter an integer, Genius!")

else:
  print(divison)

'''