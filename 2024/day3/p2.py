import re

FILENAME = "data.txt"

with open(FILENAME, "r") as f:
    text = f.read()
    matches = re.findall(r"(mul\(\d+,\d+\))|(don't\(\))|(do\(\))", text)
    total = 0
    new_match_list = []

    for match in matches:
        for item in match:
            if item != "":
                new_match_list.append(item)

    activated = True
    for item in new_match_list:
        if len(re.findall(r"\d+", item)) != 0:
            nums = re.findall(r"\d+", item)
            if activated:
                total += int(nums[0]) * int(nums[1])
        elif re.match(r"(don't\(\))", item) is not None:
            activated = False
        elif re.match(r"(do\(\))", item) is not None:
            activated = True
    print(total)

