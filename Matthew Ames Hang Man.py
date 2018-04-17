import random
import string
"""
This is a guide of
how to make Hangman.

1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Hide and reveal letters
5. Create win and lose conditions

"""

guesses_left = 10

word_bank = ['Skidaddle Skidoodle', 'Ugandan Knuckles', 'But can you do this?', 'Boneless Pizza', 'Tidepods',
             'SOMEBODY TOUCHA MY SPAGHET!!!', 'Shrek is love', 'Bob the fortune cookie', 'REEEEEEEE', 'Pepe the grinch']
random_word = random.randint(0, 9)
broken_word = word_bank[random_word]
listbroken_word = list(broken_word)
letters_guessed = list(string.punctuation)
letters_guessed.append(" ")
# print(letters_guessed)
guess = ''

win = False

while guesses_left != 0 and not win:

    print("You have %s guesses left." % guesses_left)
    output = []

    for letter in broken_word:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append('*')
    print("".join(output))

    if output == list(broken_word):
        win = True
        continue
    guess = input(">_")

    if guess not in broken_word.lower():
        guesses_left -= 1
    letters_guessed.append(guess.lower())

# print(letters_guessed)
if guesses_left == 0:
    print("You lost.")
else:
    print("You win")





