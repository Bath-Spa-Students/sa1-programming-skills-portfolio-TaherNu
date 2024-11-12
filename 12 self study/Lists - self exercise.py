names = ['josh', 'mk', 'shakir', 'boko', 'yasin']
print(names[0].title())
print(names[1].title())
print(names[2].title()) #the .title() tells python to print the item from the list in title form where the first letter is capitalized
print(names[-2].title()) #The [-2] tells python to print the 2nd last item from the list names.
print(names[-1].title())
message = "Hello"
message_2 = "how are you doing today?"
print(message, names[0].title(), message_2)
print(message, names[-4].title(), message_2)
print(message, names[2].title(), message_2)
print(message, names[3].title(), message_2)
print(message + " " + names[-1].title() + " " + message_2) #this is tring concatenation 

Transportation = ['tesla', 'motorcycle', 'lamborghini', 'bike', 'ur mama']
statement_1 = "I would like to own a"

print(statement_1 ,Transportation[0].title())
print(statement_1 ,Transportation[1].title())
print(statement_1 ,Transportation[-3].title())
print(statement_1 ,Transportation[3].title())
print(statement_1 ,Transportation[-1].title())
Transportation[0] = 'tesla bus' #This command changes the first value in the list from 'tesla' to 'tesla bus'
print(statement_1 ,Transportation[0].title())
print(Transportation) # as you can see here the first item 'tesla' has been changed to 'tesla bus'
Transportation.append('tesla motorcylce') #.append() is used to add another item to the list but cannot be used to add it to a precise position in the list
print(Transportation)
Transportation.insert(1, 'tesla van') 
""".insert(1,) here was used to insert another item into the Transportation list,
the 1 in between the brackets tells python the precise position of where to insert the new item in the list"""
print(Transportation)
del Transportation[0] #del is used to delete an item in the list the [0] tells python the position of the item in the list
print(Transportation)
popped_Transportation = Transportation.pop(2) 
"""This The pop() method removes the last item in a list, but it lets you work with that item after removing it. 
You can choose the precise item u want to pop from the list by typing its position between the .pop()
In this case, the item that was popped in the list was 'lamborghini'. 
However this popped item can still be used and can be stored in a variable"""
print(Transportation)
print(popped_Transportation)
Transportation.remove ('ur mama') 
""".remove() can be used to remove an item from the list without knowing the precise position of the item,
u can remove an item by just typing its name, here we removed the item 'ur mama'"""
print(Transportation)
Too_Expensive = 'tesla van'
Transportation.remove(Too_Expensive)
print(Transportation)
print(Too_Expensive)