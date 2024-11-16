# ****************************Delete something in code****************************

# class greeting:
#     def __init__(self,name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello {self.name}")
# user1 = greeting("sadre")
# del user1.name                 =======>>>>Del keyword delete the name
# user1.greet()








# ***********************************private __ attributes and methods**************************************


# class Account:
#     def __init__(self,acNo,acPass):
#         self.__accountNo = acNo
#         self.__accountPass = acPass          for making private attribute we can use __ dubble underscore now we are not able to access this attritue outside of class

# ac1 = Account("12345","abcde") 
# print(ac1.__accountNo)



# *************************************Inheritance****************something take from the parent class*****************

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car Started")
#     @staticmethod
#     def stop():
#         print("Car Stoped")

# class toyota(Car):
#     def __init__(self,name):
#         self.name = name
# car1 = toyota("Fortunar")
# print(car1.name)
# car1.start()

 
# ***************************Multi level inheritance**********************

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car Started")
#     @staticmethod
#     def stop():
#         print("Car Stoped")
# class toyota(Car):
#     def __init__(self,brand):
#         self.brand = brand
# class fortunar(toyota):
#     def __init__(self,type):
#         self.type = type
# car1 = fortunar("Desile")
# car1.start()






# ***************************Multiple inheritanse*************************** 

# class A:
#     a = "I am class A"

# class B:
#     b = "I am class B"

# class C:
#     c = "I am class C"

# class D(A,B,C):
#     d = "I am class D"


# a1 = D()
# print(a1.b)


# ***************************Super()**********************for inherit parent methods*****************

# class Car:
#     def __init__(self,type):
#         self.type = type
    
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop():
#         print("Car stoped...")
    
# class toyota(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = toyota("Bmw","diseal")
# print(car1.name,car1.type)






# ****************************ClassMethod****************************for changing something in parent class**********


# class Person:
#     name = "Anonymous"

#     @classmethod
#     def sadre(cls,name):
#         cls.name = name

#     # def sadre(self,name):
#     #     # Person.name = name
#     #     # __class__.name = name
# p1 = Person()
# p1.sadre("Sadre")
# print(p1.name)
# print(Person.name)





# **********************{Property decorator} use for when we are not decided to value is fixed for long term*********************


# class Number:
#     def __init__(self,real,img):
#         self.real = real 
#         self.img = img
    
#     def showNum(self):
#         print(self.real,"i +", self.img,"j")
    
#     def __add__(self,num2):
#         newReal = self.real+num2.real
#         newImg = self.img+num2.img
#         return Number(newReal,newImg)
#     def __sub__(self,num2):
#         newReal = self.real-num2.real
#         newImg = self.img-num2.img
#         return Number(newReal,newImg)
        

# num1 = Number(9,8)
# num2 = Number(5,3)
# num1.showNum()
# num2.showNum()

# # num3 = num1.add(num2)
# num3 = num1 + num2
# num4 = num1 - num2
# num3.showNum()
# num4.showNum()





# **********************************Practice Quetion**************************
# Q1.


# import math

# class Circle:
#     def __init__(self,r):
#         self.r = r
     
#     def Area(self):
#         pi = math.pi
#         return pi*self.r*self.r
    
#     def Perimeter(self):
#         pI = math.pi
#         return 2*pI*self.r
    

# cr1 = Circle(21)
# print(cr1.Area())
# print(cr1.Perimeter())



# Q2.

# class Employee:
#     def __init__(self,role,Dep,sal):
#         self.role = role
#         self.Dep = Dep
#         self.sal = sal
#     def showDetail(self):
#         print(f"Role = {self.role}\nDepartment = {self.Dep}\nSallary = {self.sal}")

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#         super().__init__("Engineer","IT",45000)


# eng1 = Engineer("Elon",50)
# eng1.showDetail()


# Q3.

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,item2):
        return self.price > item2.price



i1 = Order("fruits",56)
i2 = Order("Vegitable",76)
Ord = i1>i2

print(Ord)

