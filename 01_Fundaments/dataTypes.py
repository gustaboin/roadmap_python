# Python Data Types

"""
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType


"""

#Setting the Data Type

#In Python, the data type is set when you assign a value to a variable:

a = "Wellcome to the F1"                        # String
b = 88                                          # Int
c = 1.9                                         # float
d = 1j                                          # complex
v = True;  u = False                            # bool
x = b"Formula One"                              # bytes
w = bytearray(5)                                # bytearray
y = memoryview(bytes(5))                        # memoryView
z = None                                        # NoneType

# another Important Data Type
e = ["Maclaren", "Williams", "Mercedes"]        # list 	
f = ("Sauber", "Ferrari", "Haas") 	            # tuple 	
g = range(6) 	                                # range 	
h = {"name" : "Carlos", "age" : 30} 	        # dict 	
i = {"Mercedes", "Honda", "Ferrari"} 	        # set 	
j = frozenset({"Japon", "Italy", "Spain"}) 	    # frozenset --> there are immutable


print(type(z))

"""
 Unlike the lists, on the set we cannot modify an element through their index. If we try, we'll have a
print(i[0]); TypeError: 'set' object is not subscriptable

"""

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

a =str("Williams")
b = dict({"name":"carlos", "age":"30"})

print(b)


### NUMBERS
# Int, float, complex

x = 1
y = 1.9
z = 7.6j

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

a = -10.33
print(type(a))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 250**250
print(x)
print(type(x))

"""ouptup x
305493636349960468205197939321361769978940274057232666389361390928129162652472045770185723510801522825687515269359046715531785342780428396973513311420091788963072442053377285222203558881953188370081650866793017948791366338993705251636497892270212003524508209121908744820211960149463721109340307985507678283651836204093399373959982767701148986816406250000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
<class 'int'>

"""

"""
Python can represent almost any number, there are limit cases where we can find ourselves with an exception like the one we show below.
the output r = overflow, 
r = (5e200**2)

A curious case is that if we try to represent an even larger number, we will find the following rather than with one exception.
s = (2e2000**2)
"""

r = (5e200**2)
print(r) # result overflow

s = (2e2000**2)
print(s) # result inf
