class Character(object):
    def __init__(self, chrdes, name, talk, sectalk):
        self.name = name
        self.chrdes = chrdes
        self.talk = talk
        self.sectalk = sectalk
        self.hungry = True
        self.luck = False

    def eat(self):
        if self.hungry:
            print("You are eaten.")
            bum_joe.hungry = False


print("You need eating.")
bum_joe = Character("Bum Joe.", "You are a hobo.", "Hello there. Can I have money?", "Thank you for da munie.")
while True:
    command = input(">_")

    if command == "eat":
        bum_joe.eat()
    elif command == 'quit':
        exit('If you make a spontanious facial movement while watching this series of moving images, it\n will directly'
             ' lead to the implication that you have shown amusement while doing so, meaning you\n'
             ' have failed my challenge. In other words... YOu LaUgH, yOu lOoSe.')
    if command == "hello":
        print(bum_joe.talk)
    if command == "give money":
        print(bum_joe.sectalk)

