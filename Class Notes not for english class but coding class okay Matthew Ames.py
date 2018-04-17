# Defining a class
class Cheeseburger(object):
    def __init__(self, patty, cheese):  # TWO underscores before and after.
        self.patty = patty
        self.cheese = cheese
        self.eaten = False

    def \
            give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You eat the cheeseburger")
        self.eaten = True


# instancing(the creation of) two cheeseburgers
burger1 = Cheeseburger("Beef", "Swiss")
burger2 = Cheeseburger("Bacon", "Hawarti")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)

# A car can drive, accelerate, start up, stop, race, roll up and down it's windows, use windsheild wipers, spin their
# tires, crash, blow up, break, spinout.


class Car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passenger = 0
        self.name = name
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing Happens")
        else:
            self.running = True
            print("The car starts.")

    def move_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You move forward.")
        else:
            print("The car is already off.")

    def go_for_drive(self, passengers):
        print("%d passengers get in" % passengers)
        self.passenger = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out" % passengers)
        self.passenger = 0


my_car = Car("Patty Mobile", "Patty Color", 0, 9000)


my_car.go_for_drive(5)