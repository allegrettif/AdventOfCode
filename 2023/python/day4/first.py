
import re

with open("../../inputs/day4.txt") as input_file:

    sum = 0

    for line in [s_line.strip() for s_line in input_file.readlines()]:

        card, numbers = [x.strip() for x in line.split(":")]
        scratched, winnings = [x.strip() for x in numbers.split("|")]

        scratched_numbers = [int(x) for x in re.findall("\d+", scratched)]
        winning_numbers = [int(x) for x in re.findall("\d+", winnings)]

        points = 0
        for n in scratched_numbers:
            if n in winning_numbers:
                points = (points * 2) if points > 0 else (points + 1)

            
        sum = sum + points


    print(sum)