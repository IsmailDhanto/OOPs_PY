# class Computer :
#     def config(self):
#         print("hello ismail")


# name = Computer()

# # Computer.config(name)

# name.config()



#the __init__ method in python:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def attributes(self):
#         print("My name is ",  self.name , "and my age is ",  self.age)



# P1 = Person("Ismail", 25 )

# P1.attributes()


# the Construct method:


class Construct:
    def __init__(self):
        self.name = "Ismail"
        self.age = 25


    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            print("The two objects are equal")
        else:
            print("The two objects are not equal")


c1 = Construct()
c2 = Construct()

if c1.compare(c2):
    print("The two objects are equal")

c1.name = "ilyas"
c1.age =26





    


