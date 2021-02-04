#!/usr/bin/env python
# coding: utf-8

# ## Inheritance

# In[2]:


# Come up with an example of Single Inheritance.
class Flower:
    def brandname(self):
        return "This is a Flower Brand"

class Jasmine(Flower):
    def flowername(self):
        return "This is a Jasmine Flower"
    
J1 = Jasmine()
print(J1.flowername())
J1.brandname()


# In[16]:


class Product:
    def Product_name(self):
        return "Product name is noodles"

class Maggie(Product):
    def noodles(self):
        return "Noodles name is Maggie"
    
maggie1 = Maggie()
print(maggie1.Product_name(),maggie1.noodles())


# In[12]:


# Come up with an example for Multiple Inheritance using Maruti, Suzuki, and theircollaboration marutisuzuki
# Multiple Inheritance
class Maruti:
    def brandname(self):
        return "This is Maruti"
class Suzuki:
    def sbrandname(self):
        return "This is Suzuki"
class MarutiSuzuki(Maruti,Suzuki):
    def name(self):
        return "This is a Maruti Suzuki"
car1 = MarutiSuzuki()
print("Child Class:-",car1.name())
print("Parent Class1:-",car1.brandname())
print("Parent Class2:-",car1.sbrandname())


# In[18]:


# Multiple Inheritance
class Maruti:
    def mName(self):
        return "Was an Indian Company and was known as Maruti Udyog before"
class Suzuki:
    def sName(self):
        return "Was an Japan Company and was known as Suzuki Motor Corporation"
class MarutiSuzuki(Maruti,Suzuki):
    def msName(self):
        return "Now known as Maruti Suzuki"
ob = MarutiSuzuki()
print(ob.mName())
print(ob.sName())
print(ob.msName())


# In[10]:


# Multiple Inheritance
class Parent1:
    def func1(self):
        print("This is function1")
class Parent2:
    def func3(self):
        print("This is function3")
class Child(Parent1,Parent2):
    def func2(self):
        print("this is function2")
Obj = Child()
Obj.func1()
Obj.func2()
Obj.func3()
    


# In[9]:


# Come up with an example for Multilevel Inheritance of your choice.

class Nehru:
    def Fgen(self):
        return "This is First Generation"
    
    
class RajivGandhi(Nehru):
    def Sgen(self):
        return "This is Second Generation"
    

class RahulGandhi(RajivGandhi):
    def Tgen(self):
        return "This is Third Generation"


Congress = RahulGandhi()
print ("Latest Gen:-",Congress.Tgen())
print ("Property of second Class:-",Congress.Sgen())
print ("Property of First Class:-",Congress.Fgen())


# In[58]:


# Multilevel Inheritance
class Animal:
    def eat(self):
        print("Eating...")
class Dog(Animal):
    def bark(self):
        print("Barking...")
class BabyDog(Dog):
    def weep(self):
        print("Weeping...")
d = BabyDog()
d.eat()
d.bark()
d.weep()


# In[ ]:


# Multilevel Inheritance - In this type of Inheritance, a derived class is created from another deived class.
# Hierachical Inheritance - In this type of Inheritance, more than one subclass is inherited from a single base class.


# In[ ]:


# When a child is inheriting properties from mother and father both we can called as multiple inheritance.
- child(mother,father)


# In[11]:


# When a child inherits the properties from parent as well as grandparent then we can called as multilevel inheritance.
- grandparent
- parent(grandparent)
- child(parent


# In[22]:


# Hierarchical Inheritance 
class Course_PCDS:
    def course_name(self):
        return "From PCDS Course"
class Data_Analyst(Course_PCDS):
    def jobrole1(self):
        return "Data Analyst Role"
class Data_Engineer(Course_PCDS):
    def jobrole2(self):
        return "Data Engineer Role"
job1 = Data_Analyst()
print(job1.course_name(),job1.jobrole1())
job2 = Data_Engineer()
print(job2.course_name(),job2.jobrole2())


# In[34]:


# Example of Hirarchical Inheritance 

class Ambani:
    def sname(self):
        return "Ambani"
    
    
class Mukesh(Ambani):
    def Fname(self):
        return "This is Mukesh"
    

class Anil(Ambani):
    def Fname(self):
        return "This is Anil"


a1 = Mukesh()
a2 = Anil()
print ("Ambani's First son:-",a1.Fname(),a1.sname())
print ("Ambani's Second son:-",a2.Fname(),a2.sname())


# In[24]:


# Hybrid Inheritance
# Python program to demonstrate 
# hybrid inheritance 

class School: 
     def func1(self): 
        print("This function is in school.") 

class Student1(School): 
     def func2(self): 
        print("This function is in student 1. ") 

class Student2(School): 
     def func3(self): 
        print("This function is in student 2.") 

class Student3(Student1, Student2): 
     def func4(self): 
        print("This function is in student 3.") 
        
# Driver's code 
object = Student3() 
object.func1() 
object.func2()


# In[35]:


# Hybrid Inheritance

class Ambani:
    def sname(self):
        return "Ambani"
    
    
class Mukesh(Ambani):
    def Mname(self):
        return "This is Mukesh"
    

class Anil(Ambani):
    def Aname(self):
        return "This is Anil"


class Maruti(Mukesh,Anil):
    def brandname(self):
        return "Thanks for using Maruti car"
    
    
car1 = Maruti()
print ("customer1:-",car1.Mname(),car1.sname(),car1.brandname())
print ("customer1:-",car1.Aname(),car1.sname(),car1.brandname())


# In[36]:


# Hybrid Inheritance

class Course_PCDS:
    def course_name(self):
        return ' From PCDS course you may get a '
    
class Data_analyst(Course_PCDS):
    def jobrole1(self):
        return 'Data Analyst role.'
    
class Data_engineer(Course_PCDS): 
    def jobrole2(self):
        return 'Data Engineer role.'
    
class ArtificialIntelligence(Data_analyst,Data_engineer):
    def skillset1(self):
        return 'machine learning'
    def skillset2(self):
        return 'Deep learning'

hybrid1 =ArtificialIntelligence()
print(hybrid1.course_name(),hybrid1.jobrole1(),hybrid1.jobrole2(),hybrid1.skillset1(),hybrid1.skillset2())


# In[2]:


# Hybrid Inheritance

class Species:
    def func1(self):
        print("The function is for living things")
        
class Plants(Species):
    def func2(self):
        print("The function is in Plant, which can't move") 
        
class Animals(Species):
    def func3(self):
        print("The function is in Animals, which can move around") 
        
class Trees(Plants):
    def func4(self):
        print("The function is in Trees , which are big plants") 
        
class Dogs(Animals):
    def func5(self):
        print("The function is in Dogs , which  can move and bark") 

class Human(Species):
    def func6(self):
        print("The function is in Human  , who are intelligent")
        


# In[37]:


# example of Hybrid Inheritance

class TataSons:
    def parent(self):
        return "The company belongs to Tata Sons"
    
class Tatamotor(TataSons):
    def sisconcern(self):
        return "Tata Motor is subsidiary of Tata Sons"
    
class Jaguar(Tatamotor):
    def prmseg(self):
        return " This is premium segment of Tata Motor"
    
class Ford(Tatamotor):
    def ecoseg(self):
        return "This is mid segment of Tata Motor"
    
class car(Jaguar, Ford):
    def brand(self):
        return "This is either from Jaguar or Ford"
    

Car1 = car()
print(Car1.brand())
print(Car1.sisconcern())


# # Polymorphism : Poly - Many, Morphism - Forms

# In[25]:


# Addition of numbers
a = 2
b = 3
a + b


# In[26]:


# Concatanaion of strings
A = "Jyoti"
B = "Sabarad"
A + B


# In[29]:


# Create a class of Humans create a method to find the number of legs for humans i.e. 2
# Create another class of animals and create a method with the name as in the previous class to find the number of legs i.e. 4
# Now create an instance of humans and find the number of legs using the method that we defined.
# Now create an instance of animals and the number of legs using the method that we defined.


class Human():
    def legs(self):
        return 2
    
class Animals():
    def legs(self):
        return 4
    

H1 = Human()
print ("Humans Legs",H1.legs())

A1 = Animals()
print ("Animals Legs",A1.legs())


# In[56]:


class Humans:
    def number_of_legs(self):
        return("The number of legs for Humans is 2") 
    
class Animals:
    def number_of_legs(self):
        return("The number of legs for Animals is 4") 
    
Humans1 = Humans()
print("Humans1.number_of_legs())
Animals1 = Animals()
print("Animals1.number_of_legs())


# In[30]:


# create a class of squares and define a method whose name is Area to find out the area of the square

# create a class of rectangles and define a method with the same name Area to find out the area of the rectangle 

# then create an instance of square and find the area create an instance of rectangle and find the area

class Square:
    def area(self, height):
        return height * height
class Rectangle:
    def area(self, height, width):
        return height * width
height = 4
width = 5
ob1 = Square()
print("Area of square is ", ob1.area(height))
ob2 = Rectangle()
print("Area of rectangle is ", ob2.area(height, width))


# In[57]:


class Square:
    def area(self, a):
        return a * a
class Rectangle:
    def area(self, length, width):
        return length * width
shape1 = Square()
print("Area of square : {}".format(shape1.area(10)))
shape2 = Rectangle()
print("Area of rectangle is : {}".format(shape2.area(10,20)))


# In[31]:


class Squares:
    def __init__(self,a):
        self.a = a
        
    def area(self):
        return (self.a*self.a)
    
class Rectangles:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def area(self):
        return (self.a*self.b)
    
    
s1 = Squares(4)
print ("Area of Square",s1.area())

r1 = Rectangles(4,6)
print ("Area of Rectangles",r1.area())


# ### Polymorphism and Inheritance
# - Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.
# 
# - Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.
# 
# - Let's look at an example:
# 

# ### Super Function
# - super() directly calls the parent class method
# 
# ### Definition and Usage
# - The super() function is used to give access to methods and properties of a parent or sibling class.
# 
# - The super() function returns an object that represents the parent class.
# 
# - No need to pass any parameters

# In[1]:


# Super Function

class Parent:
    def func1(self):
        print("This is function1")

class Child(Parent):
    def func2(self):
        super().func1()
        print("This is function2")
        
obj = Child()
obj.func2()


# In[33]:


# Super Function

class DataFolkz:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)

class Learner(DataFolkz):
    def __init__(self, txt):
        super().__init__(txt)

x = Learner("Hello, and welcome to DataFolkz")

x.printmessage()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




