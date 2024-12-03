from functools import reduce
import re

TUPLE_RX = r"mul\((\d+),(\d+)\)"
SUB_RX = r"do\(\)(.*?)don't\(\)|(?:do\(\))+(.*)$"

DONT = "dont()"
DO = "do()"

def main():
    with open("../../inputs/day3.txt", "r") as mul_file:
        content = reduce(lambda a, b: a + b, [x.strip() for x in mul_file.readlines()], "")
        do_index = content.index(DO)
        dont_index = content.index(DONT)

        slice_index = 0
        if do_index < dont_index:
            slice_index = do_index
        else:
            slice_index = dont_index

        first_slice = content[:slice_index]
        other_slice = content[slice_index + (len(DONT) if do_index > dont_index else len(DO)):]

        tuple_first_slice = re.findall(TUPLE_RX, first_slice)
        tuple_other_slice = reduce(lambda a,b: a + b, [re.findall(TUPLE_RX, x) + re.findall(TUPLE_RX, y) for x, y in re.findall(SUB_RX, other_slice)], []) 

        tuples = tuple_other_slice + tuple_first_slice

        print(reduce(lambda a,b: a + b, [int(x) * int(y) for x, y in tuples], 0))

if __name__ == "__main__":
    main()
