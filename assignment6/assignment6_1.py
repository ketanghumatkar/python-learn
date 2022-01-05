# #
# 
# 1.Write a program which contains one class named as BookStore.
# BookStore class contains two instance variables as Name ,Author.
# That class contains one class variable as NoOfBooks which is initialise to 0.
# There is one instance methods of class as Display which displays name , Author and number of
# books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.
# After creating the class create the two objects of BookStore class as
# Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
# Obj1.Display() # Linux System Programming by Robert Love. No of books : 1
# Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
# Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2
# 
# #

class Book:
  def __init__(self, name, author):
    self.name = name
    self.author = author

class BookStore:
  NO_OF_BOOKS = 0;

  def __init__(self, name, author):
    self.book = Book(name, author)
    BookStore.NO_OF_BOOKS = BookStore.NO_OF_BOOKS + 1

  def display(self):
    print("Name of Book: ", self.book.name)
    print("Author of Book: ", self.book.author)
    print("Number of Books: ", BookStore.NO_OF_BOOKS)
  
def main():

  print("Enter book details")
  print("Tell me book name: ")
  book_name = input()
  print("Tell me book author: ")
  book_author = input()

  bs1 = BookStore(book_name, book_author)
  bs1.display()

  print("Enter book details")
  print("Tell me book name: ")
  book_name = input()
  print("Tell me book author: ")
  book_author = input()

  bs2 = BookStore(book_name, book_author)
  bs2.display()

if __name__ == "__main__":
  main()