import re
import functools

class Card:

    def __init__(self, num, scratched_nums, winnings_nums):
        self.__num = num
        self.__scratched_nums = scratched_nums
        self.__winnings_nums = winnings_nums


cards = {}

with open("../../inputs/day4.txt") as input_file:

    lines = [s_line.strip() for s_line in input_file.readlines()]
    cards = [1 for x in range(0, len(lines))]

    for index, line in enumerate(lines):

        card, numbers = [x.strip() for x in line.split(":")]
        scratched, winnings = [x.strip() for x in numbers.split("|")]
        scratched_numbers = [int(x) for x in re.findall("\d+", scratched)]
        winning_numbers = [int(x) for x in re.findall("\d+", winnings)]

        num_winnings = functools.reduce(lambda acc, curr: acc + 1 if (curr in winning_numbers) else acc, scratched_numbers, 0)

        # print(f"Wins {num_winnings}", "|", scratched, "|" , winnings, "|", cards[index], "|", cards, f"Cards from {index + 1} to {index + num_winnings + 1}\n")

        # print(index + 1, index + num_winnings + 1)
        for i in range(index + 1, index + num_winnings + 1):
            if i > len(cards) - 1:
                break
            to_sum = (1 * cards[index])
            cards[i] = cards[i] + to_sum

    sum = functools.reduce(lambda a, b: a + b, cards, 0)

    print(sum)

        

