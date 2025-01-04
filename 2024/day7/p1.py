from collections.abc import Iterator

FILENAME: str = "data.txt"


def read_data(filename: str) -> list[str]:
    """Reads the file passed into the function and returns the file as a list containing each line in the input file"""
    file: str
    with open(filename) as file:
        text = file.read().splitlines()
        return text


def parse_line(line: str) -> tuple[int, list[int]]:
    """parses a string passed into it for the numbers to compute with and the test value that we are targeting, returns
    the test value and the numbers to compute the target value with as a tuple"""
    instructions: list[str] = line.split(": ")
    nums: list[str] = instructions[1].split(" ")
    nums: list[int] = [int(item) for item in nums]
    return int(instructions[0]), nums


# could not figure the generate_operations part out on my own, I had to take a lot of inspiration from Cdawn99's
# solution here --> https://github.com/Cdawn99/AoC2024/blob/master/Day07/day7_p1.py


def generate_operations(max_operation_count: int) -> Iterator[list[str]]:
    """takes the max operations for the given line and uses yield to generate all possible combinations of operations"""
    operations: list[str] = ['*'] * max_operation_count
    last_operation_check: list[str] = ['+'] * max_operation_count    

    while operations != last_operation_check:     
        # yield returns the current operation back to the caller to be valuated as a single possible set of operations,
        # if that operation fails we will come back here and continue execution
        yield operations
        for i in range(max_operation_count):
            # if the current index in our operation is a + that means we have already flipped it at some point so we
            # set it to a * and continue the loop to try a different combination
            if operations[i] == "+": 
                operations[i] = "*"
                continue
            
            # if the current index is a * then we have either not been to this operator index yet or we did flip it
            # before and flipped a different index later so  we set it to a + instead to try a
            # new combination and break the loop
            else: 
                operations[i] = "+"
                break

    # if we have flipped all operators to be ++++ then it will break the while loop condition, and we can return
    # that to the caller
    yield operations


def evaluate_line(test_value: int, nums: list[int], operations: list[str]) -> bool:
    """evaluates a given set of numbers against the test value and the operations"""
    value: int = nums[0]
    for number, operation in zip(nums[1:], operations): 
        if operation == "+": 
            value += number
        else: 
            value *= number

    if value == test_value:
        return True
    else:
        return False


def main(filename: str) -> None:
    data: list[str] = read_data(filename)
    line: str
    calibration_value = 0
    for line in data: 
        test_value: int
        nums: list[int]
        test_value, nums = parse_line(line)
        max_operations: int = len(nums) - 1
        operations = generate_operations(max_operations)

        for operation in operations:
            result = evaluate_line(test_value, nums, operation)
            if result:
                calibration_value += test_value
                break
    print(calibration_value)


main(FILENAME)
