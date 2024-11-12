Pizzas = ['chicken BBQ pizza', 'chicken ranch pizza', 'pepperoni pizza']
msg1 = 'I like'
for pizza in Pizzas:
    print(msg1, pizza.title(), '\n')
print("I LOVE PIZZA"'\n')

Animals = ['rabbit', 'cat', 'dog']
message1 = 'A'
message2 = 'would make for a great pet'
for Animal in Animals: #This is called a loop which tells python to pull a animal from the Animals list and associate it with the vairable Animal, 
 #each line that is indented will be considered within the loop
    print(message1, Animal.title(), message2, '\n')
print('These animals are mostly friendly towards humans')

Numbers = list(range(0,6)) 
"""list() converts the numbers generated within the range() function into a list
Pythons range function allows you to generate a series of numbers
The range(0,6) will generate numbers from 0 all the way to 5 and not 6
The range() function causes Python to start counting at the first value you give it, 
and it stops when it reaches the second value you provide.
Because it stops at that second value, the output never contains the end
value, which would have been 6 in this case."""
print(Numbers)

odd_numbers = list(range(2,15,3)) 
"""the range() function here starts with the value 2 and then
adds 3 to that value. It adds 3 repeatedly until it reaches or passes the end
value, 15"""
print(odd_numbers)
square_numbers = [] #This is an empty list called square_numbers
for value in range(1,11): #this is a loop which creates a variable called value and gives it a range from 1 to 11
   square_numbers.append(value ** 2) #This line adds the variable value squared into the list square_numbers. it does this for each value created from 1 to 11
print(square_numbers)

print(min(square_numbers)) # finds the minimum number from the square_numbers list
print(max(square_numbers)) #finds the maximum number from the square_numbers list
print(sum(square_numbers)) #finds the sum of all the numbers in the square_numbers list


square = [values**2 for values in range(0,20) ] 
""" This is called list comprehension where u can generate multiple numbers and values within one line of code instead of many 
first we create a list called square
then make a varuable within the list called values which will be ** (squared)
then create a loop for the values squared with any of the values generated in that range 
"""
print(square)
