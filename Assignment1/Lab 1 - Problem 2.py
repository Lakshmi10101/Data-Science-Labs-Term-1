# -*- coding: utf-8 -*-
"""

@author: LAKSHMIPRIYA Anil
"""
def check_for_leap_yr(yr):
    if yr % 400 == 0:
        return True
    if yr % 4 == 0 and yr % 100 != 0:
        return True
    return False
        
        
print('Enter a year: ')
year = int(input())

flag = check_for_leap_yr(year)

if flag == True:
    print('The year ', year, ' is a leap year')
else:
    print('The year ', year, ' is not a leap year')
    
    
# =======================================================================================

''' 
OUTPUT
----------

Enter a year: 
2016
The year  2016  is a leap year

------------------------------------------

Enter a year: 
1900
The year  1900  is not a leap year

------------------------------------------

Enter a year: 
2000
The year  2000  is a leap year

------------------------------------------

Enter a year: 
1996
The year  1996  is a leap year

================================================================================================== 
'''