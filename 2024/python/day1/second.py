def main():
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
        j = 0
        sum = 0
        for i in range(0, len(left)):
            count = 0
            for j in range(0, len(right)):
                if right[j] == left[i]:
                    count += 1
                elif right[j] > left[i]:
                    break

            sum += left[i] * count

        print(sum)

        

if __name__ == "__main__":
    main()