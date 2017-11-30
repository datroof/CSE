# print("Hello World")
#
# # Matthew
#
# a = 4
# b = 3
#
# print(3+5)
# print(5-3)
# print(6/2)
# print(3 ** 2)
#
# print("Try to figure out how this works")
# print(13 % 2)
#
# # The sign is a modulus. It finds the remainder.
#
# car_type = "BPW"
# car_name = "Weeaboo steve"
# car_cylinders = 8
# car_mpg = 5000.9
#
# print("i have a car called %s. It's pretty nice."% car_name)
# print("I have a car called %s. It's a %s." % (car_name, car_type))
#
# # Here is where fancy happens.
# print("What is your name?")
# name = input(">_ ")
# print("Hello %s." % name)
#
# age = input("How old are you")
# print("%s?! That's really old! You should die now." %age)
#
# print("Pickle Rickerickerickerickerickericker")
# print("What's your dream in life?")
# dream = input(">_ ")
# print("Wow, %s, really?" % dream)
#
# #Function


def print_hw():
    print("Hello World.")
    print("Enjoy the day.")


# Indent is 4 spaces.

print_hw()


def say_hi(name):  # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Matthew")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1 # age = age + 1
    print("Next year. %s will be %d years old" % (name, age))


print_age("Matthew", 15)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x - 4
print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements

def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # else of
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc (69.99999999999999999999999999999999999999999999999999999999999999999))


def happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear %s" % name)
    print("Happy birthday to you")


happy_birthday("Matthew")


# loops

for num in range(10):
    print(num +1)


a = 1
while a < 10: # this is the condition, it must be true to execute.

    print(a)
    a += 1  # This iterate so that we can break this loop.


# Random Numbers
import random # This should be on line one1
print (random.randint(1, 10))