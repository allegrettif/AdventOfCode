def main():
    with open("../../inputs/day2.txt", "r") as report_file:
        safes = 0
        for line in [x.strip() for x in report_file.readlines()]:
            numbers = [int(x) for x in line.split(" ")]
            safe = True
            asc = numbers[0] - numbers[1] < 0
            
            for i in range(0, len(numbers)):
                if i == len(numbers) - 1:
                    break

                if abs(numbers[i] - numbers[i + 1]) == 0:
                    safe = False
                    break

                if abs(numbers[i] - numbers[i + 1]) > 3:
                    safe = False
                    break

                if asc and numbers[i] > numbers[i + 1]:
                    safe = False
                    break
                elif not asc and numbers[i] < numbers[i + 1]:
                    safe = False
                    break

            if safe:
                safes = safes + 1

        print(safes)
    

if __name__ == "__main__":
    main()