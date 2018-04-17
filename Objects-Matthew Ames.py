class Item(object):
    def __init__(self, name, taken, used, dropped):
        self.name = None
        self.taken = False
        self.used = False
        self.dropped = True

    def take(self):
        self.taken = True


class Coin(Item):
    def __init__(self, name, taken, used, dropped, given):
        super(Coin, self). __init__(name, taken, used, dropped)
        self.name = 'coin'
        self.given = False

    def take(self):
        self.taken = True

    def give(self):
        self.given = True


class Dime(Coin):
    def __init__(self, name, taken, used, dropped, given):
        super(Dime, self).__init__(name, taken, used, dropped, given)
        self.name = 'dime'

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the dime to a hobo.")


class Penny(Coin):
    def __init__(self, name, taken, used, dropped, given):
        super(Penny, self).__init__(name, taken, used, dropped, given)
        self.name = 'penny'

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the penny to a hobo.")


class Nickel(Coin):
    def __init__(self, name, taken, used, dropped, given):
        super(Nickel, self).__init__(name, taken, used, dropped, given)
        self.name = 'nickel'

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the nickel to a hobo.")


class Quarter(Coin):
    def __init__(self, name, taken, used, dropped, given):
        super(Quarter, self).__init__(name, taken, used, dropped, given)
        self.name = 'quarter'

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the quarter to a hobo.")


class Pizza(Item):
    def __init__(self, name, taken, used, dropped, eaten):
        super(Pizza, self).__init__(name, taken, used, dropped)
        self.eaten = False

    def eat(self):
        self.eaten = True
        print("You ate the pizza.")


class Key(Item):
    def __init__(self, name, taken, used, dropped):
        super(Key, self).__init__(name, taken, used, dropped)

    def use(self):
        self.used = True

class Code(Key):
    def __init__(self, name, taken, used, dropped):
        super(Code, self).__init__('code', taken, used, dropped)

    def use(self):
        self.used = True
        print("You used the passcode, the door opens.")


class Chestkey(Key):
    def __init__(self, name, taken, used, dropped):
        super(Chestkey, self).__init__('chest key',taken, used, dropped)

    def use(self):
        self.used = True
        print("You used the chest key. The chest opens")


class Batteries(Item):
    def __init__(self, name, taken, used, dropped):
        super(Batteries, self).__init__(name, taken, used, dropped)
        self.name = 'batteries'

    def use(self):
        self.used = True
        print("You put the batteries in the flashlight.")


class Flashlight(Item):
    def __init__(self, name, taken, used, dropped, on):
        super(Flashlight, self).__init__(name, taken, used, dropped)
        self.name = 'flashlight'
        self.on = False

    def on(self):
        self.on = False
        print("The flashlight is off.")

    def use(self):
        self.used = True
        self.on = True
        print("You turn the flashlight on. You see a lot a dead memes.")


class Clothes(Item):
    def __init__(self, name, taken, used, dropped, equipped):
        super(Clothes, self).__init__(name, taken, used, dropped)
        self.equipped = False

    def equip(self):
        if not self.equipped:
            self.equipped = True
        else:
            self.equipped = False


class Highheels(Clothes):
    def __init__(self, name, taken, used, dropped, equipped):
        super(Highheels, self).__init__('high heels', taken, used, dropped, equipped)

    def use(self):
        super(Highheels, self).equip()
        print("You put on the high heels. You feel fabulous.")


class Hat(Clothes):
    def __init__(self, taken, used, dropped, equipped):
        super(Hat, self).__init__('hat', taken, used, dropped, equipped)
        self.equipped = False

    def use(self):
        super(Hat, self).equip()
        print("You put on the hat. You feel fabulous.")


hat = Hat(False, False, False, False)
print(hat)