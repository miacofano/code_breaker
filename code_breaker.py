import random

COLORS_6 = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
COLORS_8 = COLORS_6 + ['white', 'black']
TURNS = 10

"""
Code Breaker (also known as Mastermind) is a board game.  The user is tasked with guessing a random code.
The code range from 3 digits to 5 digits long, and color options can be 6 or 8, depending on the difficulty.
This program has the user input the level of difficulty they desire and then gives them 10 turns to crack the code.
Each time the user guesses the program will check to see if they first have any colors that are in the correct position.
Then it will check if the have a correct color that is in the wrong position.  It will then return the hint to help the
user crack the code.  
Level difficulties: 
1 - Colors 6, Codes 3, Combinations 1290
2 - Colors 8, Codes 3, Combinations 4088
3 - Colors 6, Codes 4, Combinations 7770
4 - Colors 8, Codes 4, Combinations 32760
5 - Colors 8, Codes 5, Combinations 262136
"""


def main():
    level = intro()
    number_of_colors = difficulty_colors(level)
    number_of_codes = difficulty_codes(level)
    correct_code = get_code(number_of_codes, number_of_colors)
    game(correct_code, number_of_codes, number_of_colors)


# Starts the game lists the color options for the user
def start(number_of_colors):
    print("To play enter one color at a time.")
    print("Your color options are:")
    if number_of_colors == 6:
        print_list(COLORS_6)
    else:
        print_list(COLORS_8)


# The basic operation of the game
def game(correct_code, number_of_codes, number_of_colors):
    start(number_of_colors)
    win = 0
    for i in range(TURNS):
        player_code = get_player_code(number_of_codes)
        hint = check_answer(correct_code, player_code, number_of_codes)
        if hint[0] == number_of_codes:
            print("You cracked the code!")
            win = 1
            break
        else:
            print("There is " + str(hint[0]) + " codes correct.")
            print("There is " + str(hint[1]) + " codes in the wrong position.")
            print("You have " + str(9 - i) + " turns left.")
    if win == 0:
        print("Game Over!")
        print("You ran out of guesses.")
    print("The code was:")
    print_list(correct_code)


# Checks the users guesses and returns a hint for the user
def check_answer(correct_code, player_code, number_of_codes):
    hint = []
    w_check = 0
    b_check = 0
    for i in range(number_of_codes):
        white = 0
        for j in range(number_of_codes):
            if player_code[i] == correct_code[i]:
                b_check += 1
            elif player_code[j] == correct_code[i]:
                white += 1
        if white >= 1:
            w_check += 1
    if b_check >= 1:
        b_check //= number_of_codes
    hint.append(b_check)
    hint.append(w_check)
    return hint


# Gets code guesses from user
def get_player_code(number_of_codes):
    player_code = []
    for i in range(number_of_codes):
        color = input("Enter color " + str(i + 1) + " :")
        color = color.lower()
        player_code.append(color)
    return player_code


# Prints a list
def print_list(list):
    for value in list:
        print(value)


# Random number generates a random number of number that are converted to a color code
def color_convert(num):
    if num == 1:
        num = 'red'
    elif num == 2:
        num = 'blue'
    elif num == 3:
        num = 'green'
    elif num == 4:
        num = 'yellow'
    elif num == 5:
        num = 'orange'
    elif num == 6:
        num = 'purple'
    elif num == 7:
        num = 'white'
    else:
        num = 'black'
    return num


# Get code generates a random code based off of the difficulty
def get_code(number_of_codes, number_of_colors):
    code = []
    for i in range(number_of_codes):
        num = random.randint(1, number_of_colors)
        color = color_convert(num)
        code.append(color)
    return code


# Dif. of codes takes users desired level and returns the number of codes they have to guess
def difficulty_codes(level):
    if level == 1 or level == 2:
        number_of_codes = 3
    elif level == 3 or level == 4:
        number_of_codes = 4
    else:
        number_of_codes = 5
    return number_of_codes


# Dif. of colors takes the users desired level and returns the number of colors they can choose from
def difficulty_colors(level):
    if level == 1 or level == 3:
        number_of_colors = 6
    else:
        number_of_colors = 8
    return number_of_colors


# Intro greats the user and retrieves the level of difficulty the user would like to play at
# The user must choose between the 5 levels of difficulty
def intro():
    print("Welcome to Crack the Code!")
    level = int(input("Enter level of difficulty (levels 1-5): "))
    while level > 5 or level < 1:
        print("That is not a valid level entry.")
        level = int(input("Enter level of difficulty (levels 1-5): "))
    print("Can you crack the level " + str(level) + " code?")
    return level


if __name__ == "__main__":
    main()