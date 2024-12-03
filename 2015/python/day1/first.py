def main():
    with open("../../inputs/day1.txt", "r") as floor_file:
        directions = floor_file.readline()
        floor = 0
        for parenthesis in directions:
            if parenthesis == "(":
                floor += 1
            else:
                floor -= 1

        print(floor)


if __name__ == "__main__":
    main()