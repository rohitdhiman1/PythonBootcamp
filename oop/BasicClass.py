#self refers to the object. In python, object is passed to the constructor.
#Most of the programmers use self as the name of the object. It can be anything !
#You can even use your name instead of self.
#Point to be noted here is -> the first argument to the constructor is the object.

class Book:

    #class level attributes. Shared across all the objects.
    book_types = ['hardcover','paperback','ebook']

    #Double underscore makes a variable private
    __booklist = []

    @staticmethod
    def get_book_list():
        return Book.__booklist

    @classmethod
    def get_book_types(cls):
        #here cls is a class instance not an object instance
        return cls.book_types

    def __init__(self,title,author, publication,price,booktype):
        #instance variables
        self.title = title
        self.author = author
        self.publication = publication
        self.price = price
        self.__somePrivateVariable = "cjdbicdbcwd"
        if booktype.lower() not in Book.book_types:
            raise ValueError(booktype + " not a valid book type")
        else:
            self.booktype = booktype

    #instance methods
    def return_price(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)/100
        else:
            return self.price

    def set_discount(self, discount_percent):
        self._discount = discount_percent
        #Single preceeding underscore is intended to be used only by the class

#Object creation and instance method use.
b1 = Book("The alchemist", "Paulo Coelho","ABC Publications",500,"paperback")
b1.set_discount(10)
print(b1.return_price())
b2 = Book("Second book", "Some author","DFE Publications",200,"hardcover")
b2.set_discount(10)
print(b2.return_price())


#Static method use
Book.get_book_list().append(b1)
Book.get_book_list().append(b2)
print(Book.get_book_list())

'''
print(Book.return_price())
The above line would not work because  return_price() is an instance/object method ,not a class method
'''

'''
print(b1.get_book_types())
Note that the above line would work as an object can use an instance method.
But this is not an ideal way of calling a class method
The correct way of calling a class method ->  print(Book.get_book_types())
'''

'''
print(b1.__somePrivateVariable)   -> Error
If you try to access an instance variable (starting with double underscore), you'll run into error

print(b1._Book__somePrivateVariable)   -> No Error. But, it is discouraged to access private variable outside the class.
Python appends class name in front of these variables so that child classes cannot use these variables.


'''
