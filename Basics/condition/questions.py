# # age reference
# age = int(input("Enter your age : "))
# if(age<13 & age >0):
#     print("Child")
# elif(age>=13 & age < 20):
#     print("Teenager")
# elif(age>=20 & age <60):
#     print("Adult")
# elif(age>=60):
#     print("Senior")
# else:
#     print("Invalid age!!")

# # movie ticket
# day = input("Enter the Day : ")
# age = int(input("Enter your age : "))
# day = day.lower()
# # if (day =="wednesday"):
# #     if (age>=18):
# #         print("Ticket price is 10$")
# #     else:
# #         print("Ticket price is 6$")
# # else:
# #     if (age>=18):
# #         print("Ticket price is 12$")
# #     else:
# #         print("Ticket price is 8$")
# price = 12 if age>=18 else 8
# if day == "wednesday":
#     price -= 2
# print("Ticket price is $",price)

# # grade calculator
# marks = int(input("Enter your marks : "))
# if (90<=marks<=100):
#     print("A")
# elif(80<=marks<90):
#     print("B")
# elif(70<=marks<80):
#     print("C")
# elif(60<=marks<70):
#     print("D")
# elif(0<=marks<60):
#     print("F")
# else:
#     print("Invalid input")

# # Fruit ripeness checker
# fruit = "Banana"
# color = input("Enter the colour of fruit : ")
# color = color.lower()
# if fruit == "Banana":
#     if color == "green":
#         ripeness = "Unripe"
#     elif color == "yellow":
#         ripeness = "Ripe"
#     elif color == "Brown":
#         ripeness="Overripe"
#     else:
#         print("Can't define the colour")
#         exit()
#     print("Banana is",ripeness)
# else:
#     print("Can't define the fruit")

# # Weather Activity Suggestion
# weather = input("Enter today's weather : ")
# weather = weather.lower()
# if weather == "sunny":
#     activity = "Go for a walk"
# elif weather == "rainy":
#     activity = "Read a Book"
# elif weather == "snowy":
#     activity = "Build a snowman"
# else:
#     print("Can't get the weather")
#     exit()
# print(activity)

# # coffee order
# extra_shot = True
# order_size = input("Enter coffee size : \n")
# if extra_shot:
#     coffee = order_size+" Coffeee with an extra shot of espresso"
# else:
#     coffee = order_size+" Coffee"
# print("Order : ",coffee)

# # password strength checker
# p = input("Enter your password :\n")
# l = len(p)
# if l < 6:
#     strength = "Weak"
# elif l <=10 :
#     strength = "Medium"
# else:
#     strength = "Strong"
# print("Your Password is",strength)

# # leap year
# year = int(input("Enter a Year :\n"))
# if (year%400==0)or(year%4 == 0 and year%100 != 0) :
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

# # pet food
# pet = input("Which pet do you have :\n")
# pet = pet.lower()
# age = int(input("Enter the age of your pet(years) :\n"))
# if pet == "cat":
#     if age >5:
#         food = "Senior cat food"
#     else:
#         food = "Junior cat food"
# elif pet == "dog":
#     if age < 2 :
#         food = "Puppy food"
#     else:
#         food = "Senior dog food"
# else:
#     print("Can't get the pet")
#     exit()
# print(food)

