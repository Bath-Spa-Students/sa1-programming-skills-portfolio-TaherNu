"""Exercise 3: Biography - 25 Marks
In this exercise, you’ll create a program that stores and prints your name, hometown,
and age to the console using a Python dictionary.
Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
"""
#This name variable is associated with a string value data type
name = str('Taher Abdalla')
#This hometown variable is associated with a string value data type
hometown = str('Sharjah')
#This age variable is associated with an integar value data type
age = int(17)
#this print statement prints the variables above on multiple lines using '\n', and string concatenation
print(f"Name: " + name.title() + '\n' + "Hometown: " + hometown.title() + "\n" + 'Age:' + str(age))
#The variable age has been converted into a string as string concatenation cannot be used with integar values