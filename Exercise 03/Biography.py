"""Exercise 3: Biography - 25 Marks
In this exercise, you’ll create a program that stores and prints your name, hometown,
and age to the console using a Python dictionary.
Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
"""

info = {"Name" : "Taher Abdalla",
        "Hometown": "Sharjah",
        "age": "17"}
#this print statement prints the variables above on multiple lines using '\n', and string concatenation
print(f"Name: {info['Name']}\nHometown: {info['Hometown']}\nAge: {info['age']}")
#The variable age has been converted into a string as string concatenation cannot be used with integar values