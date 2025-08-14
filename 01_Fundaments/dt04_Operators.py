# Python Operators

# Python Arithmetic Operators


"""

Operator 	Name 	            Example 	
+ 	        Addition 	        x + y 	
- 	        Subtraction 	    x - y 	
* 	        Multiplication 	    x * y 	
/ 	        Division 	        x / y 	
% 	        Modulus 	        x % y 	
** 	        Exponentiation 	    x ** y 	
// 	        Floor division 	    x // y

"""

x = 21
y = 3

print(x + y )
print(x - y )
print(x * y )
print(x / y )
print(x % y )
print(x ** y)
print(x // y)

# Python Assignment Operators

"""
Operator 	Example 	    Same As 	
= 	        x = 5 	        x = 5 	
+= 	        x += 3 	        x = x + 3 	
-= 	        x -= 3 	        x = x - 3 	
*= 	        x *= 3 	        x = x * 3 	
/= 	        x /= 3 	        x = x / 3 	
%= 	        x %= 3 	        x = x % 3 	
//=         x //= 3 	    x = x // 3 	
**=         x **= 3 	    x = x ** 3 	
&= 	        x &= 3 	        x = x & 3 	
|= 	        x |= 3 	        x = x | 3 	
^= 	        x ^= 3 	        x = x ^ 3 	
>>=         x >>= 3 	    x = x >> 3 	
<<=         x <<= 3 	    x = x << 3 	
:= 	        print(x := 3) 	x = 3
print(x)

"""

# Python Comparison Operators

"""
Operator 	Name 	                    Example 	
==          Equal 	                    x == y 	
!=          Not equal 	                x != y 	
>           Greater than 	            x > y 	
<           Less than   	            x < y 	
>=          Greater than or equal to 	x >= y 	
<=          Less than or equal to 	    x <= y
"""

# Python Logical Operators
# Logical operators are used to combine conditional statements:
"""
Operator 	Description 	                                            Example 	
and  	    Returns True if both statements are true 	                x < 5 and  x < 10 	
or 	        Returns True if one of the statements is true 	            x < 5 or x < 4 	
not 	    Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)
"""

#And
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# OR
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False


# Python Identity Operators

"""
Operator 	Description 	                                            Example 
is  	    Returns True if both variables are the same object 	        x is y 	
is not 	    Returns True if both variables are not the same object 	    x is not y
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is not b)  # True, because a and b are different list objects in memory
print(a is not c)  # False, because c refers to the same list object as a
print(a is not None) # True, because a is a list object, not None

# Python Membership Operators

"""

Operator 	Description 	                                                                        Example 	
in        	Returns True if a sequence with the specified value is present in the object            x in y 	
not in 	    Returns True if a sequence with the specified value is not present in the object 	    x not in y

"""

# With strings
my_string = "Hello World"
print('H' in my_string)      # Output: True
print('x' in my_string)      # Output: False
print('W' not in my_string)  # Output: False

# With lists
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)          # Output: True
print(6 in my_list)          # Output: False
print(10 not in my_list)     # Output: True

# With dictionaries (checks for keys, not values)
my_dict = {'apple': 1, 'banana': 2}
print('apple' in my_dict)    # Output: True
print(1 in my_dict)          # Output: False (checks for keys)
print('orange' not in my_dict) # Output: True


# Python Bitwise Operators

"""
Operator 	Name 	                Description 	                                                                    Example
&           AND 	                Sets each bit to 1 if both bits are 1 	                                            x & y 	
|           OR 	                    Sets each bit to 1 if one of two bits is 1 	                                        x | y 	
^           XOR 	                Sets each bit to 1 if only one of two bits is 1 	                                x ^ y 	
~           NOT 	                Inverts all the bits 	                                                            ~x 	
<<          Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off 	x << 2 	
>>          Signed right shift  	Shift right by pushing copies of the leftmost bit in from the left, 
                                                                    and let the rightmost bits fall off 	            x >> 2

"""


result = 5 & 3  # 5 is 101, 3 is 011. Result is 001 (1)
result = 5 | 3  # 5 is 101, 3 is 011. Result is 111 (7)
result = 5 ^ 3  # 5 is 101, 3 is 011. Result is 110 (6)
result = ~5  # 5 is 0...0101. Result is ...11010 (-6)
result = 5 << 2  # 5 is 101. Shifted left by 2 becomes 10100 (20)
result = 5 >> 1  # 5 is 101. Shifted right by 1 becomes 10 (2)



# Operator Precedence
# Operator precedence describes the order in which operations are performed.
"Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:"
print((6 + 3) - (6 + 3)) 

"Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:"
print(100 + 5 * 3) 

#*******************#
#***  IMPORTANT! ***#
#*******************#

"The precedence order is described in the table below, starting with the highest precedence at the top:"


"""
Operator 	            Description 	
() 	                    Parentheses 	
**      	            Exponentiation 	
+x  -x  ~x 	            Unary plus, unary minus, and bitwise NOT 	
*  /  //  %             Multiplication, division, floor division, and modulus 	
+  - 	                Addition and subtraction 	
<<  >> 	                Bitwise left and right shifts 	
& 	                    Bitwise AND 	
^ 	                    Bitwise XOR 	
| 	                    Bitwise OR 	
==  !=  >  >=  
<  <=  is  is not       Comparisons, identity, and membership operators 
in  not in  		
not 	                Logical NOT 	
and 	                AND 	
or 	                    OR


"""

"Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:"

print(5 + 4 - 7 + 3)  # resutlt 5