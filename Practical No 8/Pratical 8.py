print("Constructor and Destructor")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __del__(self):
        print("Destructor is Called")
s1 = Person("Om Raut",20)
print(s1.name)
print(s1.age)
del s1


print("\nSingle Inheritance")
class Parent():
    def fun1(self):
        print("This is Parent Class ")
class Son(Parent):
    def fun2(self):
        print("This is Son Class")
sn = Son()
sn.fun1()
sn.fun2()


print("\nMultiple Inheritance")
class Father:
    def skill(self):
        print("Father's skill: Farming")

class Mother:
    def skill1(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
c.skill1()


print("\nMultilevel Inheritance")
class Grandparent:
    def display(self):
        print("Grandparent's method")

class Parent(Grandparent):
    def display(self):
        print("Parent's method")

class Child(Parent):
    def display(self):
        print("Child's method")

c = Child()
c.display()


print("\nHierachical Inheritance")
class Animal:
    def sound(self):
        print(" animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
d.sound()

c = Cat()
c.sound()

#Overridding
class A :
    def hello(self):
        return "Good Morning!"
class B(A):
    def hello(self):
        return super().hello() + "Good Night!"

a =B()
print(a.hello())

#Overloading
import math

class AreaCalculator:
    def area(self, length, width=None):
        if width is None:
            raise ValueError("Width for a rectangle.")
        return length * width

    def area_circle(self, radius):
        return 3.14 * (radius ** 2)

    def area_triangle(self, base, height):
        return 0.5 * base * height

    def area_var(self, *args):
        if len(args) == 2:
            return self.area(args[0], args[1])
        elif len(args) == 1:
            return self.area_circle(args[0])
        elif len(args) == 3:
            return self.area_triangle(args[0], args[1])
        else:
            raise ValueError("Invalid number of arguments.")

calculator = AreaCalculator()


print("Area of Rectangle:", calculator.area_var(11, 5))
print("Area of Circle ", calculator.area_var(10))
print("Area of Triangle :", calculator.area_var(2, 3, 4))
