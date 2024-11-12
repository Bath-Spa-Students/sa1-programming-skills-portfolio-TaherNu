Guest_list = ['Mk', 'Josh', 'Shakir', 'Boko', 'Yasin'] #This is a list including many names
print("This is the original order of the text", Guest_list)
Guest_list.sort() #This .sort() sorts the data in the list in alphabetical order pernamently
print('\n This is the temporarly sorted list ', sorted(Guest_list)) #this allows you to temporarly sort the list in alphabatical order
Guest_list.sort(reverse=True) #You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
print("here is the reverse alphabetical sorted list", Guest_list)
Guest_list.reverse()
print('\n This is the reversed list',Guest_list)
print(len(Guest_list))