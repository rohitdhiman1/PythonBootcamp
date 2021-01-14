'''
Unlike Java, Python lets you define classes that can inherit from more than one base class.
This is called Multiple inheritance.

In this example, we have 3 classes A,B,C
class C inherits from class A and class B (in the same order)

Now, look closely at the constructors of class A and clas B
super() written in class C would call contstructor of class A -- why ?
Answer - Chek MRO. Class A is next in order resolution of class C
class C(A, B)
 |  Method resolution order:
 |      C
 |      A
 |      B
 |      builtins.object

super() written in class A wil call constructor of class B 
Since class A is not inheriting from class B, why super() written in class A is calling constrcutor of class B ?
Answer - Note that in this scenario, class A constructor was called by constrcutor of class C, since object of 
class C was created. It is the same object is being passed in the super() written in class A. 
Python gets the list returned my MRO of class C and checks the next class. In this case, next class is class B.
So, super() written in class A will carry the object of class C and call constructor of class B.

Note : if you create an object of class A, super() written in class A would not call class B 
because in the MRO of class A, class B would not be present and the object in this scenario is of class A.
'''


class A():
    def __init__(self):
        print("In A constructor")
        super().__init__()
        self.a = "Class A variable"
        self.name = "A"

class B():
    def __init__(self):
        print("In B constructor")
        #super().__init__()
        self.b = "class B variable"
        self.name = "B"

class C(A,B):
    def __init__(self):
        print("In C constructor")
        super().__init__()
        #B.__init__(self)

    def print_variables(self):
        print(self.a)
        print(self.b)
        print(self.name)


c = C()
c.print_variables()
print(C.mro())
