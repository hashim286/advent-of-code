FILE_PATH = "text.txt"

total_of_contained_tasks = 0


def convert_to_ints(input_range):
    for i in range(len(input_range)):
        input_range[i] = int(input_range[i])


def compare_ranges(range_one, range_two):
    if range_one[0] <= range_two[0] and range_one[1] >= range_two[1]:
        return 1
    elif range_two[0] <= range_one[0] and range_two[1] >= range_one[1]:
        return 1
    else:
        return 0


with open(FILE_PATH) as file:
    for line in file:
        tasks = line.split(",")
        first_range = tasks[0].split("-")
        second_range = tasks[1].split("-")
        # if lower bound on first range is greater than second AND upper bound is less than second, then first is
        # contained within second, otherwise, check reverse condition, else, no contained, so skip
        convert_to_ints(first_range)
        convert_to_ints(second_range)

        total_of_contained_tasks += compare_ranges(first_range, second_range)

print(total_of_contained_tasks)
