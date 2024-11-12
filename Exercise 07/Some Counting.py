'''Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. 
* Write a loop that counts up from 0 to 50 in increments of 1. 
* Write a loop that counts down from 50 to 0 in decrements of 1. 
* Write a loop that counts up from 30 to 50 in increments of 1. 
* Write a loop that counts down from 50 to 10 in decrements of 2. 
* Write a loop that counts up from 100 to 200 in increments of 5. 
You may include all loops in a single project'''

#ANSWER:
#list comprehension generates numbers from 0-50 in increments of 1
loop1 = [value for value in range(0, 51, 1)]
#Prints generated list
print(f'\n',loop1)

#list comprehension generates numbers from 50-0 in decements of -1
loop2 = [value for value in range(50, -1, -1)]
#Prints generated list
print(f'\n',loop2)

#list comprehension generates numbers from 30-50 in increments of 1
loop3 = [value for value in range(30, 51, 1)]
#Prints generated list
print(f'\n',loop3)

#list comprehension generates numbers from 50-10 in decrements of -2
loop4 = [value for value in range(50, 9, -2)]
#Prints generated list
print(f'\n',loop4)

#list comprehension generates numbers from 100-200 in increments of 5
loop5 = [value for value in range(100, 201, 5)]
#Prints generated list
print(f'\n',loop5)
