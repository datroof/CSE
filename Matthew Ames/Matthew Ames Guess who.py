import random
# remember inputs from uses are always
# of type string !!!
#1. generate a number
#2. Ask the user for an imput(number)
#3. Does the guess match the number?
#4. Add "higher" and "lower"
#5. Add five guesses
guesses = 5
winning_integer = random.randint(1,10)
print(winning_integer)
print("Guess an integer between one and ten")
guess = input(">_ ")
if int(guess) == winning_integer:
    print("Yay")
    print(guesses)
elif int(guess) > winning_integer:
    guesses -= 1
    print("Too high")
    if int(guess) == winning_integer:
        guesses -= 1
        print("Yay")
        print(guesses)
elif int(guess) < winning_integer:
    guesses -= 1
    print("Too low")
    print(guesses)





