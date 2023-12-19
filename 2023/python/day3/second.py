from typing import List, Tuple, Dict
import functools


def convert_into_matrix(lines: List[str]) -> List[List[str]]:
    '''
    Converts the file into a matrix of characters
    '''
    matrix = []
    for line in lines:
        chars = []
        for char in line.strip():
            chars.append(char)
        matrix.append(chars)
    return matrix

def generate_gears(matrix: List[List[str]], cardinal_points: List[Tuple[int, int]]):
    gears: List[str] = [];

    for col, row in cardinal_points:
        cell = matrix[row][col]
        if not cell.isdigit() and cell != "." and cell == "*":
            gears.append(f"{row}x{col}")

    return gears

def check_surroundings(matrix: List[List[str]], row: int, col: int) -> List[str]:
    '''
    Takes in the positions and return the gear position and the number
    '''
    NORTH = (col, row - 1)
    SOUTH = (col, row + 1)
    EAST = (col + 1, row)
    WEST = (col - 1, row)
    SOUTH_EAST = (col + 1, row + 1)
    SOUTH_WEST = (col - 1, row + 1)
    NORTH_EAST = (col + 1, row - 1)
    NORTH_WEST = (col - 1, row - 1)


    if row == 0:

        if col == 0:
            return generate_gears(matrix, [EAST, SOUTH_EAST, SOUTH])
            
        elif col == len(matrix[row]) - 1:
            return generate_gears(matrix, [SOUTH, SOUTH_WEST, WEST])
        
        else:
            return generate_gears(matrix, [EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST])
        
    elif row == len(matrix) - 1:

        if col == 0:
            return generate_gears(matrix, [NORTH, NORTH_EAST, EAST])
            
        elif col == len(matrix[row]) - 1:
            return generate_gears(matrix, [WEST, NORTH_WEST, NORTH])
        
        else:
            return generate_gears(matrix, [WEST, NORTH_WEST, NORTH, NORTH_EAST, EAST])
        
    else:

        if col == 0:
            return generate_gears(matrix, [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH])
            
        elif col == len(matrix[row]) - 1:
            return generate_gears(matrix, [SOUTH, SOUTH_WEST, WEST, NORTH_WEST, NORTH])
        
        else:
            return generate_gears(matrix, [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST])


with open("../../inputs/day3.txt", "r") as input_file:
    sum = 0
    matrix = convert_into_matrix(input_file.readlines())

    gear_map: Dict[str, List[int]] = {}
    row = 0

    while row in range(0, len(matrix)):

        col = 0

        while col in range(0, len(matrix[row])):

            # matrix[row][col] = char
            gear_poss: List[str] = []
            num = ""
            # print(col, row, len(matrix), len(matrix[row]))

            if matrix[row][col].isdigit():

                while matrix[row][col].isdigit():
                    num = num + matrix[row][col]

                    # Check the adjacent cells
                    sorrounding_gears = check_surroundings(matrix, row, col)
                    gear_poss.extend(sorrounding_gears)

                    col = col + 1

                    if col == len(matrix[row]):
                        break
                
                gear_poss = list(dict.fromkeys(gear_poss))

            
            if len(gear_poss) > 0:
                for gear in gear_poss:
                    if gear in gear_map:
                        gear_map[gear].append(int(num))
                    else:
                        gear_map[gear] = [int(num)]

            
            col = col + 1

        
        row = row + 1

    sum = 0
    for gear, nums in gear_map.items():
        if len(nums) < 2:
            continue
        # print(gear, nums)
        mul = functools.reduce((lambda a,b: a * b), nums)
        sum = sum + mul

    print(sum)
