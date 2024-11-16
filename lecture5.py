# i = 1
# while i < 6 :
#     print(i)
#     i += 1

# i = 1

# while i < 10:
#     print(i)
#     if (i == 4):
#         break
#     i += 1

# i = 1

# while i < 101:
#     print(f"I Love You {i} Times")
#     if (i == 3):
#         break
#     i += 1

# i = 1

# while i < 7:
#     i += 1
#     if i == 4:
#         continue
#     print(i)


# i = 1

# while i < 10 :
#     print(i)
#     i +=1
# else:
#     print("I equal to 10")


# avengers = ["Tony","Thor","Captain","Spiderman"]
# i = 0

# for avenger in avengers:
#     i += 1
#     print(i,avenger)

# fruits = ["Apple","Banana","Pineapple","Mango"]

# for fruit in fruits:
#     print(fruit)
#     if fruit == "Banana":
#         break

# for fruit in fruits :
#     if fruit == "Mango":
#         break
#     print(fruit)

# for fruit in fruits:
#     if fruit == "Apple":
#         continue
#     print(fruit)

# for i in range(6):
#     print(i)

# for x in range(2,8):
#     print(x)


# for x in range(2,20,4):
#     print(x)

# for x in range(2,8,2):
#     print(x)
# else:
#     print("Finaly Loop is end !")

# for x in range(2,8):
#     if x == 5:
#         break
#     print(x)
# else:
#     print("Loop is end")

# color = ["Red","Green","Yellow"]
# fruit = ["Apple","Banana","Mango"]

# for x in color:
#     for y in fruit:
#         print(x,y)

# for x in [0,1,2,3]:
#     print(x)

                                # ******************* Practice Quetion ****************************************

# Q1. 
# for x in range(100,1,-1):
#     print(x)

# number = int(input("Enter Your Number"))

# for number in range(0,11,number):
#     print(number)

# for x in range(1,11):
#     print(x*number)



# Q2. 
# num = int(input("Enter Your Number"))
# i = 0
# Sum = 0
# while i < num:
#     i+=1
#     Sum += i
# print(Sum)

        #  ************  Other method ********************


# n  = 5
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print("This is total number of sum",sum)



# Q3.
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)
    


nums = (1,2,3,4,5,6,7,8,9)

idx = 0
x = 5
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

# while idx <len(nums):
#     if nums[idx] == x:
#         print("Number is found",idx)
#         break
#     else:
#         print("Finding..........")
#     idx +=1
idx = 0
for num in nums:
    if num == x:
        print("Number is found At idx",idx)
    idx +=1


    
 
 
