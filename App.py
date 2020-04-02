#print("Hello World

#Character_Name = "John"
#Character_Age = 50
#is_male = True
#
#print("There once was a man named " + Character_Name +",")
#print("he was "+ Character_Age + " years old.")
#print("He really liked the name " + Character_Name + ",")
#print("but didn't like being " + Character_Age + ".")

# print("Giraffe\nAcademy")
#
# phrase = "Giraffe Academy"
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))

# print(phrase[0])
# print(phrase.index("G"))
# print(phrase.replace("Giraffe","Elephant"))

# print(-2.0987)
# print(3+4.5)
# print (3*5)
# print (3*4+5)
# print (3*(4+5))
# print(10 %3) #modulus number
# my_num = -5
# print(my_num)
# print(str(my_num) + " my favorite number")
#
# print(abs(my_num))
# print(pow(3,2)) # power of number
# print(max(4,6))
# print(min(4,6))
# print(round(3.7)) #rounding numbers
#
# from math import *
# print(floor(3.7))
# print(ceil(3.4))
# print(sqrt(36))

# name = input("Enter Name:")
# age = input("Enter Age:")
# print("Hello "+ name + age)
#

# num1 = input("Enter a Number:")
# num2 = input("Enter another Number:")
# # results = int(num1) + int(num2)
# results = float(num1) + float(num2)
# print(results)

# color = input("Enter a color:")
# plural_noun = input("Enter a plural noun:")
# celebrity = input("Enter a celebrity:")
# print("Roses are "+ color)
# print( plural_noun + " are blue")
# print("I love "+ celebrity)


#lists

# Friends = ["Kevin","Jim","Karen","Oscar","Toby"]
# print(Friends[1])
# print(Friends)
# print(Friends[1:])
# Friends[1] = "Mike"
# print(Friends[1])
#
# lucky_numbers = [4,8,15,16,23,42]
# friends = ["Kevin","Jim","Jim","Karen","Oscar","Toby"]
#friends.extend(lucky_numbers) #add to lists
#friends.append("Creed")
#friends.insert(1,"Kelly")
#friends.remove("Jim")
#friends.clear
#friends.pop()

# print(friends.index("Oscar"))
# print(friends.count("Jim"))
# friends.sort()
# lucky_numbers.sort()
# friends2 = friends.copy
# print(lucky_numbers)
# print(friends)


#tuples
#
# coordinates = (4,5)
# print(coordinates[0])
# print(coordinates[1])

#functions
#
# def say_hi(name,age):
#     print("Hello "+ name + "," + str(age))
# say_hi("Mike",35)
# say_hi("Steve",54)
#
# def cube(num):
#     #print("Code")
#     return num*num*num
# result = cube(4)
# print(cube(3))
# print(result)

# is_male = True
# if is_male:
#     print("You are a male")
#############################################
# is_male = True
# is_tall = False
#if is_male and is_tall:
# if is_male or is_tall:
#     print("You are a male or tall or both")
# else:
#     print("You are not a male nor tall")
#
# if is_male or is_tall:
#     print("You are a male or tall or both")
# elif is_male and not(is_tall):
#     print("You are short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else :
#     print("You are not a male nor tall")

# def max_num(num1,num2,num3):
#     if num1  >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(40,4,5))
#
# num1 = float(input("Enter first number:"))
# OP = input("Enter Operator:")
# num2 = float(input("Enter second number:"))
#
# if OP == "+":
#     print( num1 + num2)
# elif OP == "-":
#     print(num1 - num2)
# elif OP == "/":
#     print(num1 / num2)
# elif OP == "*":
#     print (num1 * num2)
# else:
#     print("invalid operator")



#############Dictionaries


# monthConversions = {
#     "Jan": "Janurary",
#     "Feb": "Feburary",
#     "Mar": "March",
#     "Apr" : "April" ,
#     "May": "March",
#     "Jun": "June",
#     "Jul": "July",
#     0: "January",
#     1: "something else"
# }
#
# print(monthConversions["Apr"])
# print(monthConversions.get("luv","not a valid key"))

############## while loops
#
# i = 1
# while i <= 10:
#     print(i)
#     #i = i + 1
#     i += 1
#
# print("Done with Loop")

############### Guessing Game

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while  guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter Guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win")


################ for Loops

# for letter in "Giraffe Academy":
#     print(letter)
# #
# friends = "jim","Karen","Kevin"
# # for friend in friends:
# #     print(friend)
# #
# # for index in range(3,10):
# #     print(index)
#
# for index in range(len(friends)):
#     print(friends[index])
#
# for index in range(5):
#     if index == 0:
#         print("first iteration ")
#     else:
#         print("not first")

#print(2**3) ####### exponents functions


# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
#
# print(raise_to_power(2,3))

#
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# for row in number_grid:
#     #print(row)
#     for column in row:
#         print(column)
#

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase")))