class Book():
    
    def __init__(self, name, author):
        self.name = name
        self.author = author
    
    def print_book(self):
        print(self.name + ' - ' + self.author)
        
my_book1 = Book(input(), input())
my_book1.print_book()
my_book2 = Book(input(), input())
my_book2.print_book()
my_book3 = Book(input(), input())
my_book3.print_book()
