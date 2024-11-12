#Example of use of variables

A1 = int(16) #This shows that 16 is A1 is an integer with a value of 16

A2 = 17

A3= 17

print(int(A1)) #u can use this to get the data type of a variable





#U can also write these variables in this way
N1, N2, N3 = "MK", "Shakir", "Boko"
print(N1, "is", A1)
print(N2, "is", A2)
print(N3, "is", A3)
print(N1, N2, ", and", N3, "are bestfriends") 

Names = ["Shakir", "MK", "Boko"] #This is a collection of variables 
x, y, z = Names   # A collection of Variables can be unpacked in this way
print(x) #x = Shakir
print(y) #y = MK
print(z) #z = Boko
if 5 > 2: 
   print("5 is greater than 2!!") #The space between line 60 and 61 is called indentation which tells python that these 2 lines are part of a code without the spaces the code wouldnt work

print(type(x))
print(x, y, z, N1, N2, N3, A1, A2, A3)
print(type(x), type(y), type(z), type(N1), type(N2), type(N3), type(A1), type(A2), type(A3))

# String Concatenation (adding a string to the end of another string)
A4 = "My " + "Name " + "is " + "Taher "
print(A4)
print(type(A4))

print("My " + "Name " + "is " + "Taher ")