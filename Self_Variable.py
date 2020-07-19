'''
The instantiation operation (“calling” a class object) creates an empty object.
Many classes like to create objects with instances customized to a specific initial state.
Therefore a class may define a special method named __init__()
'''

'''
Often, the first argument of a method is called self. 
This is nothing more than a convention: the name self has absolutely no special meaning to Python.
Note, however, that by not following the convention your code may be less readable to other Python programmers,
and it is also conceivable that a class browser program might be written that relies upon such a convention.
'''

# ref: https://docs.python.org/3/tutorial/classes.html#tut-firstclasses

class food():
    # init method or constructor
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color

    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color)

apple = food("apple", "red")
grapes = food("grapes", "green")

apple.show()
grapes.show()

'''
Generally speaking, instance variables are for data unique to each instance 
and class variables are for attributes and methods shared by all instances of the class
'''
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs
print(e.kind)                  # shared by all dogs
print(d.name)                  # unique to d
print(e.name)                  # unique to e