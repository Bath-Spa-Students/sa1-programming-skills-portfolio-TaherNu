'''Use your newly acquired knowledge of the for loop to complete the following
tasks. Print all values to the console in each case. 
* Write a loop that counts up from 0 to 50 in increments of 1. 
* Write a loop that counts down from 50 to 0 in decrements of 1. 
* Write a loop that counts up from 30 to 50 in increments of 1. 
* Write a loop that counts down from 50 to 10 in decrements of 2. 
* Write a loop that counts up from 100 to 200 in increments of 5. 
You may include all loops in a single project'''.

#This is a list comprehension where a loop starts counting from 0 and stops when it reaches 51 in increments of 1
loop1 = [value for value in range(0, 51, 1)]
#This is a print statement that prints the loop above on a new line
print(f'\n',loop1)

#This is a list comprehension where a loop starts counting from 50 and stops when it reaches -1 in decrements of 1
loop2 = [value for value in range(50, -1, -1)]
print(f'\n',loop2)

#This is a list comprehension where a loop starts counting from 30 and stops when it reaches 51 in increments of 1
loop3 = [value for value in range(30, 51, 1)]
print(f'\n',loop3)

#This is a list comprehension where a loop starts counting from 50 and stops when it reaches 9 in decrements of 2
loop4 = [value for value in range(50, 9, -2)]
print(f'\n',loop4)

#This is a list comprehension where a loop starts counting from 100 and stops when it reaches 201 in increments of 5
loop5 = [value for value in range(100, 201, 5)]
print(f'\n',loop5)
