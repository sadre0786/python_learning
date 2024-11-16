# **********************A function is a block of code which only runs when it's call****************************
# **********************You can pass data which is known as parameter which is pass in function *****************************


# def my_function():
#     print("Hello i am sadre")
# my_function()

# def my_function(name):
#     print(f"Hello {name}")
# my_function("Sadre")

# def myFunction(fname,lname):
#     print(f"First name = {fname} \nLast name = {lname}")
# myFunction("Sadre","Alam")


# ******************Arbitrary arguments*************
# If you don't Know how many arguments you want then  add {*} before the perameter name in the function defination
# this way of function will recieve tuples of arguments

# def myFunction(*fr):
#     print(f"My best freind is {fr[2]}")
# myFunction("Nirale","Ahad","Raqib")


# *******************Keywords arguments ***********************

# def myFunction(name1,name2,name3):
#     print(f"My name is {name3}")
# myFunction(name1="Sadre",name2 = "Alama",name3="King Khan")




# ***************************************Arbitrary keywords Arguments, **kwargs ***********************

# def myFunction(**kids):
#     print(f"First child is {kids["firstChild"]}")

# myFunction(firstChild = "Zainab",secondChild="Rayen")


# *****************************************Keywords arguments *************************************8

# def myFunction(child1,child2,child3,):
#     print(f"My elder child is {child1}")
# myFunction(child1="Sadre",child2="Alam",child3="Khan")



# **********************************************Default parameter**************************************

# def myFunction(default = "Sadre"):
#     print(f"My name is {default}")
# myFunction("ALAM")
# myFunction("KhanSaab")
# myFunction()

# *******************************************************Passing a list as an argument*******************************

# def myFunction(foods):
#     for food in foods:
#         print(food)
# foods = ["Apple","Banana","Burger","Naan"]
# myFunction(foods)



# *****************************************************Return Statement****************************************

# def myFunction(x):
#     return 5*x


# print(myFunction(4))

# def avg(n1,n2,n3):
#     total = n1+n2+n3
#     Avg = total /3
#     return int(Avg)

# print(
# avg(1,2,3))



# ***************************************Ignore next line print**************************

# print("Sadre", end=" ")
# print("Alam")



# Q1. Print the lenth of list 

# def lentg(lis):
#     print(len(lis))
# num = [1,2,3,4,5,6,7,8]
# lentg(num)


# Q2. print a list in single line 

# def Sing(lists):
#     for list in lists:
#         print(list, end=",")

# nums = [1,2,3,4,5,6]
# Sing(nums)


# Q3. Find the n factorial


# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *=i
# print(fact)


# n = 5
# fact = 1
# i = 0
# while i < n:
#     i += 1
#     fact *= i
# print(fact)


# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     print(f"Factorial of {n} is {result}")

# fact(5)


# Q5. usd to inr 

# def usd(n):
#     inr = 83
#     print(n*inr)
# usd(5)

# Q6. 

# def finder(number):
#     if number%2==0:
#         print(f"{number} is Even")
#     else:
#         print(f"{number} is Odd")
# finder(4)

# ****************************************Recursion function**********************8888

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
# show(5)


# ********************************Understand recursion *****************************************
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))


# Q1.

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)
# print(sum(9))


# Q2. 
# def printList(list,idx=0):
#     if idx == len(list):
#         return
#     else:
#         print(list[idx])
#         printList(list,idx+1)
# fruits = ["Apple","Banana","Mango"]
# print(printList(fruits))


