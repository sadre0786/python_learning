# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)


# f = open("demo2.txt","r")
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x)


# f = open("demo.txt","a")
# f.write("\n Second line text added by sadre")
# f.close()

# f = open("demo.txt","r")
# print(f.read())


        #  *****************No need to close ***************
# with open("demo.txt","w") as f:
#     f.write("My new text")

# with open("demo.txt","r") as f:
#     print(f.read())


# Q1. 
# f = open("pratice.txt","r")
# data = f.read()
# print(data)


# Q2. 

# with open("pratice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open("pratice.txt","w") as f:
#     data = f.write(new_data)


# Q3. 
# with open("pratice.txt","r") as f :
#     data = f.read()     
#     if data.find("learning") != -1:
#         print("Found")
#     else:
#         print("Not Found")

# Q4. 

# def findLine():
#     data = True
#     word = "learning"
#     Line = 1
#     with open("pratice.txt","r") as f:
#         while data:
#             data = f.readline() 
#             if word in data:
#                 print(Line)
#                 return
#             Line+=1
#     return -1
# findLine()



# Q5.

# with open("practice.txt","r") as f:
#     data = f.read()
#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             num = int(num)
#             if num%2==0:
#                 print(num)
#             num = ""
#         else:
#             num += data[i]
 

# with open("practice.txt","r") as f:
#     data = f.read()
#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             print(num)
#             num = ""
#         else:
#             num += data[i]


# count = 0
# with open("practice.txt","r") as f:
#     data = f.read()
#     nums = data.split(",")
#     for num in nums:
#         if int(num)%2==0:
#             count+=1
# print(count)
