"""Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as One of my favorite books is Alice in Wonderland. 
Call the function, making sure to include a book title as an argument in the function call."""

def fav_book(book):
    print(f"My favourite book series is {book.title().strip()}, it's a really good book series")

fav_book('Diary of a wimpy kid')