FILE_PATH = "text.txt"

input_data = [
    ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
    ['M', 'Q', 'H'],
    ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
    ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
    ['M', 'T', 'H', 'P'],
    ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
    ['M', 'N', 'B', 'F', 'V', 'R'],
    ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
    ['P', 'D', 'B', 'C', 'N']
 ]



with open(FILE_PATH) as file:
    for line in file:
        command_list = []
        line_split = line.split(" ")
        if "move" in line_split:
            command_list.append(int(line_split[1]))
            command_list.append(int(line_split[3]))
            command_list.append(int(line_split[-1]))
        else:
            continue

        num_items_to_move = command_list[0]


        crates_being_moved = input_data[command_list[1] - 1][-command_list[0]:]

        for crate in crates_being_moved:
            input_data[command_list[2] - 1].append(crate)
        
        for i in range(num_items_to_move):
            input_data[command_list[1] - 1].pop()



for item in input_data:
    print(item[-1:])

