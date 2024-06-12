import re

FILENAME = "input.txt"

max_val_for_each_color = {
    "red": 12,
    "blue": 14,
    "green": 13
}


def main(file):
    with (open(file) as f):
        valid_games = list()
        for line in f:
            is_valid = check_valid(line)

            if is_valid:
                game_num = get_game_num(line)
                valid_games.append(game_num)

        print(sum(valid_games))


def get_game_num(line):
    """returns the game ID of a given line"""
    # parses the line string to isolate just the number, gets rid of the : character
    game_num = re.findall(r"\d+:", line)
    game_num = game_num[0].replace(":", "")
    return int(game_num)


def check_valid(line):
    """looks at all the draws in the line and compares it to the max value defined in the dictionary, if any
    draw has a value that is greater than what is allowed for that color, it returns a false value, if no values
    are greater than it returns true"""

    valid = True

    # create a list that matches all occurrences of any number of digits followed by a space and then any number of
    # word characters
    draws = re.findall(r"\d+\s\w+", line)
    for draw in draws:
        # split each item by a space character in the list into a number and the color, each item has a
        # format of number space color e.g. 2 green or 5 blue
        draw_split = draw.split(" ")
        # compare the max value defined in the dictionary to the integer value in the item, set the valid value to false
        # if it is greater
        if max_val_for_each_color.get(draw_split[1]) < int(draw_split[0]):
            valid = False
            return valid

    return valid


main(FILENAME)
