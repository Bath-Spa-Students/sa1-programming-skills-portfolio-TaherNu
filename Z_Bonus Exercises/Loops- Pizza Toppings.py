"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, Print a message saying you'll add that topping to their pizza."""
'''Answer for exercise: '''

#message to user
print('Your order will start now, type "Quit" to finish your order')
#loop starts
while True:
    #asks user for toppings
    pizza_toppings = input("Enter the toppings you want for your pizza here: ")
    #if quit is inputted, break loop
    if pizza_toppings.title().strip() == "Quit":
        break
    #continue loop until broken
    else:
        print(f'{pizza_toppings.title().strip()} will be added to your pizza')

    