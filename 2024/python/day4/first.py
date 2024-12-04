XMAS = "XMAS"
XMAS_LEN = len(XMAS)

def btt_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row - i][col] for i in range(0, XMAS_LEN)]

def ltrt_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row - i][col + i] for i in range(0, XMAS_LEN)]

def ltr_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row][col + i] for i in range(0, XMAS_LEN)]

def ltrb_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row + i][col + i] for i in range(0, XMAS_LEN)]

def ttb_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row + i][col] for i in range(0, XMAS_LEN)]

def rtbl_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row + i][col - i] for i in range(0, XMAS_LEN)]

def rtl_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row][col - i] for i in range(0, XMAS_LEN)]

def rttl_slice(matrix: list[list[str]], row: int, col: int):
    return [matrix[row - i][col - i] for i in range(0, XMAS_LEN)]

def search(slice: list[str]):
    assert len(slice) == XMAS_LEN

    for i in range(0, XMAS_LEN):
        if slice[i] != XMAS[i]:
            return 0

    print(slice, "OK")
    return 1

def main():
    with open("../../inputs/day4.txt", "r") as words_file:
        lines = [list(x.strip()) for x in words_file.readlines()]
        words_count = 0
        for row in range(0, len(lines)):
            for col in range(0, len(lines[row])):

                if row + 1 - XMAS_LEN < 0: # NO LEFT
                    if col + XMAS_LEN > len(lines[row]): # NO RIGHT 0 1 2 3 4 5 x 7 8 9 
                        words_count += search(ttb_slice(lines, row, col)) + \
                            search(rtbl_slice(lines, row, col)) + \
                            search(rtl_slice(lines, row, col))
                    elif col + 1 - XMAS_LEN < 0: # NO LEFT
                        words_count += search(ltr_slice(lines, row, col)) + \
                            search(ltrb_slice(lines, row, col)) + \
                            search(ttb_slice(lines, row, col))
                    else: # MIDDLE
                        words_count += search(ltr_slice(lines, row, col)) + \
                            search(ltrb_slice(lines, row, col)) + \
                            search(ttb_slice(lines, row, col)) + \
                            search(rtbl_slice(lines, row, col)) + \
                            search(rtl_slice(lines, row, col))
                elif row + XMAS_LEN > len(lines): # NO RIGHT
                    if col + XMAS_LEN > len(lines[row]):
                        words_count += search(btt_slice(lines, row, col)) + \
                            search(rttl_slice(lines, row, col)) + \
                            search(rtl_slice(lines, row, col))
                    elif col + 1 - XMAS_LEN < 0: # NO LEFT
                        words_count += search(btt_slice(lines, row, col)) + \
                            search(ltrt_slice(lines, row, col)) + \
                            search(ltr_slice(lines, row, col))
                    else: # MIDDLE
                        words_count += search(btt_slice(lines, row, col)) + \
                            search(ltrt_slice(lines, row, col)) + \
                            search(ltr_slice(lines, row, col)) + \
                            search(rtl_slice(lines, row, col)) + \
                            search(rttl_slice(lines, row, col))
                else: # MIDDLE
                    if col + XMAS_LEN > len(lines[row]): # RIGHT
                        words_count += search(btt_slice(lines, row, col)) + \
                            search(ttb_slice(lines, row, col)) + \
                            search(rtbl_slice(lines, row, col)) + \
                            search(rtl_slice(lines, row, col)) + \
                            search(rttl_slice(lines, row, col))
                    elif col + 1 - XMAS_LEN < 0: # NO LEFT
                        words_count += search(btt_slice(lines, row, col)) + \
                            search(ltrt_slice(lines, row, col)) + \
                            search(ltr_slice(lines, row, col)) + \
                            search(ltrb_slice(lines, row, col)) + \
                            search(ttb_slice(lines, row, col))
                    else: # MIDDLE
                        words_count += search(btt_slice(lines, row, col)) + \
                            search(ltrt_slice(lines, row, col)) + \
                            search(ltr_slice(lines, row, col)) + \
                            search(ltrb_slice(lines, row, col)) + \
                            search(ttb_slice(lines, row, col)) + \
                            search(rtbl_slice(lines, row, col)) + \
                            search(rtl_slice(lines, row, col)) + \
                            search(rttl_slice(lines, row, col))
        
        print(words_count)


if __name__ == "__main__":
    main()