class Book:
    def __init__(self,title,author,pages,price):
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price
    def discount(self):
        self.Discount="Congratulations! you have a 10% discount on this item! Your new price will be",self.price-self.price*0.1
        self.nodiscount="Sorry, no discount for this item, your price will be:",self.price
        if self.price>=100:
            return self.Discount
        else:
            return self.nodiscount
    def expensive(self):
        self.expense="This is expensive"
        self.noexpense="This is not too bad"
        if self.price>=60:
            return self.expense
        else:
            return self.noexpense
    def Overview(self):
        return self.title, self.author, self.pages, self.price
book=Book("Watership Down","Richard Adams",300,101)
print(book.expensive())
print(book.Overview())
print(book.discount())


