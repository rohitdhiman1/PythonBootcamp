#Python is a dynamically typed language - we need not to specify variable datatype while creating a variable.

a = 100
#This will create an integer object with value 100 and assign variable a to point to that object.

print(type(a))
#this will print the class of the object which is referenced by variable a

b = a
#Assignment operator
#A new refrence  'a' will be made to point same object that a points.
#One way to verify is by checking the id of the 2 variables
print("id of a : " + str(id(a)))
print("id of b : " + str(id(b)))

b =200
#Now a new integer object with value 200 will be created and b becomes a refrence to it.

b ="abc"
'''
There is no loger a reference to integer object of value 100. It is orphaned and there is no way to access it.
When the number of references to an object drops to zero, it is no longer accessible.At that point, its lifetime is over.
Python will eventually notice that it is inaccessible and reclaim the allocated memory so it can be used for something else.
'''

#Delete a variable
del b

#print(b) will throw error
#After deletion of a variable, we cannot access it.

'''
Local Variable
Local variables are the variables that declared inside the function and have scope within the function. Let's understand the following example.
'''

def test_func1():
    #defining local variables
    x = 10
    y =100
    z = x+y
    print("z : " + str(z))

test_func1()

#print(z) would throw error as z is a local variable to function test_func1


'''
Global Variables
Global variables can be used throughout the program, and its scope is in the entire program. 
We can use global variables inside or outside the function.
'''

def test_func2():
    #explicitly mentioning t as a global variable
    global t
    t = 47


#below line will have global scope
t = 65

test_func2()
print("t : " + str(t))
#Note that the value of variable t has been overwritten since the scope was global in the function test_func2



