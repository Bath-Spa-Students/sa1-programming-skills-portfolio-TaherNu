"""Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions
outlined below:
Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function."""

def even_odd(Number):
    """This function checks if the number is odd or even"""
    if Number % 2 == 0:
        return(f'The value {Number} is even')
    else:
        return(f'The value {Number} is odd')

def main_function():
    try:
        #Asks for input and stores it as an integar
        Number = int(input('please type in your value here: '))
        #calls even_odd function to check if number is odd or even
        result = even_odd(Number)
        #prints result
        print(result)
    except ValueError:
        #non-integar input will show an error message
        print(' ERROR. please enter an integer')
#runs main_function
main_function()
    
    