# This is a sample Python script.

# Press Ctrl+R to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# PYTHON BASICS ----UwU----

# ------1

# age = 20
# price = 19.19
# my_name = "batnyam"
# apre = ":"
# isOnline = False
# print("1.", my_name + apre, age + price, isOnline);

# ------2

# name = input("What is your name? ")
# print("Hello " + name)

# ------3

# birth = input("Enter your birth year: ")
# age = 2023 - int(birth)
# print("Age:", age)

# 10 is number
# 10.1 is float

# int()
# float()
# bool()
# str()

# ------3

# first = input("First: ")
# second = input("second: ")
# sum = float(first) + float(second)
# ----------
# first = float(input("First: "))
# second = float(input("second: "))
# sum = first + second
#
# print("sum: " + str(sum))

# ------4

# course = "Python for begginers"
        # 0123456789
# print(course.upper())
# print(course.lower())
# print(course.find("for"))
# print(course.replace("for", "4"))
# replace shows: Python 4 begginers
# print("python" in course) #true

# ------5

# name = "John"
# age = 30
# message = "My name is %s, and I am %d years old." % (name, age)
# print(message)
# print(14 % 5) #return 5
# print(10 ** 3) #return 1000
#---------------------------
# x=10
# x=x+3
# x*=3
# print(x)

# ------6

# x = (1 + 2) * (2 * 5)
# x = 3 >= 2 # ali ih bogood tentsuu gedeg hoyr nohtsoliin ali neg n l biylej bwl true butsaadag
# y = 2 == 2 # ijil baiwal true butsaana
# <
# <=
# >
# >=
# ==
# != not equal

# print("x", x)
# print("y", y)

# ------7

# price = 5
# print(price > 10 or price < 30)
# print(price > 10 and price < 30)
# print(not price > 10)

# ------8

# temperature = 30
#
# if temperature > 30: #30<
#     print("It is a hot day")
#     print("Drink plenty of water")
# elif temperature > 20: # (20<30]
#     print("It is a nice day")
# else: #last option
#     print("nothing")
# print("Done")

# ------9

# weight = input("What is your weight?: ")
# weightSpec = input("(K)g or (L)bs?: ")
# if weightSpec == 'K' or 'k':
#     weightLbs = float(weight) / 2.2
#     print("Weight in lbs: ", weightLbs)
# elif weightSpec == 'L' or 'l':
#     weightKg = float(weight) * 2.2
#     print("Weight in kg: ", weightKg)
# else:
#     print("Done !")

# if weightSpec.upper() == "K":
#     converted = float(weight) / 0.45
#     print('Weight in Lbs: ', converted)
# else:
#     converted = float(weight) * 0.45
#     print('Weight in Kg: ', converted)

# ------10

# i = 1
# while i <= 5:
#     print(i)
#     i+=1
# returns:
# 1
# 2
# 3
# 4
# 5

# i = 1
# while i <= 5:
#     print(i * '*')
#     i+=1
# returns:
# *
# **
# ***
# ****
# *****

# ------10

names = ["bat", "bold", "dorj", "nar"]
# print(names[0, 1])
print(names[0:3])
# this returns ["bat", "bold", "dorj"]
