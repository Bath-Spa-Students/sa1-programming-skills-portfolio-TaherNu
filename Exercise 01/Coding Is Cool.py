'''Exercise 1: Coding is Cool- 10 Marks
Fill in the blanks in the Python code below to output the phrase “Coding is
Cool” to the console using variables and string concatenation.'''

#Answer to Exercise 1 - Coding Is Cool:
word1 = str("cod" + "ing ") 
'''The Variable word1 has a string value asssigned to it, The Variable has 2 strings in the 
same Variable,This is known as string concatenation'''
word2 = str("i" + "s ") #this is string concatenation which allows you to combine 2 or more strings in one string line
word3 = str("cool") 
print(str(word1.title()) + str(word2) + str(word3.title())) 
'''string concatenation is also used here in this statement by the + operater which allows 
more than 1 string to be in the same line
str() makes sure that whatever is written within its parentisis is in string data type
.title() allows whatever is in the Variable to be in title form where the first letter is capitalized'''