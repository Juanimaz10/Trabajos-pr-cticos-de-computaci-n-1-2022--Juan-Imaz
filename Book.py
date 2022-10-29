class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price


    def __str__(self):
        return "------------------------\n          Book\n------------------------" \
               "\nTitle: {} \nAuthor: {} \nPrice: {}\n------------------------" \
            .format(self.title, self.author, self.price)
