
class Publication:
    def __init__(self,title,price):
        self.title = title
        self.price = price

class Periodical(Publication):
    __someprivatevariable = "bwdccwdncwd"
    def __init__(self,title,price, period, publisher):
        super().__init__(title,price)
        self.period = period
        self.publisher = publisher

#Book class extends Publication class
class Book(Publication):
    def __init__(self,title,author,price,pages):
        super().__init__(title,price)
        self.author = author
        self.pages = pages

#Newspaper extends Periodical class
class Newspaper(Periodical):
    def __init__(self,title,price,period,publisher):
        super().__init__(title,price,period,publisher)

#Magazine extends Periodical class
class Magazine(Periodical):
    def __init__(self,title,price,period,publisher):
        super().__init__(title,price,period,publisher)


b1 = Book('The Alchemist','Paulo Coelho',50,300)
n1 = Newspaper('The Tribune',4,2012,'Tribune')
m1 = Magazine('Forbes',30,2020,'Forbes Inc')

print("============Book===========")
print(b1.title)
print(b1.author)
print(b1.price)
print(b1.author)

print("=============Newspaper============")
print(n1.title)
print(n1.publisher)
print(n1.price)
print(n1.period)

print("=============Magazine============")
print(m1.title)
print(m1.publisher)
print(m1.price)
print(m1.period)


