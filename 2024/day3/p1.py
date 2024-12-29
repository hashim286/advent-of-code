import re

FILENAME = "data.txt"

with open(FILENAME, "r") as f:
    text = f.read()
    matches = re.findall(r"(mul\(\d+,\d+\))", text)
    total = 0
    for match in matches:
        nums = re.findall(r"\d+", match)
        total += int(nums[0]) * int(nums[1])

    print(total)
