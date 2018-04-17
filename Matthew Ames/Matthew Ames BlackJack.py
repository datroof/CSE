import random
import sys
deal = random.randint(2, 21)
draw = random.randint(1, 11)
dealer_hand = random.randint(10, 21)
choice = input
hand = deal + draw
your_hand = random.randint(2, 21)


print(your_hand)


choice = int(input("Wanna stay or hit?"))

if your_hand <= 21:
    while choice == 1:
        your_hand = your_hand + random.randint(1, 11)
        print("You got a %s" % your_hand)

        if your_hand >= 22:
            print("You busted")
            sys.exit(0)
        choice = int(input("Wanna stay or hit?"))
    if choice == 1:
        your_hand = your_hand + random.randint(1, 11)
        print("You got %s" % your_hand)
        print("The dealer got %s" % dealer_hand)

        if your_hand >= 22:
            print("You busted.")
        elif dealer_hand <= your_hand <= 21:
            print("You won.")
        elif dealer_hand >= your_hand:
            print("You lost.")
        elif dealer_hand == your_hand:
            print("It's a tie.")

    else:
        if choice == 2:
            print("You got %s" % your_hand)
            print("The dealer got %s" % dealer_hand)
        elif dealer_hand <= 16:
            print("The dealer chooses to hit himself.")
            dealer_hand = dealer_hand + random.randint(1, 11)
            print("The dealer now has %s" % dealer_hand)

        elif dealer_hand >= 22:
            print("The dealer busted. You won.")
            sys.exit(0)

        if dealer_hand < your_hand <= 21:
            print("You won.")
        elif dealer_hand > your_hand:
            print("You lost.")
        elif dealer_hand == your_hand:
            print("It's a tie.")
        elif your_hand >= 22:
            print("You busted.")
else:
    print("You busted.")
