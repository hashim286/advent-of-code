import re as re

FILENAME = "input.txt"


def main(file_name):
    with open(file_name, "r") as f:
        line_matches = list()
        for line in f:
            matches = re.findall(r"\d", line)
            line_matches.append(int(matches[0] + matches[-1]))

        print(sum(line_matches))


main(FILENAME)
