#FUNCTIONS


#def tells python a funtion is being made
#hi is the name of the function
#() is where the information is passed
def hi():
    #this is a comment called a docstring, which describes what the function does
    '''this functions prints the message "hi"'''
    #is the only line of actual code in the body of this function, so hi() has just one job: print("hi!!").
    print('hi!!')
    
hi()

"""This function is the modified version of the one above.
it's name is 'hii'
the () stores the information 'Name'"""
def hii(Name):
    '''this function says hi to a name'''
    #This is the only line of actual code in this function, so hii() has one job: print('hi' and the 'name' being assigned in between the brackets)
    print("hi,", Name.title())
#the name being assigned here is 'maki'. when the function is called it will print hi, Maki.
#doesnt matter what name is given it will still print it
hii('maki')

#positional arguments in functions:
def describe_pet(animal_type, pet_name):
    #this prints the animal type and its name
    print("I have a", animal_type.title(), "who's name is",pet_name.title())
#the order of the arguments is very important
describe_pet('Rabbit', 'Coco')
#The function can be called as many times as you'd like
describe_pet('Dog', 'Sasha')
#THe funcation can also be called this way
describe_pet(animal_type='Rabbit', pet_name='Sasha')

#a default value can be assigned to an argument
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    #if no value is assigned to animal_type, it will use the default value which is 'dog'
describe_pet(pet_name='willie')
#if you want to assign a value to this function u will have to use this:
describe_pet(pet_name='harry', animal_type='hamster')

#Functions with optional arguments
#here middle_name is given a default value of an empty string
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
        
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker',middle_name= 'lee')
print(musician)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print('\n please type your name')
    f_name = input('type your first name: ')
    l_name = input('type your last name here: ')
    formatted_name = get_formatted_name











"""Exercise 1.1: Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly."""

def display_message():
    """ this function prints a sentence"""
    print('\ntoday we are learning about functions')
#function being called:
display_message()

"""Exercise 1.2: Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""

def favourite_book(fav_book):
    """This function prints a message"""
    print("\nMy favourite book is ", fav_book, ",you should read it")
    
#function being called:
favourite_book('Alice in Wonderland')

"""1.3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments."""

def make_shirt(shirt_size, shirt_message):
    '''This function prints a shirt size adn message '''
    print('\nThe size of your shirt is', shirt_size, 'and the message of your shirt is', shirt_message)

make_shirt('Large', 'Hiiiiiiii')
make_shirt(shirt_size= 'Large', shirt_message='Hiiiiiii')

'''1.4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt'''

def make_shirt(shirt_message, shirt_size = 'Large' ):
    '''This function prints a shirt size adn message '''
    print('\nThe size of your shirt is', shirt_size, 'and the message of your shirt is', shirt_message)
    
make_shirt('I love Python')
make_shirt('I love Python', 'Medium')

"""1.5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""

def describe_city(city_name, country_name = 'United Arab Emirates'):
    print("\n", city_name.title(), 'is in', country_name.title())
describe_city('Dubai')
describe_city(city_name= 'Reykjavik', country_name= 'iceland')
describe_city('Toronto','canada')







