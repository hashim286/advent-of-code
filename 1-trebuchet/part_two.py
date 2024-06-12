import re as re


num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

FILENAME = "input.txt"


def main(file_name):
    with open(file_name, "r") as f:
        # contains the numbers found from each line
        all_line_matches = list()
        for line in f:
            # the number found from the specific line
            num_in_line = find_string(line)
            # add the number found to a list of all numbers
            all_line_matches.append(int(num_in_line))

        print(sum(all_line_matches))


def find_string(line):
    """finds the number for a given line by matching the first and last number and concatenating the string
    and returning it"""
    # list to contain matches within the line given
    unordered_matches = list()
    for item in num_dict.keys():

        # matches all occurrences of a number spelled out, creates an iterable called match_list
        matches_as_word = re.finditer(item, line)
        # matches all occurrences of a number written in numerical form, creates iterable called matches_as_number
        matches_as_number = re.finditer(str(num_dict.get(item)), line)

        # iterate through match_list, add each match object to a list called "match_list"
        for match_obj in matches_as_word:
            unordered_matches.append(match_obj)

        # iterate through matches_as_number, add each match object to the match_list from before
        for match_obj in matches_as_number:
            unordered_matches.append(match_obj)

    # sends to a function to order match objects based on where they occurred in the string
    ordered_matches = order_by_span(unordered_matches)

    return create_string(ordered_matches)


def order_by_span(matches):
    """takes in a list of match objects and returns the list sorted by where in the string the match occurred"""
    new_match_list = list()
    span_list = list()

    # creates a list of the first span value in the tuple from the match object
    for item in matches:
        span_list.append(item.span()[0])

    # sort the span list
    span_list.sort()

    # iterate through each span value from the created list and compare it to the span values in the match object, if a
    # match is found, the match object is added to a new match list
    for i in range(len(span_list)):
        for item in matches:
            if span_list[i] == item.span()[0]:
                new_match_list.append(item)

    return new_match_list


def create_string(matches):
    """takes in list of match objects, returns a string that is concatenated from the first and last value in the
    list"""

    first_num = num_dict.get(matches[0].group())
    last_num = num_dict.get(matches[-1].group())
    if first_num is None:
        first_num = matches[0].group()

    if last_num is None:
        last_num = matches[-1].group()

    return str(first_num) + str(last_num)


main(FILENAME)
