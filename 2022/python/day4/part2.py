FILE_PATH = "E:/PycharmProjects/advent-of-code/day4/text.txt"

total_of_overlapping_tasks = 0


def convert_to_ints(input_range):
    for i in range(len(input_range)):
        input_range[i] = int(input_range[i])


def find_overlaps(range_one, range_two):
    value_to_return = 0

    if range_one[0] <= range_two[0] <= range_one[1] or range_two[0] <= range_one[0] <= range_two[1]:
        value_to_return = 1

    return value_to_return


with open(FILE_PATH) as file:
    for line in file:
        tasks = line.split(",")
        first_range = tasks[0].split("-")
        second_range = tasks[1].split("-")
        convert_to_ints(first_range)
        convert_to_ints(second_range)
        total_of_overlapping_tasks += find_overlaps(first_range, second_range)

print(total_of_overlapping_tasks)