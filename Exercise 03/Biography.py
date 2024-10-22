"""Exercise 3: Biography - 25 Marks
In this exercise, you’ll create a program that stores and prints your name, hometown,
and age to the console using a Python dictionary.
Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?"""
#Answer to Exercise 3: Biography

#This is a String Variable with an input function which asks the User for their First Name
First_Name = str(input ("First Name: "))
#This is a String Variable with an input function which asks the user for their Hometown 
Hometown = str(input ("Hometown: "))
 #This is an Integer Variable with an input function which asks the user for their Age
Age = int(input ("Age: "))

print(f"User First Name: " + First_Name + "\n" +
      "User Age: " + str(Age) + "\n" +
      "User Hometown: " + Hometown ) 
'''This print statement uses string concatenation to put all the String Variables into one singular line 
The Integer Variable Age was converted to string in this statement as integers cannot be added with strings
"\n" is used to create a new line after each Variable'''
