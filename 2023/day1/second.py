numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


# jjfvnnlfivejj1
# -------^----- trovo una lettera che corrisponde alla prima lettera di un numero
# pcg91vqrfpxxzzzoneightzt

with open("second.txt", "r") as input_file:
    sum = 0
    for line in [x.strip() for x in input_file.readlines()]:
        first_number: str = None
        for i in range(0, len(line)):
            if line[i].isdigit():
                first_number = line[i]
                break

            number_found: bool = False
            for number in numbers.keys():
                for j in range(0, len(number)):
                    # print(i, j, number[j], line[i+j], number)
                    if line[i+j] != number[j]:
                        break

                    if j == len(number) - 1:
                        number_found = True
                        break

                if number_found:
                    break

            if number_found:
                first_number = numbers[number]
                break

        second_number: str = None
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                second_number = line[i]
                break

            number_found: bool = False
            for number in numbers.keys():
                if i + len(number) > len(line):
                    continue

                for j in range(0, len(number)):
                    # print(i, j, number[j], line[i+j], number, line)
                    if line[i+j] != number[j]:
                        break

                    if j == len(number) - 1:
                        number_found = True
                        break

                if number_found:
                    break

            if number_found:
                second_number = numbers[number]
                break
        if first_number is None or second_number is None:
            print(line)
            continue

        sum = sum + int(f"{first_number}{second_number}")
        # print(line, first_number, second_number, sum)
    print(sum)
