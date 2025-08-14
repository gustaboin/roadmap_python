
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

"""

    #    Code	Result	
    #    \'	Single Quote	
    #    \\	Backslash	
    #    \n	New Line	
    #    \r	Carriage Return	
    #    \t	Tab	
    #    \b	Backspace	
    #    \f	Form Feed	
    #    \ooo	Octal value	
    #    \xhh	Hex value



texto =  "We are the so-called \"Vikings\" from the north."

print(texto)

"""
Method      	Description
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