from typing import List, Tuple


def convert_into_matrix(lines: List[str]) -> List[List[str]]:
    matrix = []
    for line in lines:
        chars = []
        for char in line.strip():
            chars.append(char)
        matrix.append(chars)
    return matrix


def get_cardinal_points(matrix, x, y, directions):
    cardinal_points = []
    for direction in directions:
        if direction == "NORTH":
            cardinal_points.append(matrix[y - 1][x])
        elif direction == "SOUTH":
            cardinal_points.append(matrix[y + 1][x])
        elif direction == "EAST":
            cardinal_points.append(matrix[y][x + 1])
        elif direction == "WEST":
            cardinal_points.append(matrix[y][x - 1])
        elif direction == "SOUTH_EAST":
            cardinal_points.append(matrix[y + 1][x + 1])
        elif direction == "SOUTH_WEST":
            cardinal_points.append(matrix[y + 1][x - 1])
        elif direction == "NORTH_WEST":
            cardinal_points.append(matrix[y - 1][x - 1])
        elif direction == "NORTH_EAST":
            cardinal_points.append(matrix[y - 1][x + 1])

    return cardinal_points


def check_near(matrix: List[List[str]], cur_pos: Tuple[int, int]):
    y, x = cur_pos
    # print(x, y)
    if y == 0:
        # Top
        if x == 0:
            # Left Border

            for cardinal_point in get_cardinal_points(matrix, x, y, ["EAST", "SOUTH_EAST", "SOUTH"]):
                if not cardinal_point.isdigit() and cardinal_point != ".":
                    return True

            return False

        elif x == len(matrix[y]) - 1:
            # Right Border

            for cardinal_point in get_cardinal_points(matrix, x, y, ["WEST", "SOUTH_WEST", "SOUTH"]):
                if not cardinal_point.isdigit() and cardinal_point != ".":
                    return True

            return False

        else:

            for cardinal_point in get_cardinal_points(matrix, x, y, ["SOUTH", "SOUTH_EAST", "SOUTH_WEST", "WEST", "EAST"]):
                if not cardinal_point.isdigit() and cardinal_point != ".":
                    return True

            return False

    elif y == len(matrix) - 1:
        # Bottom
        if x == 0:
            # Left Border
            north = matrix[y - 1][x]
            north_east = matrix[y - 1][x + 1]
            east = matrix[y][x + 1]

            if not east.isdigit() and east != ".":
                return True
            elif not north_east.isdigit() and north_east != ".":
                return True
            elif not north.isdigit() and north != ".":
                return True
            else:
                return False

        elif x == len(matrix[y]) - 1:
            # Right Border
            north = matrix[y - 1][x]
            north_west = matrix[y - 1][x - 1]
            west = matrix[y][x - 1]

            if not west.isdigit() and east != ".":
                return True
            elif not north_west.isdigit() and south_east != ".":
                return True
            elif not north.isdigit() and south != ".":
                return True
            else:
                return False

        else:
            north = matrix[y - 1][x]
            north_west = matrix[y - 1][x - 1]
            north_east = matrix[y - 1][x + 1]
            west = matrix[y][x - 1]
            east = matrix[y][x + 1]

            for cardinal_point in [north, north_east, north_west, west, east]:
                if not cardinal_point.isdigit() and cardinal_point != ".":
                    return True

            return False

    else:
        # No border
        if x == 0:
            # Left Border
            north = matrix[y - 1][x]
            north_east = matrix[y - 1][x + 1]
            south = matrix[y + 1][x]
            south_east = matrix[y + 1][x + 1]
            east = matrix[y][x + 1]

            if not north.isdigit() and east != ".":
                return True
            elif not north_east.isdigit() and north_east != ".":
                return True
            elif not east.isdigit() and east != ".":
                return True
            elif not south_east.isdigit() and south_east != ".":
                return True
            elif not south.isdigit() and south != ".":
                return True
            else:
                return False

        elif x == len(matrix[y]) - 1:
            # Right Border
            north = matrix[y - 1][x]
            north_west = matrix[y - 1][x - 1]
            south = matrix[y + 1][x]
            south_west = matrix[y + 1][x - 1]
            west = matrix[y][x - 1]

            if not north.isdigit() and north != ".":
                return True
            elif not north_west.isdigit() and north_west != ".":
                return True
            elif not west.isdigit() and west != ".":
                return True
            elif not south_west.isdigit() and south_west != ".":
                return True
            elif not south.isdigit() and south != ".":
                return True
            else:
                return False

        else:
            north = matrix[y - 1][x]
            south = matrix[y + 1][x]
            north_east = matrix[y - 1][x + 1]
            north_west = matrix[y - 1][x - 1]
            south_east = matrix[y + 1][x + 1]
            south_west = matrix[y + 1][x - 1]
            east = matrix[y][x + 1]
            west = matrix[y][x - 1]

            for cardinal_point in [north, south, south_east, south_west, north_east, north_west, east, west]:
                if not cardinal_point.isdigit() and cardinal_point != ".":
                    return True

            return False


with open("../../inputs/day3.txt", "r") as input_file:
    sum = 0
    matrix = convert_into_matrix(input_file.readlines())

    # Debug Print matrix
    # for x in range(0, len(matrix)):
    #     for y in range(0, len(matrix[x])):
    #         print(matrix[x][y], end="")
    #     print("")

    y = 0

    while y in range(0, len(matrix)):
        x = 0

        while x in range(0, len(matrix[y])):

            num: str = ""
            is_summable = False

            # print(x, len(matrix[y]), matrix[y], matrix[y][x])
            if matrix[y][x].isdigit():
                # print(matrix[y])
                while matrix[y][x].isdigit():
                    # print(matrix[y][x])
                    is_summable = is_summable or check_near(matrix, (y, x))
                    num = num + matrix[y][x]
                    x = x + 1
                    if x == len(matrix[y]):
                        break

                if is_summable:
                    sum = sum + int(num)

                x = x - 1
            # print(sum, num)

            print(f"{num if len(num) > 0 else matrix[y][x]}", end="")

            x = x + 1
            # print(x, len(matrix[y]))
        print("")
        y = y + 1

    print(sum)
