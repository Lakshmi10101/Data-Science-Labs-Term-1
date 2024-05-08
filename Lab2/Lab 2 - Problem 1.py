# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:45:51 2023

@author: LAKSHMIPRIYA Anil
"""

# Sub-problem b
# Returns the number of lines and number of characters (including spaces) in the above file
def count_line_chars():
    file_lak.seek(0)
    line_cnt = len(file_lak.readlines())        # The number of lines
    file_lak.seek(0)
    content = file_lak.read()
    char_cnt = len(content)                     # The number of characters    
    return (line_cnt , char_cnt)

# Sub-problem c
def write_additional(line_cnt , char_cnt):
    if line_cnt < 2 or char_cnt < 50:
        add_str = 'It was so much fun!\n'
        add_len = len(add_str)
        while char_cnt < 50 or line_cnt < 2:    # Write lines until condition is satisfied
            file_lak.write(add_str)
            line_cnt += 1
            char_cnt += add_len
        
        print('Updated file content is:\n')
        file_lak.seek(0)
        print(file_lak.read())
        print('\n')
   
# Sub-problem d
# Check if given word exists in file
def check_occurence(word):
    file_lak.seek(0)
    content = file_lak.read().lower()
    if word.lower() in content:
        return True
    else:
        return False
    
# Sub-problem e
# Returns the longest and shortest word in the file
def find_long_short(): 
    file_lak.seek(0)
    content = file_lak.read()
    words = content.split()
    
    longest_word = max(words,key=len)
    shortest_word = min(words,key=len)
    return (longest_word, shortest_word)
    
# Sub-problem f
# Swaps adjacent words in the file
def swap_adjacent():
    file_lak.seek(0)
    content = file_lak.readlines()
    new_content = []
    for line in content:
        punctuation = line[-2]      # Full-stop (.) or exclamation (!) etc
        line = line[:-2]            # Remove newline character ('\n') and punctuation
        words = line.split()        # List of words in line
        new_order = []
        
        for idx in range(0, len(words) - 1, 2):
            new_order.extend([words[idx + 1], words[idx]])      # Swapping adjacent words
        
        new_sentence = ' '.join(new_order)
        new_sentence += punctuation
        new_sentence += '\n'
        new_content.append(new_sentence)
     
    # Writing the changed content onto the file
    with open('C://Plaksha//DSLab//Lab2//TLP_Lakshmipriya.txt', 'w') as file:
        file.write(' '.join(new_content))
            
        


# a) - Create and write to file
file_lak = open('C://Plaksha//DSLab//Lab2//TLP_Lakshmipriya.txt', 'a+')
file_lak.write('We have gone throgh file and exception handling.\n')

# b) 
line_cnt , char_cnt = count_line_chars()
print('The number of lines in the text is :', line_cnt)
print('The number of characters(including spaces) in the text is :', char_cnt,'\n\n')

# c)
write_additional(line_cnt , char_cnt)

# d)
print('Enter a word:')
word = input().rstrip()
word_occurence = check_occurence(word)
if word_occurence == True:
    print('The word ', word, ' exists in the file TLP_Lakshmipriya.txt\n')
else:
    print('The word ', word, ' does not exist in the file TLP_Lakshmipriya.txt\n')
    
    
# e) 
longest_word, shortest_word = find_long_short()
print('The longest word in the file is: ', longest_word)
print('The shortest word in the file is: ', shortest_word, '\n')

#f)
swap_adjacent()
with open('C://Plaksha//DSLab//Lab2//TLP_Lakshmipriya.txt', 'r') as file:
    content = file.read()
    print('\nThe updated file after swapping is:\n')
    print(content)

# Closing the file 
file_lak.close()



# =======================================================================================

''' 
OUTPUT
----------

The number of lines in the text is : 1
The number of characters(including spaces) in the text is : 49 


Updated file content is:

We have gone throgh file and exception handling.
It was so much fun!



Enter a word:
gone
The word  gone  exists in the file TLP_Lakshmipriya.txt

The longest word in the file is:  exception
The shortest word in the file is:  We 


The updated file after swapping is:

have We throgh gone and file handling exception.
 was It much so!

================================================================================================== 
'''