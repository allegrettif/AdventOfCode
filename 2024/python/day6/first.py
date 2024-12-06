DIR_UP = "^"
DIR_DOWN = "v"
DIR_LEFT = "<"
DIR_RIGHT = ">"
PREV_STEP = "X"

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_new_direction(current_direction: str) -> str:
    if current_direction == DIR_UP:
        return DIR_RIGHT
    elif current_direction == DIR_RIGHT:
        return DIR_DOWN
    elif current_direction == DIR_DOWN:
        return DIR_LEFT
    else:
        return DIR_UP

def get_new_position(matrix: list[list[str]], current_position: tuple[int, int], direction: str) -> tuple[int, int]:
    row, col = current_position
    if direction == DIR_UP:
        matrix[row][col] = "X"
        matrix[row - 1][col] = direction
        return (row - 1, col)
    elif direction == DIR_DOWN:
        matrix[row][col] = "X"
        matrix[row + 1][col] = direction
        return (row + 1, col)
    elif direction == DIR_RIGHT:
        matrix[row][col] = "X"
        matrix[row][col + 1] = direction
        return (row, col + 1)
    else:
        matrix[row][col] = "X"
        matrix[row][col - 1] = direction
        return (row, col - 1)

def get_matrix(content: list[str]):
    return [list(line.strip()) for line in content]

def is_border(matrix: list[list[str]], position: tuple[int, int]):
    row, col = position
    return row == 0 or row == len(matrix) - 1 or col == 0 or col == len(matrix[row]) - 1

def find_cursor(matrix: list[list[str]]) -> tuple[tuple[int, int], str]:
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            curr = matrix[row][col]
            if curr == DIR_UP:
                return (row, col), DIR_UP
            elif curr == DIR_DOWN:
                return (row, col), DIR_DOWN
            elif curr == DIR_RIGHT:
                return (row, col), DIR_RIGHT
            elif curr == DIR_LEFT:
                return (row, col), DIR_LEFT
    
def obstacle_found(matrix: list[list[str]], position: tuple[int, int], direction: str):
    row, col = position
    if direction == DIR_UP:
        return matrix[row - 1][col] == "#"
    elif direction == DIR_DOWN:
        return matrix[row + 1][col] == "#"
    elif direction == DIR_LEFT:
        return matrix[row][col - 1] == "#"
    else:
        return matrix[row][col + 1] == "#"

def is_previous_step(matrix:list[list[str]], position: tuple[int, int], direction: str):
    row, col = position
    if direction == DIR_UP:
        return matrix[row - 1][col] == PREV_STEP
    elif direction == DIR_DOWN:
        return matrix[row + 1][col] == PREV_STEP
    elif direction == DIR_RIGHT:
        return matrix[row][col + 1] == PREV_STEP
    else:
        return matrix[row][col - 1] == PREV_STEP

def print_matrix(matrix: list[list[str]]):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            print(matrix[row][col], end="")
        print("")
        

def main():
    with open("../../inputs/day6.txt", "r") as path_file:
        matrix = get_matrix(path_file.readlines())
        position, direction = find_cursor(matrix)
        steps = 0
        is_out = False
        
        while not is_out:
                
            if is_border(matrix, position):
                is_out = True
                steps += 1
                break
            
            if is_previous_step(matrix, position, direction):
                position = get_new_position(matrix, position, direction)
                continue

            if obstacle_found(matrix, position, direction):
                direction = get_new_direction(direction)
                continue
                
            position = get_new_position(matrix, position, direction)    
            steps += 1
            
        print(steps)

if __name__ == "__main__":
    main()