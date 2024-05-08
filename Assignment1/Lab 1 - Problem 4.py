# -*- coding: utf-8 -*-
"""

@author: LAKSHMIPRIYA Anil
"""

print("Enter first word")
word_A = input().rstrip()
print("Enter second word")
word_B = input().rstrip()

# Sub-problem a)
# Convert each word into a list containing its characters
letters_A = set(word_A)
letters_B = set(word_B)
print("The letters of the first word ", word_A, 'are: ', letters_A)
print("The letters of the first word ", word_B, 'are: ', letters_B)

# Sub-problem b)
# Find the union and intersection sets
union_list = list(letters_A.union(letters_B))
intersection_list = list(letters_A.intersection(letters_B))
print("The union of the list of letters of the two words is: ", union_list)
print("The intersection of the list of letters of the two words is: ", intersection_list, "\n")

# Sub-problem b)
# Sort union list with lowercase letters first
lower_letters = []
upper_letters = []
for u in union_list:
    if ord('a') <= ord(u) <= ord('z'):
        lower_letters.append(u)
    if ord('A') <= ord(u) <= ord('Z'):
        upper_letters.append(u)
        
lower_letters.sort()
upper_letters.sort()
lower_letters.extend(upper_letters)
print("Case sensitive sorting of the union list: ", lower_letters)

# Sub-problem b)
# Case-insensitive sorting of the union list
union_list.sort(key = str.lower)
print("Alphabetical sorting of the union list: ", union_list)
        

# =======================================================================================

''' 
OUTPUT
----------

Enter first word
TehnoLogy
Enter second word
BanaNa
The letters of the first word  TehnoLogy are:  {'e', 'y', 'T', 'L', 'n', 'g', 'o', 'h'}
The letters of the first word  BanaNa are:  {'a', 'n', 'N', 'B'}
The union of the list of letters of the two words is:  ['e', 'y', 'T', 'L', 'n', 'N', 'B', 'a', 'g', 'o', 'h']
The intersection of the list of letters of the two words is:  ['n'] 

Case sensitive sorting of the union list:  ['a', 'e', 'g', 'h', 'n', 'o', 'y', 'B', 'L', 'N', 'T']
Alphabetical sorting of the union list:  ['a', 'B', 'e', 'g', 'h', 'L', 'n', 'N', 'o', 'T', 'y']

================================================================================================== 
'''