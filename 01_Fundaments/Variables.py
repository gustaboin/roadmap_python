# Variables
"""
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it."""

a = 7
b = 9.5
c = "Rocket"

# Casting

"If you want to specify the data type of a variable, this can be done with casting."

x = str(a)
y = float(b)
z = int(b)

print(a, b, c)
print("casting")
print(x, y, z)

# Get the Type --> You can get the data type of a variable with the type() function.

print(type(a))
print(type(c))
print(type(y))
print(type(x))

"String variables can be declared either by using single or double quotes:"

" Case-Sensitive: Variable names are case-sensitive."

"is different Number than number"

d = 3
D = "Rocket"

# Variable Names

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.

"""

age = 20
name = "Ines"
hair = "blondie"

# Multi Words Variable Names

""" If you need use multi word variable names there are 3 methods "
1 - camelCase
myName = "John Connor"
2 - PascalCase
MyName = "John Connor"
3- Snake_case
my_name = "john Conor"

"""

myName = "John Connor"
MyName = "John Connor"
my_name = "John Connor"

# Python Variables - Assign Multiple Values

e, f, g = "Williams", "Sauber","Ferari"

print(e,f,g)

# One Value to Multiple Variables
a = b = c = "Red Bull Racing"
print(a)
print(b)
print(c)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

teams = ["Sauber","Red Bull Racing","Ferrari", "Williams"]
w, x, y, z = teams
print(y)
print(x)

# Python - Output Variables
a = "Maclaren"
print(a)

#In the print() function, you output multiple variables, separated by a comma:
print(x,y,z)

# You can also use the + operator to output multiple variables:
print (x + y + z)

"""
For numbers, the + character works as a mathematical operator:
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
"""

a = 7
b = 10
print(a+b)

c = "Oliver"

# print(a+b) give you an error, must be cast the variable"

print(str(b) +" - "+ c )

# Python - Global Variables

"""
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

"""
x = "Rookie"

def func_example():
    print("I am a " + x)

func_example()

# Create a variable inside a function, with the same name as the global variable

x = "Rookie"

def myfunc():
  x = "Professional" # in this case the variable professional is only inside de function
  print("I am a " + x)

myfunc()

print("I am a " + x)


# The global Keyword

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

x = "loser"

def myfunc():
  global x 
  x = "winner" # in this case the variable winner is global
  print("I am a " + x)

myfunc()

print("I am a " + x)