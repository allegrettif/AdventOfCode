def main():
    with open("../../inputs/day1.txt", "r") as floor_file:
        directions = floor_file.readline()
        position = None
        floor = 0
        for index, parenthesis in enumerate(directions):
            if parenthesis == "(":
                floor += 1
            else:
                floor -= 1

            if floor == -1:
                position = index
                break

        print(position + 1)


if __name__ == "__main__":
    main()