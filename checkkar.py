# # ROCK PAPER SCISSOR

# # import random 

# # random_number = random.randint(1,5)
# # # choose a random number everytime between 1 and 5
# # print(random_number)
# # # import book from python library

# # import random

# # user_choice = input("ROCK / PAPER / SCISSORS : ")
# # computer_choice = random.randint(1 , 3)
# # # computer = 1 [ ROCK]
# # # computer = 2 [ SCISSOR]
# # # computer = 3 [ PAPER]
# # if user_choice == "ROCK":
# #     if computer_choice ==2: # 2 --> SCISSOR
# #       print("YOU WON!!")
# #     elif computer_choice == 3: # 3 --> PAPER
# #       print("YOU LOSE!!")
# #     else:
# #       print("TIE")
      
# # elif user_choice == "PAPER":   
# #   if computer_choice ==1: # 1 --> ROCK
# #     print("YOU WON!!")
# #   elif computer_choice == 2: # 2--> SCISSORS
# #     print("YOU LOSE!!")
# #   else:
# #     print("TIE")

# # elif user_choice =="SCISSORS":
# #   if computer_choice ==3: # 3 --> PAPER
# #     print("YOU WON!!")
# #   elif computer_choice == 1: # 1 --> ROCK
# #     print("YOU LOSE!!")
# #   else:
# #     print("TIE")

# # else:
# #   print("INVALID CHOICE")

# # CALCULATOR
# # num1 = int(input("Enter your first number : "))
# # num2 = int(input("Enter your second number : "))
# # choice = input("+ OR - OR * OR / OR % :")
# # result = 0

# # if choice == "+":
# #   result = num1 + num2
# # elif choice == "-":
# #   result = num1 - num2
# # elif choice == "*":
# #   result = num1*num2
# # elif choice == "/":
# #   result = num1/num2
# # elif choice =="%":
# #   result = num1%num2
# # else:
# #   print("INVALID CHOICE")

# # print(result)


# # Write a program to check whether a person is eligible for voting or not. (accept age from user)

# # age = int(input("Enter your age : "))
# # if age >= 18:
# #   print("You are eligible for voting")
# # else:
# #   print("You are not eligible for voting")

# # Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# #              Unit                                                     Price  
# # First 100 units                                               no charge
# # Next 100 units                                              Rs 5 per unit
# # After 200 units                                             Rs 10 per unit


# # units = int(input("Enter your electricity units: "))
# # if units <100:
# #   print("NO CHARGE")
# # elif units >=100 and units <200:
# #    result = 5*units
# #    print(result)
# # elif units >=200:
# #    result = 10*units
# #    print(result)
# # else:
# #   print("INVALID UNITS")

# # Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

# n = int(input("Enter number between 1 to 7 : "))
# if  n == 7:
#   print("SATURDAY")
# elif n == 1:
#   print("SUNDAY")
# elif n == 2:
#   print("MONDAY")
# elif n == 3:
#   print("TUESDAY")
# elif n == 4:
#   print("WEDNESDAY")
# elif n==5:
#   print("THURSDAY")
# elif n == 6:
#   print("FRIDAY")
# else:
#   print("INVALID NUMBER")

# I WANT TO DO A TASK AGAIN , AGAIN, AGAIN

# IN A LOOP 


# i is a variable which is running from 0 to 5-1 = 4
# 0 1 2 3 4
# for i in range(5):
#   print(i)


# IN python range works for n -1 
# for i in range(10) --> 
# 0 1 2 3 4 5 6 7 8 9

# for i in range(4)-->
# 0 1 2 3 

# BY DEFAULT , range starts from 0

# I WANT TO PRINT NUMBERS FROM 1 to 10
# for i in range(1           ,    10):
#             # starting     ,  ending point
#   print(i)

# 
# for i in range(43,144):
#   print(i)

# PRINT NUMBERS
# 5 to 45
# 99 to 999
# 89 to 159
# 43 to 143
# For i1 in range (5 ;45)
# For i2 in range (99;999)
# For i3 in range (89;153)
#  Print(i1)
# Print(i2)
# Print(i3)


# # I WANT TO PRINT NUMBERS FROM 10 to 1
# for i in range(10,-2,-1):
# # how much we want to reduce/increase
#   print(i)


# 599 to 59
# for i in range(10,-11,-1):
#   print(i)


# one more type of loop
# n = 10
# while n==10:
#   print("Hello")


# FOR LOOP --> end 
# WHILE LOOP --> we dont what is our end

  
# 140 to 14

# 22 to -22

# 10 to -10 

# n = 1    60 <= 59 ? 
# n = 1
# while n <=59:
#   print(n)
#   n = n + 1

# 1
# 2
# 3
# 4
# 5
# -------59

# 1 to 20 
# even 

# for i in range(1,21):
#   if i %2 !=0:
#     print(i)

# IF I WANT TO PRINT NUMBERS FROM 
# 1 to 100 but I want only those numbers which
# can be divisible 5 and 7 

# for i in range(1,101):
#   if i %5 == 0 and i%7==0:
#     print(i)

# AND --> all the conditions should be true
# OR --> any of the condition will work

# I WANT TO PRINT 
# 10 to -1 using while LookupError

# n = 10
# while n >=1:
#   print(n)
#   n = n -1

# 140 to 14
n = 140
while n>=14 and n%2==0: 
 print(n) 
 n = n-1
# 140
# 139
# 138
# 137
# .....14
    
# 22 to -22

# 10 to -10 
