'''Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted.'''

#Correct password 
correct_password = int(12345)
#Maximum attemps
maximum_attempts = int(5)
#Current attemps
current_attempts = int(0)
#start password attempt loop
while current_attempts < maximum_attempts:
    try:
        #get input from user for password
        input_Password = int(input('Enter the numerical passsword here:').strip())
     #checks if password is correct
        if input_Password == correct_password :
            print(f'The password is correct',)
        #if password correct, break loop
            break
        else:
        #increments current attempts by 1
            current_attempts += 1
        #remaining attempts calculation
            remaining_attempts = maximum_attempts - current_attempts
        #print remaining attempts
            print(f'Password is incorrect, you have {remaining_attempts} remaining attempts, please try again',)

    except ValueError:
    #non numeric attempt will count as a failed attempt
        current_attempts += 1
        remaining_attempts = maximum_attempts - current_attempts
        print('INVALID INPUT, PLEASE TYPE IN A NUMERICAL PASSWORD, you have', remaining_attempts, 'attempts remaining')
        #if maximum attempts is reached print alert
    if current_attempts == maximum_attempts:
            print("YOU HAVE REACHED THE MAXIMUM ATTEMPTS, THE AUTHORITIES HAVE BEEN ALERTED ")