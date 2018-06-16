"""Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger 
which is inheriting Animal and access the base class method."""
class animal():
    def animal_attribute(self,leg):
        self.leg=leg
        print(leg)

class tiger(animal):
    def __init__(self):
        print("object of tiger made!!")

obj=tiger()
obj.animal_attribute(4)  #base class method is called using the child class object

""" Q.2- What will be the output of following code.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()
"""
print("A B\nA B")


"""Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
 Define methods to add, display and update the following details. Create another class 
 Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop 
 and access methods of base class to get information for a particular cop and make it available for mission.
"""
class Cop():
    def add(self):
        name=input(("enter name:"))
        self.name=name
        age=input("enter the age:")
        self.age=age
        work=input("enter the work:")
        self.work=work
        exper=input("enter the experience:")
        self.exper=exper
         
    def display(self):
        print("name:%s\nage:%s\nwork:%s\nexperience:%s"%(self.name,self.age,self.work,self.exper))
    
    def update(self):
        name=input(("enter new name:"))
        self.name=name
        age=input("enter the new age:")
        self.age=age
        work=input("enter the new work:")
        self.work=work
        exper=input("enter the new experience:")
        self.exper=exper

class Mission(Cop):
    mission=""
    def add_mission_details(self):
        self.mission=input("Enter the mission name:")
obj=Mission()
obj.add()
obj.display()
n=input("do you want to update?:(Y?N)")
if(n=="y" or n=="Y"):
    obj.update()


"""Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class
 rectangle and square which inherits shape and access the method Area."""

class Shape():
    def __init__(self,leng,bre):
        self.leng=leng
        self.bre=bre
    def area(self):
        return (self.leng)*(self.bre)
    
class rectangle(Shape):
    def __init__(self,leng,bre):
        self.leng=leng
        self.bre=bre

class square(Shape):
    def __init__(self,leng,bre):
        self.leng=leng
        self.bre=bre

obj1=rectangle(2,3)
print("area of rec:",obj1.area())

obj2=square(5,5)
print("area of square:",obj2.area())


    






