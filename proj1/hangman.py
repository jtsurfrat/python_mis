import random
from random import randint
import os
import sys
#
#
# words = [
#     'apple',
#     'banana',
#     'orange',
#     'coconut',
#     'lime',
#     'grapefruit',
#     'lemon',
#     'kumquat',
#     'blueberry',
#     'melon'
# ]
#
# while True:
#     start = input("Press enter/ return to start, or enter 'Q' to quit")
#     if start.lower() =='q':
#         break
#     # pick a random word
#     secret_word = random.choice(words)
#     bad_guesses = []
#     good_guesses = []
#     # make a list of words
#
#
#     while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
#         #draw guess
#         # draw letters and strikes
#         for letter in secret_word:
#             if letter in good_guesses:
#                 print(letter, end='')
#             else:
#                 print("-", end='')
#         print('')
#         print('Strikes: {}/7'.format(len(bad_guesses)))
#         print('')
#     # take guess
#         guess = input("Guess a letter: ").lower()
#     # print out win / lose
#
#         if len(guess) != 1:
#             print("You can only guess a single letter!")
#             continue
#         elif guess in bad_guesses or guess in good_guesses:
#             print("You've already guess that letter!")
#             continue
#         elif not guess.isalpha():
#             print("You can only guess letters")
#             continue
#
#         if guess in secret_word:
#             good_guesses.append(guess)
#             if len(good_guesses) == len(list(secret_word)):
#                 print("You win! The word was {}".format(secret_word))
#                 break
#         else:
#             bad_guesses.append(guess)
#     else:
#         print("You didn't guess it! My secret_word was {}".format(secret_word))
#
#
#


# def random_item(word):
#     index = 0
#     randomize = randint(index, len(word))
#     randomize = randomize - 1
#     if randomize <= 0:
#         randomize = 0;
#     print(randomize)
#
#
#     for letter in word:
#         if(index == randomize):
#             print(index, letter, "This is it")
#             return letter
#         index += 1
#         print(index,letter)
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"


#
# random_item("Treehouse")


# def random_item(thestring):
#     print(random.randint(0, len(thestring)-1))
#     return random.randint(0, len(thestring)-1)
#
# random_item("somethingrandom")


# def random_item(word):
#     index = 0
#     randomize = randint(index, len(word))
#     randomize = randomize - 1
#     if randomize <= 0:
#         randomize = 0;
#     print(randomize)
#
#
#     for letter in word:
#         if(index == randomize):
#             print(index, letter, "This is it")
#             return letter
#         index += 1
#         print(index,letter)
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"




words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

# clears screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('')
    print('Strikes: {}/7'.format(len(bad_guesses)))

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')
    # draw letters and strikes
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print("-", end='')
    print('')


def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        # print out win / lose
        if len(guess) != 1:
            print("You can only guess a single letter!")
            #continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guess that letter!")
            #continue
        elif not guess.isalpha():
            print("You can only guess letters")
            #continue
        else:
            return guess

def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}". format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret_word {}".format(secret_word))
                done = True

        if done:
            play_again = input("Do you want to play again? Y/n ").lower()
            if play_again != "n":
                done = False
                play(done)

            else:
                print("Bye!")
                sys.exit()
def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True
print("Welcome to letter Guess!")

done = False

while True:
    clear()
    welcome()
    play(done)

play()













#
