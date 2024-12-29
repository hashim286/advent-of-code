import re

FILENAME = "data.txt"

with open(FILENAME) as file:
    text = file.read()
    lines = [item for item in text.split("\n")]
    left_side = []
    right_side = []
    total_distance = 0
    for pair in lines:
        numbers = re.findall(r"\d+", pair)
        left_side.append(int(numbers[0]))
        right_side.append(int(numbers[1]))

    left_side.sort()
    right_side.sort()

    length_list = len(left_side)

    for i in range(length_list):
        total_distance += abs(left_side[i] - right_side[i])
        # print(left_side[i], right_side[i], total_distance)

    print(total_distance)