# ROCK PAPER SCISSOR

# import random 

# random_number = random.randint(1,5)
# # choose a random number everytime between 1 and 5
# print(random_number)
# # import book from python library

# import random

# user_choice = input("ROCK / PAPER / SCISSORS : ")
# computer_choice = random.randint(1 , 3)
# # computer = 1 [ ROCK]
# # computer = 2 [ SCISSOR]
# # computer = 3 [ PAPER]
# if user_choice == "ROCK":
#     if computer_choice ==2: # 2 --> SCISSOR
#       print("YOU WON!!")
#     elif computer_choice == 3: # 3 --> PAPER
#       print("YOU LOSE!!")
#     else:
#       print("TIE")
      
# elif user_choice == "PAPER":   
#   if computer_choice ==1: # 1 --> ROCK
#     print("YOU WON!!")
#   elif computer_choice == 2: # 2--> SCISSORS
#     print("YOU LOSE!!")
#   else:
#     print("TIE")

# elif user_choice =="SCISSORS":
#   if computer_choice ==3: # 3 --> PAPER
#     print("YOU WON!!")
#   elif computer_choice == 1: # 1 --> ROCK
#     print("YOU LOSE!!")
#   else:
#     print("TIE")

# else:
#   print("INVALID CHOICE")

# CALCULATOR
# num1 = int(input("Enter your first number : "))
# num2 = int(input("Enter your second number : "))
# choice = input("+ OR - OR * OR / OR % :")
# result = 0

# if choice == "+":
#   result = num1 + num2
# elif choice == "-":
#   result = num1 - num2
# elif choice == "*":
#   result = num1*num2
# elif choice == "/":
#   result = num1/num2
# elif choice =="%":
#   result = num1%num2
# else:
#   print("INVALID CHOICE")

# print(result)


# Write a program to check whether a person is eligible for voting or not. (accept age from user)

# age = int(input("Enter your age : "))
# if age >= 18:
#   print("You are eligible for voting")
# else:
#   print("You are not eligible for voting")

# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit


# units = int(input("Enter your electricity units: "))
# if units <100:
#   print("NO CHARGE")
# elif units >=100 and units <200:
#    result = 5*units
#    print(result)
# elif units >=200:
#    result = 10*units
#    print(result)
# else:
#   print("INVALID UNITS")

# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

n = int(input("Enter number between 1 to 7 : "))
if  n == 7:
  print("SATURDAY")
elif n == 1:
  print("SUNDAY")
elif n == 2:
  print("MONDAY")
elif n == 3:
  print("TUESDAY")
elif n == 4:
  print("WEDNESDAY")
elif n==5:
  print("THURSDAY")
elif n == 6:
  print("FRIDAY")
else:
  print("INVALID NUMBER")
