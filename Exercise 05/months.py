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

#Dictionary of month numbers and month days
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
#Variable asks user for month number
month = int(input('Month number? ')) 
#if statement to check if number is valid
if month < 1 or month > 12:
#if invalid and error message is printed
    print('this number of month is invalid, enter a number between 1 and 12')
else:
#else statement
    print(f'month number ', month , 'has', days_of_month[month], 'days')
#prints the month number and the days

