
# ************************************************Calculator************************************
# first = float(input("Enter You first number"))
# second = float(input("Enter Your second numbr"))
# operator = str(input("Enter Your operator"))


# if operator == "+":
#     print(f"{first} + {second} = {first+second}")

# elif operator == "-":
#     print(f"{first} - {second} = {first-second}")

# elif operator == "*":
#     print(f"{first} * {second} = {first*second}")

# elif operator == "**":
#     print(f"{first} ** {second} = {first**second}")

# elif operator == "%":
#     print(f"{first} % {second} = {first%second}")

# else:
#     print("Please enter valid number or operator")


# ***************************Email slicer**************************

# email = input("Enter your email")

# index = email.index("@")

# username = email[:index]
# Domain = email[index:]

# print(f"You username is {username} your domain is {Domain}")


# ********************************Timer programme******************

# import time

# myTime = int(input("Enter Your Time :"))

# for x in range(myTime,0,-1):
#     second = x % 60
#     minut = int((x/60)%60)
#     hour = int((x/3600)%60)
#     print(f"{hour:02}:{minut:02}:{second:02}")
#     time.sleep(1)

# print("Times Up")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$Quize game$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Quetions = (
#             "Which animal is largest animal on earth",
#             "How many bons in Human body",
#             "Who invented Buld",
#             "Who is known as Iron man of india",
#             "Who Invented 0"
# )

# options = (
#             ("A : Horse","B : Whale","C : Lion","D : Owl"),
#             ("A : 206","B : 207","C : 208","D : 209"),
#             ("A : Elon","B : Tony","C : Thomas","D : einstean"),
#             ("A : Sardar patel","B : abul kalam","C : Jwln","D : Gandhi"),
#             ("A : albert","B : yuclid","C : nikola","D : arya bhat")
# )


# answers = ("B","A","C","A","D")
# guesses = []
# score = 0
# quetion_num = 0


# for quetion in Quetions:
#     print("------------------------")
#     print(quetion)
    
#     for option in options[quetion_num]:
#         print(option)
#     guess = input("Which one is correct").upper()
#     guesses.append(guess)
#     if guess == answers[quetion_num]:
#         print("Correct !")
#         score += 1
#     else:
#         print(f"Wrong answer guess 😫 Correct is {answers[quetion_num]}")
#     quetion_num +=1

# print("--------------------------")
# print(f"Correct answers is {answers}")
# print(f"Your answers are {guesses}")
# print("Your Total score is",score)





# ******************************Rondom Numbers***************************8

# import random

# choices = ("Rock","Paper","Scissor")
# choice = random.choice(choices)
# print(choice)

# low = 1
# high = 20
# guesses = 0
# number = random.randint(low,high)

# while True:
#     print(f"Guess your number {low} - {high}")
#     guess = int(input("Guess number !"))
#     guesses +=1
#     if guess > number:
#         print(guess,"Your guess is too high")
#     elif guess < number:
#         print(guess,"Your guess is too low")
#     else:
#         print(guess,"is correct !")
#         break


# print("---------------")
# print(guesses)



# ***************************ROCK PAPER SCISSORS**********************
# import random
# comp_choices = ("rock","paper","scissors")
# play = 0


# while True:
#     comp_choice = random.choice(comp_choices)

#     user_choice = input("Enter Your choice")

#     if user_choice == "rock" and comp_choice == "scissors" or user_choice == "paper" and comp_choice == "rock" or user_choice == "scissors" and comp_choice == "paper":
#         print("You Win")
#     elif user_choice == comp_choice:
#         print("Game draw")

#     else:
#         print("computer Win")
#     play +=1
#     if play == 10:
#         break



