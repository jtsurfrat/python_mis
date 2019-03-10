from random import randint

# generate a random number between 1 and 10

# computer_guess = randint(0,10)
# print(computer_guess)
# number_guesses = 0
#
# while number_guesses < 3:
#     user_guess = input("""
#                         Please choose an number between 1 and 10,
#                         you have guessed {} times
#                         """.format(number_guesses))
#     user_guess = int(user_guess)
#     if user_guess == computer_guess:
#         print("You won")
#         break
#     elif user_guess < computer_guess:
#         print("higher")
#         number_guesses += 1
#         continue
#     elif user_guess > computer_guess:
#         print("Lower")
#         number_guesses += 1
#         continue
#     # elif isinstance(user_guess, int):
#     #     print("Thats not a number. ")
#     #     continue
#
# if number_guesses >= 3:
#     print("You lost, you guessed {} times".format(number_guesses))
# else:
#     print("You won, you guessed {} times".format(number_guesses))

# safely make an int
# limit guesses
# too high
# too Low
# play again

#########################################
# number game
##########################################

# def game():
#     # generate a random number between 1 and 10
#     secret_num = randint(1, 10)
#     guesses = []
#
#     print(secret_num)
#
#     while len(guesses) < 5:
#         try:
#             #get a number guess from player
#             guess = int(input("Guess a number between 1 - 10: "))
#         except ValueError:
#             print("{} isn't a number!".format(guess))
#             continue
#         else:
#             #compare guess to secret number
#             if guess == secret_num:
#                 print("You got it! My number was {}".format(secret_num))
#                 break
#             elif guess < secret_num:
#                 print("It's higher")
#             else:
#                 print("It's Lower")
#             guesses.append(guess)
#     else:
#         print("You didn't get it. It was {} ".format(secret_num))
#     play_again = input("Do You want to play again Y/N? ")
#     if play_again.lower() != 'n':
#         game()
#     else:
#         print("Bye!")
#
# game()

# def just_right(number_char):
#     #number_char = len(number_char)
#     if len(number_char) < 5:
#         print("Your string is too short")
#         return "Your string is too short"
#     elif len(number_char) > 5:
#         print("Your string is too long")
#         return "Your string is too long"
#     else:
#         print(True)
#         return True
#
#
# just_right("bacon1")
# just_right("cat")
# just_right("bacon")


##########################
# square challenge 4.5
########################


# def squared(num):
#     try:
#         num = int(num) #try to turn num into integer
#         return num * num #try to return num squared
#     except: #if an error comes up
#         return num * len(num) #just return num multiplied by its length
#

def game():
    help = print("Welcome to computer guess' number game")
    my_number = int(input("Choose a number"))
    number_guesses = 0
    high_guess = 10
    low_guess = 1

    while number_guesses < 3:
        computer_guess = randint(low_guess,high_guess)
        print(computer_guess)
        if my_number == computer_guess:
            print("Computer has won! The computer guessed your number {}".format(my_number))
            break
        elif computer_guess > my_number:
            print("Computer has choosedn Higher number: {}".format(computer_guess))
            high_guess = computer_guess
            number_guesses += 1
            continue
        elif computer_guess < my_number:
            print("Computer has choosedn Lower number:{}".format(computer_guess))
            low_guess = computer_guess
            number_guesses += 1
            continue
    else:
        print("You have won, the computer failed!")

    #else:
    play_again = input("Do you want to play again? Y/N")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye!")

game()






# def even_odd(num):
#     if num % 2 == 0:
#         print(True)
#         return True
#     else:
#         print(False)
#         return False
#
# even_odd(10)
# even_odd(5)

















#
