# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:52:54 2023

@author: LAKSHMIPRIYA Anil
"""



# Function to find the minimum vaue in the list
def find_min(numbers):
    min_val = numbers[0]
    
    try:
        for idx in range(len(numbers)):
            n = numbers[idx + 1]        # Trying to access value with invalid index
            if n < min_val:
                min_val = n
                
    except IndexError as idx_err:
        print('IndexError: ', idx_err)
        print('The minimum value till now is:', min_val, '\n')
        print('Enter a number to check the divibility of the minimum number: ')
        try:
            divisor = int(input())      # A number to check the divisibiity of the minimum value
        except ValueError as val_err:
            print('ValueError: ', val_err)
            try:
                print(divisor)          # Trying to access a variable without any value
            except UnboundLocalError as ubl_err:
                print('UnboundLocalError: ', ubl_err)
        else:
            try:
                # Check using Assert statement
                assert divisor != 0, 'The number entered must be non-zero!'
            except AssertionError as assert_err:
                print('AssertionError: ', assert_err)
            else:
                print('Divsible' if min_val % divisor == 0 else 'Not divisible')          
        
    else:
        print('The minimum value is:', min_val)
    finally:
        # finally block - always executed
        print('Code by @LAKSHMIPRIYA_Anil')
    
            
            

def main():
    print('Enter a list of numbers')
    numbers = list(map(int, input().split()))
    find_min(numbers)
  
  
if __name__=="__main__":
    main()       
    
    


# =======================================================================================

''' 
OUTPUT
----------

Enter a list of numbers
4 6 8 15 10 34 82 21 6 5 2 14
IndexError:  list index out of range
The minimum value till now is: 2 

Enter a number to check the divibility of the minimum number: 
two
ValueError:  invalid literal for int() with base 10: 'two'
UnboundLocalError:  cannot access local variable 'divisor' where it is not associated with a value
Code by @LAKSHMIPRIYA_Anil


------------------------------------------

Enter a list of numbers
4 6 8 15 10 34 82 21 6 5 2 14
IndexError:  list index out of range
The minimum value till now is: 2 

Enter a number to check the divibility of the minimum number: 
0
AssertionError:  The number entered must be non-zero!
Code by @LAKSHMIPRIYA_Anil

------------------------------------------

Enter a list of numbers
4 6 8 15 10 34 82 21 6 5 2 14
IndexError:  list index out of range
The minimum value till now is: 2 

Enter a number to check the divibility of the minimum number: 
1
Divsible
Code by @LAKSHMIPRIYA_Anil

------------------------------------------

Enter a list of numbers
4 6 8 15 10 34 82 21 6 5 2 14
IndexError:  list index out of range
The minimum value till now is: 2 

Enter a number to check the divibility of the minimum number: 
8
Not divisible
Code by @LAKSHMIPRIYA_Anil

================================================================================================== 
'''
