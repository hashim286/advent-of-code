import re

FILENAME = "input.txt"


def main(file):
    with (open(file) as f):
        # stores power of cubes for each line
        power_of_cubes = list()
        for line in f:
            max_cubes = get_max_cubes(line)
            # appends the cube maxes multiplied by each other
            power_of_cubes.append(max_cubes.get("red") * max_cubes.get("blue") * max_cubes.get("green"))
        print(sum(power_of_cubes))


def get_max_cubes(line):
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    # matches all draws in the line string with a pattern of any number of digits followed by a space character and
    # any number of word characters
    draws = re.findall(r"\d+\s\w+", line)
    for draw in draws:
        draws_split = draw.split(" ")

        # compares the current max value in the dictionary to the value of the draw, if the draw is greater it becomes
        # the new value stored in the dictionary
        if max_cubes.get(draws_split[1]) < int(draws_split[0]):
            max_cubes[draws_split[1]] = int(draws_split[0])

    return max_cubes


main(FILENAME)
