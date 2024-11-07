#Exercise 4: Primitive Quiz
"""
Advanced Requirements:.
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question.
"""
# The answer to the question for this exercise starts here:

#input method is used here to ask for user input regarding the question, \n is used to create a new line before the question
Capital_France = input('\nWhat is the capital of France? ') 
#if statement is used here to compare if user input is equal to the variables value or not
if Capital_France.strip().title() == 'Paris':
#if it is equal to the variables value; it will print the following statement:
        print(f'Correct the answer is',Capital_France.strip().title(), "!!!")
#if not it will print the following statement:
else: 
        print(f"Your answer is incorrect")

Capital_germany = input('\nWhat is the capital of Germany? ')
if Capital_germany.strip().lower() == 'berlin':
        print(f'Correct the answer is',Capital_germany.strip().title(), '!!!')
else: 
        print(f"You're answer is incorrect")

Switzerland_Capital = input("\nWhat is the capital of Switzerland? ")
if Switzerland_Capital.strip().upper() == "BERN" :
        print(f'Correct the capital of Switzerland is', Switzerland_Capital.strip().title(), '!!!')
else :
        print(f"Your answer is incorrect")

Capital_Netherlands = input('\nWhat is the capital of Netherlands? ')
if Capital_Netherlands.strip().title() == 'Amsterdam' :
        print(f'Correct the capital of Netherlands is', Capital_Netherlands.strip().title(), '!!!')
else:
        print(f'Your answer is incorrect')

Capital_Ukraine = input("\nWhat is the capital of Ukraine? ")
if Capital_Ukraine.strip().title() == 'Kiev' or 'Kyiv' :
        print(f"correct the answer is", Capital_Ukraine.strip().title(), '!!!')
else:
        print(f'The answer is incorrect')

Capital_Portugal = input('\nWhat is the capital of Portugal? ')
if Capital_Portugal.strip().title() == 'Lisbon' :
        print(f'Correct the capial of portugal is ', Capital_Portugal.strip().title(), '!!!')
else:
        print(f'Your answer is incorrect')

Capital_Malta = input('\n What is the capital of Malta? ')
if Capital_Malta.strip().title() == 'Valleta' :
        print(f'Your answer is correct, The capital of Malta is ', Capital_Malta.strip().title(), '!!!')
else: 
        print(f"Your answer is incorrect ")
        
Capital_Türkiye = input('What is the capital of Türkiye? ')
if Capital_Türkiye.strip().title() == 'Ankara' :
        print(f'Correct the capital of Türkiye is ', Capital_Türkiye.strip().title(), '!!!')
else: 
        print(f'Your answer is incorrect')

Capital_Romania = input('\nWhat is the capital of Romania? ')
if Capital_Romania == 'Bucharest' :
        print(f"Correct the capital of Romania is ", Capital_Romania.strip().title(), '!!!')
else:
        print(f'Your answer is incorrect')

Capital_Georgia = input('What is the capital of Georgia? ')
if Capital_germany.strip().title() == 'Atlanta' :
        print('correct the capital of Gerogia is ', Capital_Georgia.strip().title(), '!!!')
else:
        print('Your answer is incorrect')
        
