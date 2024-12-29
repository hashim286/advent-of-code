FILENAME = "data.txt"

with (open(FILENAME) as file):
    lines = [line.split(" ") for line in file]
    safe_reports = 0
    for line in lines:
        is_safe = True
        list_type = ""
        nums = [int(num.strip()) for num in line]

        for i in range(len(nums) - 1):
            if i == len(nums) - 1:
                break

            if nums[i + 1] > nums[i] and nums[i + 1] - nums[i] <= 3:
                if list_type == "decreasing":
                    is_safe = False
                    break

                list_type = "increasing"

            elif nums[i + 1] < nums[i] and abs(nums[i + 1] - nums[i]) <= 3:
                if list_type == "increasing":
                    is_safe = False
                    break

                list_type = "decreasing"

            else:
                is_safe = False
                break

        if is_safe:
            safe_reports += 1

    print(safe_reports)

