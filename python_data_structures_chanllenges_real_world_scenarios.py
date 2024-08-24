'''
2. Python Data Structure Challenges in Real World Scenarios

Task 1: Library System Enhancement.
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no
duplicates.

Exhisting Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley)]

Add funcitionality to insert new books to 'library'. Ensure that adding a duplicate book is handled properly.


'''

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
new_book1 = ("The Fighters Mind", "Sam Sheridan")
new_book2 = ("Brave New World", "Aldous Huxley")

def add_book(library, book):
  if book not in library:
    library.append(book)
    print(f' Book: {book[0]} by Author: {book[1]} - Added to library')
  else:
    print(f' Book: {book[0]} by Author: {book[1]} - Already in the library') 
    
     
add_book(library, new_book1)
add_book(library, new_book2)
print(library)