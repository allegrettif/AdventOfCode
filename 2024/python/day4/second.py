XMAS = "MAS"
XMAS_LEN = len(XMAS)

def search(matrix: list[list[str]], row: int, col: int):
    tr = matrix[row - 1][col + 1]
    tl = matrix[row - 1][col - 1]
    br = matrix[row + 1][col + 1]
    bl = matrix[row + 1][col - 1]

    if tr == "m" and bl == "s" and tl == "m" and br == "s":
        return 1
    
    if tr == "s" and bl == "m" and tl == "s" and br == "m":
        return 1
    
    if tr == "s" and bl == "m" and tl == "m" and br == "s":
        return 1
    
    if tr == "m" and bl == "s" and tl == "s" and br == "m":
        return 1
    
    return 0
    
    

def main():
    with open("../../inputs/day4.txt", "r") as words_file:
        lines = [[y.lower() for y in list(x.strip())] for x in words_file.readlines()]
        words_count = 0
        for row in range(0, len(lines)):
            for col in range(0, len(lines[row])):
                if row == 0 or row == len(lines) - 1 or col == 0 or col == len(lines[row]) - 1:
                    continue

                if lines[row][col] == "a":
                    words_count += search(lines, row, col)
        
        print(words_count)


if __name__ == "__main__":
    main()