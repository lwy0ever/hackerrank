

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price = price
    def display(self):
        #super().display()
        print('Title: %s' % (self.title))
        print('Author: %s' % (self.author))
        print('Price: %d' % (self.price))

