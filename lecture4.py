# info = {
#     "name": "sadre",
#     "age":19,
#      "study":"BA",
#      "fav_movie":"avenger"
# }
# info["name"] = "King"

# info = {}
# info["name"] = "sadre Aalm"
# info["age"] = 19
# print(info["age"])

# student = {
#     "name":"sadre",
#     "age":19,
#     "subject":{
#         "math":90,
#         "science":50,
#             "hindi":60    }
# }

# print(student["subject"]["math"])
# print(list(student.keys())[1])


#               ************************** set() sets are mutable but sets elements are immutable *****************************

# ListSet = {1,2,3,4,5,6,6,2,3,"Sadre","Mr"}
# items = set()
# items.add(1)
# items.add(2)
# items.add(3)
# items.add(2)
# items.add("Sadre")
# items.add(("alam","khan"))
# # items.remove("Sadre")
# # items.clear()
# # print(items.pop())
# # items.update()
# print(items)

# list_1 = {1,2,2,3}
# list_2 = {3,4,5,6}
# print(list_1.union(list_2))   union returns the different values not similar value 
# print(list_1.intersection(list_2)) intersection return the same value if present in both varaible 


# Q1.
# dic = {
#     "cat": "a small animal",
#     "table": ["a piece of furniture", "list of facts & figure"],
#     "name" : ("sadre","alam","prince")
# }
# print(dic["table"][1])
# print(dic["name"][0])

    # Q2. 
# Class = {"python","java","c++","python","javascript","java","python","java","c","c++"}

# print(len(Class))


# Q3. 
# result = {}
# x = input("Enter your Math marks :")
# result.update({"Math":x})
# x = input("Enter your science marks :")
# result.update({"Science":x})
# x = input("Enter your Chem marks :")
# result.update({"Chem":x})
# print(result)

# store = {9, "9.0"}
# store = {("float",9.0)
#          ("int",9)}
# print(store)

# name = "sadre alam"
# print(name.count("a"))


