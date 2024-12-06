DIR_UP = "^"
DIR_DOWN = "v"
DIR_LEFT = "<"
DIR_RIGHT = ">"
PREV_STEP = "X"

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
        return matrix[row - 1][col] == "#" or matrix[row - 1][col] == "O"
    elif direction == DIR_DOWN:
        return matrix[row + 1][col] == "#" or matrix[row + 1][col] == "O"
    elif direction == DIR_LEFT:
        return matrix[row][col - 1] == "#" or matrix[row][col - 1] == "O"
    else:
        return matrix[row][col + 1] == "#" or matrix[row][col + 1] == "O"

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

def get_simulation_result(matrix: list[list[str]], start_position: tuple[int, int], start_direction: str) -> bool:
    inner_matrix = clone_matrix(matrix)
    position = start_position
    direction = start_direction
    is_out = False
    while not is_out:
        if is_border(inner_matrix, position):
            is_out = True
            continue

        if obstacle_found(inner_matrix, position, direction):
            direction = get_new_direction(direction)
            continue
        
        position = get_new_position(inner_matrix, position, direction)
    return inner_matrix
 
def get_useless_indices(matrix: list[list[str]], direction: str):
    indices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if(matrix[row][col] == "."):
                indices.append(f"{row}x{col}")
    
    return indices
 
def simulate(matrix: list[list[str]], start_position: tuple[int, int], start_direction: str) -> bool:
    inner_matrix = clone_matrix(matrix)
    position = start_position
    direction = start_direction
    old_positions = {}
    is_out = False
    while not is_out:
        if is_border(inner_matrix, position):
            is_out = True
            continue

        if obstacle_found(inner_matrix, position, direction):
            direction = get_new_direction(direction)
            continue
        
        position = get_new_position(inner_matrix, position, direction)
        if position in old_positions:
            old_positions[position] += 1
        else:
            old_positions[position] = 1
            
        for value in old_positions.values():
            if value > 5:
                return 1
    return 0

def clone_matrix(matrix: list[list[str]]):
    new_matrix = []
    for row in range(0, len(matrix)):
        new_matrix.append(matrix[row][:])

    return new_matrix

def main():
    with open("../../inputs/day6.txt", "r") as path_file:
        matrix = get_matrix(path_file.readlines())
        position, direction = find_cursor(matrix)
        useless_matrix = get_simulation_result(matrix, position, direction)
        useless_indices = get_useless_indices(useless_matrix, direction)
        loops = 0
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix)):
                if f"{row}x{col}" in useless_indices:
                    continue
                print((row, col))
                
                simulate_matrix = clone_matrix(matrix)
                simulate_matrix[row][col] = "O"
                result = simulate(simulate_matrix, position, direction)
                print("LOOP" if result == 1 else "NO_LOOP")
                loops += result
                
        print(loops)

if __name__ == "__main__":
    main()