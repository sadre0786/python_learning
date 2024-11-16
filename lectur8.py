# ********************************OOPS**********************
# Four concept of oops => Classes , Object , Inheritance & polymorphism
# Classes => This is a blueprint. in this, we have atributes(data) and methods(function) are defined like car Class,  which can have properties like color & model and can have methods like stop() drive() 
# Object =>  This is an instance of a class. When you create an object from a class, it can use the properties and methods of the class. Like my_car = car().
# Inheritance =>
# Polymorphism =>


# ******************************Basic of oops*****************************8

# class Student:
#     def __init__(self):      #default constructor
#         pass
#     def __init__(self,name,age):   #parameterize constructor
#         self.name = name
#         self.age = age
#         print("Adding new student in databass...")

# s1 = Student("Sadre",19)
# print(s1.age,s1.name)



# *******************************Student diffrent name but not diff collage**************************

# class Student:
#     collage_name = "Jamia millia islamia"     this class attribute         #this is comman for every student and equire only once space
#     def __init__(self,name,age):               this is object attribut
#         self.name = name                           #data more acquire because single name single space aquare
#         self.age = age
#         print("Student adding in databass...")                  object > class

# s1 = Student("Sadre",19)
# print(s1.collage_name)






# class Car:
#     def __init__(self,color,model):
#         print("Automatic call")
#         self.color = color
#         self.model = model
#     def drive(self):
#         print(f"{self.model} is driving")
# Mycar = Car("Black","Ford")
# Mycar.drive()

# ***************Inheritance*********************


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speakes(self):
#         return "Animal speakes"

# class Dog(Animal):
#     def speakes(self):
#         return f"{self.name} says woof !"

# class Cat(Animal):
#     def speakes(self):
#         return f"{self.name} says Meew !"

# Mydog = Dog("Puppy")
# Mycat = Cat("Catty")

# print(Mydog.speakes())
# print(Mycat.speakes())


# Q1. Create student class that takes name & marks of three subjects as arguments in constructor then create a method to print the average

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val
#         avg = sum/3
#         print(f"Hi {self.name} Your Average score is {avg}")
# s1 = Student("Bruce",[67,88,76])
# s1.avg()



# class Student:
#     def __init__(self,name,Math,Physics,bio):
#         self.name = name
#         self.math = Math
#         self.pyhsics = Physics
#         self.bio = bio
#         print("Student marks getting...")
    
#     def avg(self):
#         sum = self.math+self.bio+self.pyhsics
#         avrage = sum/3
#         return(f"Average number is {avrage}")

# s1 = Student("Sadre",90,80,70)
# print(s1.avg())





#************* staticmethod**************

# class student:
#     def __init__(self,name):
#         self.name = name 
#     @staticmethod                #staticmethod print function without using self para
#     def hello():
#         print("Hello") 

# s1 = student("sadre")
# s1.hello()


# *******************ABSTRACTION********************

# class car:
#     def __init__(self):
#         self.acc = False
#         self.Break = False         #in this example all the unnacessary things hide from the user and showing olny essential thing
#         self.clutch = False
    
#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car Started...")
# car1 = car()
# car1.start()


# Q2. Create Account class with two attributes - Balance & account no. create methods for Debit, Credit & printing the balance. 


# class Account:
#     def __init__(self,bal,ac):
#         self.balance = bal
#         self.account = ac
    
#     def Debit(self,amount):
#         self.balance -= amount
#         print(f"{amount} was debit from your acount {self.cr_bal()}")
    
#     def Credit(self,amount):
#         self.balance += amount
#         print(f"{amount} was credit in your account {self.cr_bal()}")
    
#     def cr_bal(self):
#         return(f"Your current balance is {self.balance}")


# acc1 = Account(27,123455)
# acc1.Credit(15000)

    







