'''
In composition, we build objects out of other objects.
HAS-A relationship implementation.
'''

class Book:
    def __init__(self,title, price, author = None):
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    def add_chapter(self,chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result =0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Author:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return self.fname + " " + self.lname

class Chapter:
    def __init__(self,name, pagecount):
        self.pagecount = pagecount
        self.name = name


a1 = Author("Charles","Dickens")
b1 = Book("Christmas Carol",321,a1)

ch1 = Chapter("Chapter 1", 200)
ch2 = Chapter("Chapter 2", 100)
ch3 = Chapter("Chapter 3", 400)

b1.add_chapter(ch1)
b1.add_chapter(ch2)
b1.add_chapter(ch3)

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())