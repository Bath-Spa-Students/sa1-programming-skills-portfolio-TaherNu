Guest_list = ['Mk', 'Josh', 'Shakir', 'Boko', 'Yasin'] #This is a list including many names
message1 = 'Hello' 
message2 = "how are you doing today?, i'd like to invite you to dinner at my house today"
print(message1, Guest_list[0].title(), message2) 
"""The following print statement write an invite to a name from the list of guest names
.title() writes the name in title form"""
print(message1, Guest_list[1].title(), message2) 
print(message1, Guest_list[-3].title(), message2) 
print(message1, Guest_list[3].title(), message2) 
print(message1, Guest_list[-1].title(), message2) 
print(Guest_list[3].title(), "cant make it to dinner")#This print statements writes that the name 'boko' from the guest list cant make it to dinner
del Guest_list[-2] #This command deletes the name 'boko' from the position of -2 in the Guest list
Guest_list.insert(-2, 'dani') #This command inserts the name 'dani' into the -2 position in the Guest list

"""The following print statement write an invite to a name from the list of guest names
.title() writes the name in title form"""
print(message1, Guest_list[0].title(), message2)
print(message1, Guest_list[1].title(), message2)
print(message1, Guest_list[-3].title(), message2)
print(message1, Guest_list[3].title(), message2)
print(message1, Guest_list[-1].title(), message2)

print(message1, "everyone, I've just stumbled across a bigger dinner table so I'll be inviting a few more of our friends")
Guest_list.insert(0, 'Venice') #This command inserts the name 'venice' into the 0 position in the Guest list
Guest_list.insert(-3, 'Dane') #This command inserts the name 'dane' into the -3 position in the Guest list
Guest_list.insert(8, 'Justine') #This command inserts the name 'justine' into the 8 position in the Guest list
print(Guest_list)

"""The following print statement write an invite to a name from the list of guest names
.title() writes the name in title form"""
print(message1, Guest_list[0].title(), message2)
print(message1, Guest_list[1].title(), message2)
print(message1, Guest_list[-3].title(), message2)
print(message1, Guest_list[3].title(), message2)
print(message1, Guest_list[4].title(), message2)
print(message1, Guest_list[2].title(), message2)
print(message1, Guest_list[-2].title(), message2)
print(message1, Guest_list[-1].title(), message2)

print(message1, """everyone, im so sorry for the delays and short notices,
however the new dinner table wont come in time and i can only invtie 2 of you""")
message3 = ", Im so sorry but you're no longer inviteed to the dinner due to space issues"

"""The following commands are to pop one name at a time out of the Guest list
the .pop() can be used to remove a name from the list using the precise position of that name
the print statements are used to print a messsage to the name that was popped 
"""
print("\n", Guest_list)
Guest_popped1 = Guest_list.pop(0)
print(message1, Guest_popped1, message3)
Guest_popped2 = Guest_list.pop(0)
print(message1, Guest_popped2, message3)
Guest_popped3 = Guest_list.pop(1)
print(message1, Guest_popped3, message3)
Guest_popped4 = Guest_list.pop(0)
print(message1, Guest_popped4, message3)
Guest_popped5 = Guest_list.pop(-1)
print(message1, Guest_popped5, message3)
Guest_popped6 = Guest_list.pop(-1)
print(message1, Guest_popped6, message3)
"""The following list includes the names of the guest names that were popped in numerical order"""
GUESTS_POPPED = [Guest_popped1], [Guest_popped2], [Guest_popped3], [Guest_popped4], [Guest_popped5], [Guest_popped6]
print("\n", Guest_list) #'\n' here is used to print the Guest list onto a new line
print("\n", GUESTS_POPPED) #'\n' here is used to print the Guest list onto a new line
message4 = ", I'm Sorry for the delays, however happily you're still invited to the dinner"
"""The following print statements write a message to the remaining guests in the guest list to tell them that they're still ivited"""
print(message1, Guest_list[0].title(), message4) 
print(message1, Guest_list[-1].title(), message4)
"""The following commands are used to delete a name from the list
The [0] shows the precise position of the name thats being deleted in the list 
"""
del Guest_list[0] 
del Guest_list[0]
print(Guest_list) #This print statement prints the names that are in the guest list



