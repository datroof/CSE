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

"""def print_hw():
    print("Hello World.")
    print("Enjoy the day.")


# Indent is 4 spaces.

print_hw()


def say_hi(name):  # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Matthew")
# Inputs are ALWAYS of type String!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


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

c = '1'
print(c == 1) # we have a string ans an integer
print(int(c) == 1)
print(c == str(1))




# comparisons
print (1 == 1) # use a double equal sign

print(1 != 2) # is not equal to 2
print(not False)
"""




# lists
"""
the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', 'meat', 'sauce', 'sesame seed bread', 'avocado']
print(cheeseburger_ingredients[0])
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))
print(len(the_count))

# going through lists

for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for number in the_count:
    print(number * 2)

length = len(cheeseburger_ingredients)
range(5)  # A list of numbers 0 through 4
range(len(cheeseburger_ingredients)) # Generates a list of all indices

for number in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[number]
    print("The item at index %d is %s" % (number, item))


# Recasting into a list
strOne = "Hello World!"
listOne = list(strOne)
print(listOne)
listOne[11] = '.'
print(listOne[-1])

# Adding things to a list.

cheeseburger_ingredients.append("Fries")
print(cheeseburger_ingredients)
cheeseburger_ingredients.append("Pickles")

# Remove things from a list.

cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things lowercase
strTwo = "ThIs Is A VeRY oDd sEnTeNCe"
lowercase = strTwo.lower()
print(lowercase)

"""

# Dictionaries - Made up of key: value pair

dictionary = {"name": 'George', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictionary.
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])
dictionary["profession"] = "telemarketer."
large_dictionary = {
    'CA':'California',
    'AZ':'Arizona',
    'NY' : 'New York'
}
print(large_dictionary['NY'])

larger_dictionary = {

    'CA':[
        'Fresno',
        "San Fransisco"
    ],
    'AZ':[
        "Phoenix",
        "Tusoon"
    ],
    'NY':[
        "New York City",
        'Brooklyn'
    ]

}

print(larger_dictionary['NY'][1])
print(larger_dictionary['AZ'][0])
print(larger_dictionary['AZ'][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'Population': 39250000,
        'Border ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'Name': 'Arizona',
        'Population': 6931000,
        'Border ST:': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'Name': 'New York',
        'Population': 19750000,
        'Border ST':[
            'Vermont',
            'Massachusetts',
            'Connections',
            'Pennsylvania',
            'New Jersey'
        ]
    },
}
current_node = largest_dictionary['NY']
print(current_node['Name'])
print(current_node['Population'])
print(largest_dictionary)

