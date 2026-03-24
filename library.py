#Develop a library class that has instance variables book_name,author,availability status. 
#The class should provide methods to check out a book, return a book and display available books.
#Use the __init__constructor.
class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print("You have checked out:", self.book_name, "by", self.author)
        else:
            print("Sorry,", self.book_name, "is not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("You have returned:", self.book_name)
        else:
            print(self.book_name, "was not checked out.")

    def display_info(self):
        status = "Available" if self.available else "Checked Out"
        print("Book:", self.book_name, "| Author:", self.author, "| Status:", status)

Book1= Library("Matilda","Roald Dahl",True)
Book1.check_out()
Book1.return_book()
Book1.display_info()