'''Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.'''

#List of Names
Names = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']
#ask user a name to search
search_name = input('Please enter the name you want to search in the list here: ')
#If to check if name in the list
if search_name.strip().title() in Names:
    print(f'{search_name} found in list of Names')
else:
    print('name is not found in the list')