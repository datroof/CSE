# Defining functions
def hello_world():
    print("Hello world.")


hello_world()


def square_it(number):
    return number ** 2


print(square_it(3))


def bill_plus_tip_calc(tots):
    tax_amt = tots * 0.18
    total_bill = tots + tax_amt
    return total_bill

print("You bill is $%d" % bill_plus_tip_calc(72))


def distance_calc(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5
    return answer


print(distance_calc(0,0,3,4))


def pythgorean(a, b):
    inside = a ** 2 + b ** 2
    answer = inside ** 0.5
    return answer

print(pythgorean(4, 9))