'''Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly.'''
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
#days in february for leap year
leap_Year_days = 29
#Variable asks user for month number
month = int(input('Month number?')) 
#if statement to check if number is valid
if month < 1 or month > 12:
    #if invalid and error message is printed
    print('this number of month is invalid, enter a number between 1 and 12')
else: 
    #if month is 2 
    if month == 2:
        #asks if its leap year or no
        year = str(input('Is it a leap year? '))
        if year.strip().lower() == "yes":
        #if yes print leap month and days
            print('Month', month, 'has', leap_Year_days)
        elif year.strip().lower() == "no":
        # if no, print month and days
            print(f'Month', month, 'has', days_of_month[month], 'days')
    #else statement
    else: 
            print(f'Month', month , 'has', days_of_month[month], 'days')
        #prints the month number and the days
    
