"""Exercise 8: Simple Search - 30 Marks
Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
"""

#List of Names
Names = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']
#searches name in list
search_name = 'Sam'
#if name in list
if search_name in Names:
    #print statement shows
    print(f'{search_name} found in list of Names')
else:
    print('name is not found in the list')