FILENAME = "data.txt"

with open(FILENAME) as file:
    data = file.read()
    data = data.split("\n")
    num_xmas = 0

    num_rows = len(data)
    num_columns = len(data[0])

    for i in range(num_rows - 1):
        for j in range(num_columns - 1): 
            if data[i][j] != "A": # skip to next loop iteration if it's not an A
                continue

            try: 
                if (data[i + 1][j + 1] == "M" and data[i - 1][j - 1] == "S") or (data[i - 1][j - 1] == "M" and data[i + 1][j + 1] == "S"): # check around our A for an M or an S in either direction
                    if (data[i + 1][j - 1] == "M" and data[i - 1][j + 1] == "S") or (data[i - 1][j + 1] == "M" and data[i + 1][j - 1] == "S"): # check the other direction for an M or an S 
                        num_xmas += 1
            except IndexError: # catch the index error and skip, if we hit an index error then we know there's no room to have a MAS cross so we can safely move on 
                continue

    print(num_xmas)

