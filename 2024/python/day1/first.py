from io import TextIOWrapper

FILE_FOLDER = "inputs"

def main():
    # Read file
    with open(f"2024\inputs\day1.txt") as day_file:
        left: list[int] = []
        right: list[int] = []

        for line in day_file.readlines():
            left_num, right_num = line.split("   ")
            left.append(int(left_num))
            right.append(int(right_num))

        left.sort()
        right.sort()

        i = 0
        sum = 0
        for i in range(0, len(left)):
            sum = sum + abs(left[i] - right[i])


        print(sum)

        

if __name__ == "__main__":
    main()