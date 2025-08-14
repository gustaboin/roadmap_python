# Python Booleans

a = 2025
b = 2001

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

  print(bool("Nie Viem"))


  """
  Most Values are True

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
  
  """

bool(123)
bool("Hello")

"""
Some Values are False

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.

"""

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 


"""
Python also has many built-in functions that return a boolean value, like the isinstance() function,
which can be used to determine if an object is of a certain data type:
"""

x = 10
print(isinstance(x, int)) 