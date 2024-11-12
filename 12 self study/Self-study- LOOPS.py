person = ['mk', 'boko', 'shakir']
for name in person: #This is called a loop which tells python to pull a name from the person list and associate it with the vairable name, 
 #each line that is indented will be considered within the loop
 print(name)

Guest_list = ['Mk', 'Josh', 'Shakir', 'Boko', 'Yasin'] #This is a list including many names
message1 = 'Hello'
message2 = 'how are you doing today?, im inviting u to my dinner party'
for Guest in Guest_list:#This is called a loop which tells python to pull a name from the person list and associate it with the vairable name, 
 #each line that is indented will be considered within the loop
    print(message1, Guest.title() , message2)
    print(f'I cant wait to see you at the dinner', Guest.title(),'.\n')
print("Cant wait to see you guys")