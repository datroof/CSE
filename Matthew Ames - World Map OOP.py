class Settings:
    win_condition = False
    toilet_used = False
    real_penny = False
    quest = False
    flashlight_on = False
    quest_num = 0
    gave_penny = False
    gave_quarter = False
    gave_dime = False
    gave_nickel = False
    pls_print = True
    num_flash = 0
    add_flash_b = True
    add_flash_f = True
    took_penny = False


print("Welcome to the world of Starving Hobo.")
response = input("Would you like to learn the rules of the game?\n"
                 ""
                 "yes/no?")
if response.lower() == "yes":
    print("Welcome to my game, to the world of Starving Hobo.\n"
          "\n"
          "Jest letting you know now, the only actions are:\n"
          "use\n"
          "talk\n"
          "take\n"
          "give\n"
          "open\n"
          "i (you type in i to check your inventory)\n"
          "\n"
          "You need to type in an action by itself.\n"
          "\n"
          "The game will then ask you to specify your request.\n"
          "\n"
          "For example:\n"
          "player: use\n"
          "game: Use what?\n"
          "player: hat\n"
          "game: You used hat.\n"
          "\n"
          "You need to type in a direction to move that way.\n"
          "These directions are:\n"
          "north/n\n"
          "west/w\n"
          "south/s\n"
          "east/e\n"
          "\n"
          "Now that you know how to play, let's begin your adventure as a Starving Hobo.\n"
          "P.S... Scroll up to read the directions.\n"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "\n")
else:
    print("Ok then. Good luck.\n"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "\n")


class Room(object):
    def __init__(self, name, description, dark, objects, north, east, south, west, locked, chr):
        self.name = name
        self.description = description
        self.dark = dark
        self.objects = objects
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.locked = locked
        self.chr = chr

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Character(object):
    def __init__(self, chrdes, name, talk, sectalk, spoke):
        self.chrdes = chrdes
        self.name = name
        self.talk = talk
        self.sectalk = sectalk
        self.spoke = False
        self.hungry = True
        self.luck = 0

    def talk(self):
        self.spoke = True


class Item(object):
    def __init__(self, name, taken, used, dropped):
        self.name = name
        self.taken = taken
        self.used = used
        self.dropped = dropped


class Coin(Item):
    def __init__(self, name, taken, used, dropped, given):
        super(Coin, self).__init__(name, taken, used, dropped)
        self.given = False

    def give(self):
        self.given = True

    def take(self):
        self.taken = True


class Dime(Coin):
    def __init__(self, taken, used, dropped, given):
        super(Dime, self).__init__('dime', taken, used, dropped, given)

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the dime to George.")
        secinv.append(dime)
        inventory.remove(dime)


class Penny(Coin):
    def __init__(self, taken, used, dropped, given):
        super(Penny, self).__init__('penny', taken, used, dropped, given)

    def take(self):
        if Settings.took_penny is True:
            print("There are only fake pennies left.")
        elif Settings.took_penny is False:
            self.taken = True
            Settings.took_penny = True

    def give(self):
        self.given = True
        print("You gave the penny to George.")
        secinv.append(penny)
        inventory.remove(penny)


class Nickel(Coin):
    def __init__(self, taken, used, dropped, given):
        super(Nickel, self).__init__('nickel', taken, used, dropped, given)

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the nickel to George.")
        secinv.append(nickel)
        inventory.remove(nickel)


class Quarter(Coin):
    def __init__(self, taken, used, dropped, given):
        super(Quarter, self).__init__('quarter', taken, used, dropped, given)

    def take(self):
        self.taken = True

    def give(self):
        self.given = True
        print("You gave the quarter to George.")
        secinv.append(quarter)
        inventory.remove(quarter)


class Pizza(Item):
    def __init__(self, taken, used, dropped):
        super(Pizza, self).__init__('pizza', taken, used, dropped)
        self.eaten = False

    def use(self):
        self.eaten = True
        print("You ate the pizza.")
        bum_joe.hungry = False
        self.name = "pizza crumbs"
        bum_joe.luck += 1
        print("Your luck is %s" % bum_joe.luck)


class Key(Item):
    def __init__(self, name, taken, used, dropped):
        super(Key, self).__init__(name, taken, used, dropped)

    def use(self):
        self.used = True


class Code(Key):
    def __init__(self, taken, used, dropped):
        super(Code, self).__init__('code', taken, used, dropped)

    def use(self):
        self.used = True
        print("You used the passcode, the door opens.")


class Chestkey(Key):
    def __init__(self, taken, used, dropped):
        super(Chestkey, self).__init__('chest key', taken, used, dropped)

    def use(self):
        self.used = True
        print("You used the chest key. The chest opens")


class Batteries(Item):
    def __init__(self, taken, used, dropped):
        super(Batteries, self).__init__('batteries', taken, used, dropped)

    def use(self):
        self.used = True
        print("You put the batteries in the flashlight.")


class Flashlight(Item):
    def __init__(self, taken, used, dropped):
        super(Flashlight, self).__init__('flashlight', taken, used, dropped)
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
    def __init__(self, taken, used, dropped, equipped):
        super(Highheels, self).__init__('high heels', taken, used, dropped, equipped)
        self.used = False

    def use(self):
        if self.used is True:
            print("You already used that.")
        elif self.used is False:
            super(Highheels, self).equip()
            print("You put on the high heels. You feel fabulous.")
            self.used = True
            bum_joe.luck += 1
            print("Your luck is %s" % bum_joe.luck)


class Hat(Clothes):
    def __init__(self, taken, used, dropped, equipped):
        super(Hat, self).__init__('hat', taken, used, dropped, equipped)
        self.equipped = False
        self.used = False

    def use(self):
        if self.used:
            print("You already used that.")
        elif self.used is False:
            super(Hat, self).equip()
            self.equipped = True
            self.used = True
            bum_joe.luck += 1
            print("You put on the hat. You feel fabulous.")
            print("Your luck is %s" % bum_joe.luck)



class Button(Item):
    def __init(self,name, taken, used, dropped):
        self.name = 'button'
        self.taken = taken
        self.dropped = dropped

    def use(self):
        if not self.use:
            self.used = False
            print("You broke the button when you pressed it, so you can't press it again.")
        else:
            self.used = True
            print("You press the button. Nothing happens, but you feel luckier.")


secinv = []

high_heels = Highheels(False, False, False, False)

hat = Hat(False, False, False, False)

dime = Dime(False, False, False, False)

quarter = Quarter(False, False, False, False)

flashlight = Flashlight(False, False, False)

batteries = Batteries(False, False, False)

chestkey = Chestkey(False, False, False)

code = Code(False, False, False)

pizza = Pizza(False, False, False)

penny = Penny(False, False, False, False)

nickel = Nickel(False, False, False, False)

button = Button('button', False, False, False )

bum_joe = Character("You are a hobo. That's all you need to know. Also, you wet the bed until you were seven.",
                    "Bum Joe.", None, None, False)

ugandan_knuckles = Character("It reminds you of a character from a show you used to watch.", "Ugandan Knuckles",
                             "You wish to know da wae? Here is a code. It shall help u on your jerney.\n"
                             " Farewell..."
                             ""
                             "He disappeared.", None, False)

george = Character("He has a trench coat and a key around his neck.", "George", "So you want this key? "
                   "If you want it, then you're gonna\n"
                   "have to give me 4 things: a dime, a penney, a nickle, and a quarter.\n"
                   "I'm gonna tag along with you.", None, False)

hdum = Room("Home Dumpster.", "Every hobo in the Istan Allies owns a dumpster, this one's yours.\n In it is a chest that"
                           " you really wanna open. There are allies to the North, South, East and West of you\n"
                           ". There's also a hat. You like the color.",
            False, hat, "na", "rdum", "dwpc", "ugkn", False, None)
na = Room("North Alley.", "To the west of you is the entrance to an Abandoned Apt. The Alley continues north.", False,
          'none', "corner", None, "hdum", "abap", False, None)
corner = Room("Corner.", "You are hungry. To the west of you is a dumpster with a slice of pizza in it. \n"
              "to the east of you is an alley with a mysterious looking figure at the end of it.",
              False, 'none', None, "mwk", "na", "fdum", False, None)
abap = Room("Abandoned Apartment.", "The apt. is mostly empty except for a dime.", True,
            dime, None, "na", None, None, False, None)
fdum = Room("Dumpster with Food.", "On top of a pile of black garbage bags lay a perfectly fine slice of pizza. \n"
                                   "To the north of you is a ghostly looking toilet. To the west of you is a \n"
                                   "mysterious door that is open.",
            False, pizza, "ghto", "corner", None, "pero", False, None)
ghto = Room("Ghostly Toilet.", "The toilet is dimly lit by a fading bulb. To the west of you is a stand-alone sink\n"
                               "with no knobs and a faucet that's the size of a baseball. Pretty odd.", False,
            'none', None, None, "fdum", "sink", False, None)
pero = Room("Penny Room.", "The door lead you to a small room, with nothing but pennies in it. Upon further inspection"
                           ",\n all of the pennies appear to be fake. There's a sign on the far wall that reads,\n'"
                           "One of these is real'.",
            False, "fake penny", None, "fdum", None, None, False, None)
sink = Room("Sink.", "The sink is really weird. It has no knobs to turn the water on, and the faucet the water\n"
                     "would've come out of is the size of a baseball. There must be a way to turn it on.", False,
            nickel, None, "ghto", None, None, False, None)
mwk = Room("Man with key.", "Upon further inspection, the figure is actually a man in a black trench coat \n"
                            "with a mask covering his face. Around his neck is a chain with a key around it.\n"
                            "It might be the key you're looking for. You think his name is George",
           False, None, "abshe", None, "rdum", "corner", False, george)
abshe = Room("Abandoned shop entrance.", "The door is open and when looking inside you can't see anything. \n"
                                         "There is a button on the wall to the west of you with a sign above\n"
                                         " it that says 'Warning: Pointless button. You wanna press it.", False, None,
             "absh", 'none', "mwk", "pobu", False, None)
absh = Room("Abandoned shop.", "The shop is mostly empty except for a cash register. In the cash register\n"
                               "is a single quarter.", True, quarter, None, None, "abshe", None, False, None)
pobu = Room("Pointless button.", "The button is big and red. You really want to push it.",
            False, button, None, "abshe", None, None, False, None)
rdum = Room("Red Dumpster.", "When looking in the red dumpster, you see there is a flashlight.\n"
                             " To the north of you is a mysterious looking figure staring at you.", False,
            flashlight, "mwk", None, None, "hdum", False, None)
dwpc = Room("Door with pass code.", "On the door is an input thingy with a dialpad. You input the code you got(1234). "
                                    "The door opens to reveal a small room to the east.",
            False, 'none', "hdum", "bioc", None, None, True, None)
bioc = Room("Batteries in open chest.", "You already know what's in here.",
            False, batteries, None, None, None, "dwpc", False, None)

ugkn = Room("Ugandan Knuckles.", "There is a small red creature in front of you that reminds you of a character from \n"
            "a show you used to watch as a child... before you were homeless. It's kinda deformed.",
            False, code, None, "hdum", "hihe", None, False, ugandan_knuckles)
hihe = Room("Room with High heels.", "There are fabulous red high heels just laying there. You think you'd \n"
                                     "feel fabulous in them.",
            False, high_heels, "ugkn", None, None, None, False, None)


def use_menu():
    use_response = input("Use what?")
    found = False
    try:
        if use_response.lower() == 'button' and button.used is True:
            print("You broke the button when you pressed it, so you can't do it again.")
            found = True
        elif use_response == 'button':
            button.use()
            button.used = True
            bum_joe.luck += 1
            print("Your luck is %s" % bum_joe.luck)
            found = True
        elif use_response == "toilet" and current_node == ghto:
            print("You flush the toilet. You hear a sound to the west of you. When you look over,\n"
                  " you see that a nickel had fallen out of the faucet.")
            Settings.toilet_used = True
            found = True
        for pos in range(len(inventory)):
            if use_response != "toilet" or "button":
                if inventory[pos].name == use_response:
                    item = inventory[pos]
                    item.use()
                    found = True
        if not found:
            print("You don't have that.")
    except AttributeError:
        print("You don't need to use that.")


def open_menu():
    open_response = input("Open what?")
    if open_response == "chest" and current_node == hdum and Settings.win_condition is False and chestkey in inventory:
        print("You open the chest. The chest opens to reveal a scratcher.\n"
              "\n"
              "You decide to play the scratcher.\n"
              "\n"
              "You weren't lucky enough. You lost the scratcher.\n"
              "You are still a hobo. You are still broke. You did all that for nothing.\n"
              "\n"
              "Congratulations! You got the bad ending.")
        exit(0)
    elif open_response == "chest" and current_node == hdum and Settings.win_condition is True and chestkey in inventory:
        print("You open the chest. The chest opens to reveal a scratcher.\n"
              "\n"
              "You decide to play the scratcher.\n"
              "\n"
              "You luck pays off. To your utmost amazement, you won... $500,000.\n"
              "\n"
              "With this amount of money, you can go back to school and finish your education.\n"
              "\n"
              "You can then get a job and make money... if you spend your money just right...\n"
              "\n"
              "You won't be homeless anymore.\n"
              "\n"
              "Congratulations! You got the good ending.")
        exit(0)


current_node = hdum
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
take = ['take']
use = ['use']
talk = ['talk']
open_commands = ['open']
drop = ['drop']
give = ['give']
inventory = []

current_chr = bum_joe


while True:
    if Settings.num_flash == 2:
        Settings.flashlight_on = True
    if flashlight in inventory and Settings.add_flash_f is True:
        Settings.num_flash += 1
        Settings.add_flash_f = False
    if batteries in inventory and Settings.add_flash_b is True:
        Settings.num_flash += 1
        Settings.add_flash_b = False
    if bum_joe.luck >= 2:
        Settings.real_penny = True
    if bum_joe.luck == 4:
        Settings.win_condition = True
    if current_node == pero and Settings.real_penny is True and Settings.took_penny is False:
        print()
        pero.objects = penny
    else:
        pero.objects = None
    if penny.given and Settings.gave_penny is False:
        Settings.quest_num += 1
        Settings.gave_penny = True
    if dime.given and Settings.gave_dime is False:
        Settings.quest_num += 1
        Settings.gave_dime = True
    if quarter.given and Settings.gave_quarter is False:
        Settings.quest_num += 1
        Settings.gave_quarter = True
    if nickel.given and Settings.gave_nickel is False:
        Settings.quest_num += 1
        Settings.gave_nickel = True
    if Settings.quest_num == 4:
        print("George speaks to you.")
        Settings.quest = True
        if Settings.pls_print is True:
            print("\n"
                  "Thank you for giving me all the items I need to start the ritual.\n"
                  "The ritual to end all the knuckles.\n"
                  "Their reign of terror ends here!\n"
                  "\n"
                  "George disappears. You feel conflicted about these knuckles people...but you're too tired to care.\n"
                  "\n"
                  "You got the key.\n"
                  "\n")
            inventory.append(chestkey)
            Settings.quest_num = 0
            Settings.pls_print = False

    elif current_node == pero and bum_joe.luck >= 2:
        print("The door lead you to a small room, with nothing but pennies in it. Upon further inspection"
              ",\n all of the pennies appear to be fake. There's a sign on the far wall that reads,\n'"
              "One of these is real'.")
    elif current_node == absh and current_node.objects is None:
        print("You are in the abandoned shop. Apparently, \n"
              "the only thing in here was a quarter. Odd.")
    elif current_node == abap and current_node.objects is None:
        print("You are in the abandoned apt. Apparently, \n"
              "the only thing in here was a dime. Odd.")
    elif current_node == pero and penny in inventory:
        print("The room now has nothing but fake pennies in it.")
    elif current_node == pero and penny in secinv:
        print("The room now has nothing but fake pennies in it.")
    elif current_node.locked and code not in inventory:
        print("You come to a door with a dialpad. You need to input a 4-digit code to open it. \n"
              "You don't know the code.")
    elif current_node == bioc and current_node.objects is None:
        print("You are in the room where you got the batteries. \n"
              "There is nothing else of interest here.")
    elif current_node == sink and Settings.toilet_used is True and nickel not in inventory:
        print("You look in the sink where you heard the clinking sound. You see there is\n"
              " a nickel. How this actually worked, you'll probably never know, nor will\n"
              " you question it.")
    elif current_node == sink and current_node.objects is None:
        print("You're at the weird sink. How it works, you'll never know.")
    elif current_node == ugkn and code in inventory:
        print("You are where the mysterious creature used to be. You hope he finds da wae.")
    elif current_node == rdum and flashlight in inventory:
        print("You are at Red Dumpster. To the north of you is a mysterious\n"
              " looking figure staring at you.")
    elif current_node.dark and Settings.flashlight_on is False:
        print("It is too dark to see. You need flashlight and batteries.")
    elif current_node == hdum and hat in inventory:
        print("You are at Home Dumpster. Every hobo in the Istan Allies owns a dumpster, this one's yours.\n"
              "In it is a chest that you really want to open. There are allies to the North, South, East, and"
              " West of you. ")
    elif current_node == hihe and high_heels in inventory:
        print("You are in the room where the high heels used to be.")
    elif current_node == fdum and pizza in inventory:
        print("You are at a dumpster full of garbage. To the north of you is a ghostly looking toilet.\n"
              " To the west of you is a mysterious door that is open.")
    elif current_node == corner and bum_joe.hungry is False:
        print("To the west of you is a dumpster with garbage bags in it. To the east of you is a weird figure at\n"
              "the end of an alley.")
    else:
        print("You are at", current_node.name, current_node.description)  # change
    command = input('>_').lower().strip()

    if command in talk:
        response = input("To who?").lower().strip()
        try:
            if response == current_node.chr.name.lower() and current_node.chr.spoke is False:
                current_chr = current_node.chr
                print(current_chr.talk)
                current_chr.spoke = True
                if current_chr.spoke is True and current_chr == ugandan_knuckles:
                    print("You got the code.")
                    inventory.append(code)
            elif current_chr.name.lower != response.lower():
                print("He or she is not there.")
        except AttributeError:
            print("He or she is not there.")

    if command == 'quit':
        quit(0)
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("Your legs won't move in that direction.")
    if command in take:
        try:
            response = input("Take what?")
            if response.lower() == 'button':
                print("You can't take that.")
            elif response.lower() == 'chest key':
                print("You can't steal from poor people, meanie.")
            elif response.lower() == 'key':
                print("You can't still from poor people, meanie.")
            elif response == current_node.objects.name:
                current_object = current_node.objects
                inventory.append(current_object)
                current_node.objects = None
                print("You take %s" % current_object.name)
            else:
                raise NameError
            if response.lower() == "penny" and current_node == pero and bum_joe.luck >= 2:
                print("You feel lucky. You pick up the first penny you see. It turns out to be real.")
                Settings.took_penny = True
            if response.lower() == "penny" and penny in inventory or penny in secinv:
                print("There are only fake pennies left.")
        except NameError:
            print("It's not there.")
        except AttributeError:
            print("It's not there.")

    if command in give:
        try:
            response = input("Give what?")
            found = False
            i = 0
            while i < len(inventory) and not found:
                if inventory[i].name == response:
                    item = inventory[i]
                    item.give()
                    print("You no longer have the %s." % response)
                    found = True
                i += 1
        except AttributeError:
            print("You don't need to give that away.")
    if command in use:
        use_menu()
    if command in open_commands:
        open_menu()
    if command == 'i':
        print()
        print("You have:")
        for item in inventory:
            print(item.name)
        print()

else:
    print("Welp, I'm feeling a little stupid right now, cause I can't act out my own thoughts.")
