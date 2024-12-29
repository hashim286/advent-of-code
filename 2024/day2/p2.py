FILENAME = "data.txt"


def check_safe(line: list):
    is_safe = True
    list_type = ""
    for i in range(len(line) - 1):
        if i == len(line) - 1:
            break

        if line[i + 1] > line[i] and (line[i + 1] - line[i] <= 3):
            if list_type == "decreasing":
                is_safe = False
                break

            list_type = "increasing"

        elif line[i + 1] < line[i] and abs(line[i + 1] - line[i]) <= 3:
            if list_type == "increasing":
                is_safe = False
                break

            list_type = "decreasing"

        else:
            is_safe = False
            break
    if i > 0:
        return is_safe, i+1, i - 1, i
    else:
        return is_safe, i + 1, i

with (open(FILENAME) as file):
    lines = [line.split(" ") for line in file]
    safe_reports = 0
    counter = 0
    for line in lines:
        nums = [int(num.strip()) for num in line]
        check = check_safe(nums)
        if not check[0]:
            temp_list = nums.copy()
            temp_list.pop(check[1])
            next_index = check_safe(temp_list)
            try:
                temp_list = nums.copy()
                temp_list.pop(check[2])
                current_index = check_safe(temp_list)
                temp_list = nums.copy()
            except IndexError:
                if next_index[0]:
                    safe_reports += 1
                    continue
            else:
                try:
                    temp_list.pop(check[3])
                    prior_index = check_safe(temp_list)
                except IndexError:
                    if next_index[0] or current_index[0]:
                        safe_reports += 1
                        continue
                else:
                    if next_index[0] or current_index[0] or prior_index[0]:
                        safe_reports += 1
                        continue

        else:
            safe_reports += 1


    print(safe_reports)