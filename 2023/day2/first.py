# RED_CUBES = 12
# GREEN_CUBES = 13
# BLUE_CUBES = 14

CUBES = {
    "green": 13,
    "blue": 14,
    "red": 12
}

with open("input.txt", "r") as input_file:
    possible_games = []
    sum = 0
    for line in [x.strip() for x in input_file.readlines()]:
        game_label, subgames_str = line.split(":")
        id = game_label.split(" ")[1]
        subgames = [subgame.strip() for subgame in subgames_str.split(";")]
        is_possible = True
        for subgame in subgames:
            hands = [x.strip() for x in subgame.split(",")]
            for hand in hands:
                num, color = hand.split(" ")
                if int(num) > CUBES[color]:
                    is_possible = False
                    break

            if not is_possible:
                break

        if not is_possible:
            continue

        possible_games.append(id)
        sum = sum + int(id)

    print(sum)
