import sys

print("hello world")


def get_numbers(line):
    return [num for num in line if num.isnumeric()]


if __name__ == "__main__":
    the_sum = 0
    with open(sys.argv[1]) as file:
        for line in file:
            nums = get_numbers(line.strip())
            the_sum += int(str(nums[0]) + str(nums[-1]))
    print(the_sum)
