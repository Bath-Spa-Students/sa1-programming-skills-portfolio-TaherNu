'''Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the
3
password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.'''

#Correct password
correct_password = int(12345)
#Start loop
while True:
    try:
        #ask user for password
        input_Password = int(input('Enter the numerical passsword here:').strip())
        #check if it's correct
        if input_Password == correct_password :
            print(f'The password is correct',)
            #exit loop if password is correct
            break 
        # if password incorrect, try again
        elif input_Password != correct_password:
            print(f'Password is incorrect, please try again',)
    #non numeric password will be invalid
    except ValueError:
        print('INVALID INPUT, PLEASE TYPE IN A NUMERICAL PASSWORD')

    