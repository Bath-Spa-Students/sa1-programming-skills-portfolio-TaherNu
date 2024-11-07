'''Exercise 5: Days of the Month - 30 Marks
Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month.
Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers
and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month.'''
#Answer to Exercise 5: Days of the Month :

# this is a dictionary storing the month numbers and the number of days within each one
days_of_month = {1: 31, 
                 2: 28,
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31} 
#This is an integer variable which asks the user what month number they want
month = int(input('Month number? ')) 
#This if statement checks if the number inputted is less than 1 or more than 12
if month < 1 or month > 12:
#if the number inputted is less than 1 or more than 12 the following message is printed
    print('this number of month is invalid, enter a number between 1 and 12')
else:
#If the number inputted is not less than 1 or more than 12 the following is printed
    print(f'month number ', month , 'has', days_of_month[month], 'days')
"""this print statement finds the number inputted and prints it 
then finds its corresponding days of the month in the dictionary and prints it"""
