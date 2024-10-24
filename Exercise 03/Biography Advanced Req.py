"""Exercise 3 - Biography
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?"""
#Answer to Exercise 3: Biography Advanced Requirements 

#This is a String Variable with an input function which asks the User for their First Name
First_Name = str(input ("First Name: "))
#This is a String Variable with an input function which asks the user for their Hometown 
Hometown = str(input ("Hometown: "))
 #This is an Integer Variable with an input function which asks the user for their Age
Age = int(input ("Age: "))
#The Integer Variable Age was converted to string here as string concatenation cannot be used with integars 
print(f"User First Name: " + First_Name.strip().title() + "\n" +
      "User Age: " + str(Age).strip() + "\n" +
      "User Hometown: " + Hometown.strip().title() ) 
'''This print statement uses string concatenation to put all the String Variables into one singular line 
"\n" is used to create a new line after each Variable'''
