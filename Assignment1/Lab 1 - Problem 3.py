# -*- coding: utf-8 -*-
"""

@author: LAKSHMIPRIYA Anil
"""

# Program to check if the given string is a palindrome

print("Enter a string:")
inp_str = input()

rev_str = "".join(reversed(inp_str))
if rev_str == inp_str:
    print("The string ", inp_str, " is a palindrome.")
else:
    print("The string ", inp_str, " is not a palindrome.")
    
    
# =======================================================================================

''' 
OUTPUT
----------

Enter a string:
madam
The string  madam  is a palindrome.

------------------------------------------

Enter a string:
malayalam
The string  malayalam  is a palindrome.

------------------------------------------

Enter a string:
apple
The string  apple  is not a palindrome.

================================================================================================== 
'''