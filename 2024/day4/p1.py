FILENAME = "example.txt"

with open("example.txt", "r") as file:
    lines = file.readlines()
    grid = [line.strip() for line in lines]

    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), # up, down, right, left
        (1, 1), (1, -1), (-1, -1), (-1, 1) # diagonal(right up, right down, left down, left up)
    ]
    word = "XMAS"
    xmas_num = 0

    for i in range(len(grid)): # row iterator
        for j in range(len(grid[0])): # column iterator
            if grid[i][j] != word[0]:
                continue
            for direction in directions:
                increment_num = True
                for k in range(len(word)):
                    column_modifier = j + (k * direction[0])
                    row_modifier = i + (k * direction[1])
                    try:
                        if grid[row_modifier][column_modifier] == word[k] and column_modifier >=0 and row_modifier >= 0:
                            continue
                        else:
                            increment_num = False
                            break
                    except IndexError:
                        increment_num = False
                        break

                if increment_num:
                    xmas_num += 1

    print(xmas_num)
