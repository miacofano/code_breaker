import random

COLORS_6 = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
COLORS_8 = COLORS_6 + ['white', 'black']
TURNS = 10


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
    #loop will run based until i is equal to the number of allowed turns
    for i in range(TURNS):
        player_code = get_player_code(number_of_codes, number_of_colors)
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
def get_player_code(number_of_codes, number_of_colors):
    player_code = []
    #creates constant to verify the entered color
    if number_of_colors == 6:
        verify_color = COLORS_6
    else:
        verify_color = COLORS_8
    #will ask player to enter color choice based on number of required codes
    for i in range(number_of_codes):
        color = input("Enter color " + str(i + 1) + " :")
        #converts entry to lower case string
        color = color.lower()
        #while loop to verify that the users entry is one of the available options
        while color not in verify_color:
            print("That is not a valid color entry.")
            color = input("Enter color " + str(i + 1) + " :")
        #once the user has entered a valid option it will add it to the players code
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
    #loops for number of codes needed for level of difficulty
    for i in range(number_of_codes):
        #generates random number based on number of colors
        num = random.randint(1, number_of_colors)
        #converts the random number into a color
        color = color_convert(num)
        #adds color to code list
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