#Exercise 4: Primitive Quiz
"""Exercise 4: Primitive Quiz - 30 Marks
In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.
"""
# The answer to the question for this exercise starts here:

#input method is used here to ask for user input regarding the question, \n is used to create a new line before the question
Capital_France = input('\nWhat is the capital of France? ') 
#if statement is used here to compare if user input is equal to the variables value or not
if Capital_France.strip().title() == 'Paris':
#if it is equal to the variables value; it will print the following statement:
        print(f'Correct the answer is',Capital_France.strip().title(), "!!!")
#if it's not equal,the following statement will be printed:
else: 
        print(f"Your answer is incorrect")
        
        
        
