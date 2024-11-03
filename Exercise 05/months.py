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
month = int(input('Month number? ')) 
if month < 1 or month > 12:
    print('this number of month is invalid, enter a number between 1 and 12')
else:
    print(f'month', month , 'has ', days_of_month[month], 'days')

