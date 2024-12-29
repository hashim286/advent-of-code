FILE_PATH = "text.txt"

# change read_length to 4 or 14 for parts 1 or 2 respectively
read_length = 14 #4


def has_duplicates(input_list):
    duplicates = False
    for j in range(len(list_of_letters)):
        for k in range(len(list_of_letters)):
            if j == k:
                break

            if list_of_letters[j] == list_of_letters[k]:
                duplicates = True
    return duplicates


with open(FILE_PATH) as file:
    text = file.read()
    for i in range(len(text)):
        if i == len(text) - read_length:
            break

        list_of_letters = []
        for j in range(read_length):
            list_of_letters.append(text[i + j])
            
        if not has_duplicates(list_of_letters):
            print(i + read_length)
            break
