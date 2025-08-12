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


#        r = (5e200**2)
#        print(r) # result overflow

s = (2e2000**2)
print(s) # result inf

#***************************
#    01 ---> STRINGS    ****
#***************************
"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'Aston Martin' is the same as "Sauber".

You can display a string literal with the print() function:
"""

# Multiline is with """ text here """

text  = """ Hello, World!
this is a test, 
for learn
snake ? or
python
"""
print(text)

# strings are arrays. Square brackets can be used to access elements of the string.

print(text[10])


#   Looping Through a String
#   Since strings are arrays, we can loop through the characters in a string, with a for loop.


for t in text:
    print(t)


#    String Length
#   To get the length of a string, use the len() function.

print(len(text))

# in and not in in text

# IN: To check if a certain phrase or character is present in a string, we can use the keyword in.

print("World" in text) # if world is in text then True if not False

# Check if NOT To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("expensive" not in text)


# Slicing

a = "Hola mundo!"
print(a[2:5])       # Get the characters from position 2 to position 5 (not included):

b = "Hello, World!" 
print(b[:5])        # Get the characters from the start to position 5 (not included):



c = "Ciao, mondo!" 
print(c[3:])        # Slice To the End  By leaving out the end index, the range will go to the end:

# Modify strings

print(text.upper()) # upper case 

# remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String

i = "bella, Italia!"
print(i.replace("b", "B"))

# Split string
# The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation

a = "Sicilia "
b = "Itay"
c = a + " - " + b
print(c)


# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers directly, 
# But we can combine strings and numbers by using f-strings or the format() method!:

age = 44
name = "Halina"

my_string = f"my name is {name} and I am {age}"
print(my_string)

# Placeholders and Modifiers: A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 25.55
seller = f"The price is {price} dollars"
print(seller)

price = 25.875
seller2 = f"The price is {price:.2f} dollars"             # Display the price with 2 decimals:
print(seller2)              



# Escape Character
"""
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


Code	Result	
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value


"""
texto =  "We are the so-called \"Vikings\" from the north."

print(texto)

"""
Method          	Description
capitalize()    	Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()         	Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()    	Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()  	Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()   	Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()  	        Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            plits the string at the specified separator, and returns a list
splitlines()        Splits the string at line breaks and returns a list
startswith()        Returns true if the string starts with the specified value
strip()             Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning

"""