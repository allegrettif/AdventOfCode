from functools import reduce
import re

def main():
    with open("../../inputs/day3.txt", "r") as mul_file:
        content = reduce(lambda a, b: a + b, [x.strip() for x in mul_file.readlines()], "")
        numbers = [int(x)*int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", content)]
        print(reduce(lambda a, b: a + b, numbers))

if __name__ == "__main__":
    main()
