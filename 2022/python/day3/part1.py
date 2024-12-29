FILE_PATH = "text.txt"

with open(FILE_PATH) as file:
    total = 0
    for line in file:
        length = len(line)
        first_half = line[:int(length / 2)]
        second_half = line[int(length / 2): -1]
        letters_in_common = list()

        for letter in first_half:
            if letter in second_half and letter not in letters_in_common:
                letters_in_common.append(letter)

        for letter in letters_in_common:
            ascii_value = ord(letter)
            if 97 <= ascii_value <= 122:
                letter_value = ascii_value - 96
            else:
                letter_value = ascii_value - 38

            total += letter_value
print(total)
