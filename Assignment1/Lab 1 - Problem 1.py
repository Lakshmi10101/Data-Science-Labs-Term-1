# -*- coding: utf-8 -*-
"""

@author: LAKSHMIPRIYA Anil
"""

# Subproblem a)
def check_for_even_odd(num):
    if num % 2 == 0:
        print('The number ', num , 'is even.')
    else:
        print('The number ', num , 'is odd.')

# Subproblem b)
def sum_using_for(num):
    sum_val = 0
    for i in range(num + 1):
        sum_val += i
    print('The sum of all the numbers till the given number is: ', sum_val)

# Subproblem c)
def digit_sum_using_while(num):
    sum_val = 0
    n = num
    while n > 0:
        rem = n % 10
        n //= 10
        sum_val += rem
    print('The sum of the digits of the number ', num, ' is: ', sum_val)

# Subproblem d)
def create_num_list(num):
    n_list = list(range(0, num + 1))
    print('The list of numbers till ', num, ' is: ', n_list)
    return n_list

# Subproblem e)
def replace_multiple():
    for idx in range(3, num + 1, 3):
        numbers[idx] = 0
    print('The modified list of numbers till ', num, ' is: ', numbers)

# Recusion example
def sum_using_recursion(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    sum_val = num + sum_using_recursion(num - 1)
    return sum_val




print('Enter a positive number less than 20: ')
num = int(input())

if 0 < num < 20:
    
    # Subproblem a)
    check_for_even_odd(num)
    
    # Subproblem b)
    sum_using_for(num)
    
    # Subproblem c)
    digit_sum_using_while(num)
    
    # Subproblem d)
    numbers = create_num_list(num)
    
    # Subproblem e)
    replace_multiple()
    
    # Recusion example
    sum_recrr = sum_using_recursion(num)
    print('The sum of all the numbers till the given number using recursion is: ', sum_recrr)
    
    
# =======================================================================================

''' 
OUTPUT
----------

Enter a positive number less than 20: 
16
The number  16 is even.
The sum of all the numbers till the given number is:  136
The sum of the digits of the number  16  is:  7
The list of numbers till  16  is:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
The modified list of numbers till  16  is:  [0, 1, 2, 0, 4, 5, 0, 7, 8, 0, 10, 11, 0, 13, 14, 0, 16]
The sum of all the numbers till the given number using recursion is:  136

================================================================================================== 
'''
