#Name Cases
name1 = "                    Josh                             "
print("Hello " + name1 + " would you like to play Valorant today?")
print(name1.title()) #.title() prints the name in title form where the first letter is capitalized
print(name1.lower())
print(name1.upper())
print("Hi normal",name1)
print("\n Hi left",name1.lstrip())
print("\t Hi right",name1.rstrip())
print("\n Hi all",name1.strip())





print('''Albert Einstein once said "A person who never made a 
mistake never tried anything new"''')
Author1 = "Albert Einstein "
between_A_Q = "once said "
quote1 = "A person who never made a mistake never tried anything new"
print(Author1 + between_A_Q + quote1)

Names = ['hi', 'monkey', 'kys'] #This is a list where multiple items can be stored
print(Names) #Here python will print the list Names within []
print(Names[0].title())
"""[0] tells python u want to print the 0 position in the Names list and prints it without the [], Python considers the first item in a list to be at position 0, not position 1.
The .title() prints the statement but prints it in a title format"""
print(Names[1].title())
print(Names[2].title())