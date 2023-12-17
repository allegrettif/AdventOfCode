# RED_CUBES = 12
# GREEN_CUBES = 13
# BLUE_CUBES = 14

import functools
import operator

CUBES = {
    "green": 13,
    "blue": 14,
    "red": 12
}

with open("../../inputs/day2.txt", "r") as input_file:
    possible_games = []
    sum = 0
    for line in [x.strip() for x in input_file.readlines()]:
        game_label, subgames_str = line.split(":")
        id = game_label.split(" ")[1]
        subgames = [subgame.strip() for subgame in subgames_str.split(";")]
        max_colors = {
            "green": 1,
            "red": 1,
            "blue": 1
        }
        for subgame in subgames:
            hands = [x.strip() for x in subgame.split(",")]
            for hand in hands:
                num_str, color = hand.split(" ")
                num = int(num_str)

                if max_colors[color] < num:
                    max_colors[color] = num

        power = functools.reduce(operator.mul, max_colors.values())

        sum = sum + power

    print(sum)
