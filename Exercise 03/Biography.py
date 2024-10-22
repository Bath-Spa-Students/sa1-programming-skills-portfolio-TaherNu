First_Name = str(input ("First Name: ")) #This is a String Variable with an input function which asks the User for their First Name
Hometown = str(input ("Hometown: "))    #This is a String Variable with an input function which asks the user for their Hometown
Age = int(input ("Age: ")) #This is an Integer Variable with an input function which asks the user for their Age
User_Details = First_Name + Hometown,  str(Age) 
'''This is a String Variable that contains the Variables for the User input details
The Integer Variable Age was converted to string in this statement as integers cannot be added with strings'''

print(f"User First Name: " + First_Name + "\n" +
      "User Age: " + str(Age) + "\n" +
      "User Hometown: " + Hometown ) 
'''This print statement uses string concatenation to put all the String Variables into one singular line 
The Integer Variable Age was converted to string in this statement as integers cannot be added with strings
"\n" is used to create a new line after each Variable'''
