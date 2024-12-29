FILE_PATH = "text.txt"

with open(FILE_PATH) as file:
    letters_in_all = list()
    total = 0
    while True:
        line_one = file.readline()
        line_two = file.readline()
        line_three = file.readline()

        if len(line_one) == 0:
            break

        for letter in line_one:
            if letter in line_two and letter in line_three:
                letters_in_all.append(letter)
                break

    for letter in letters_in_all:
        ascii_value = ord(letter)
        if 97 <= ascii_value <= 122:
            letter_value = ascii_value - 96
        else:
            letter_value = ascii_value - 38

        total += letter_value

print(total)
