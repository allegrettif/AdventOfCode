import functools

def calculate(a, b):
    print(a, b)
    return a + b*2

def main():
    with open("../../inputs/day2.txt", "r") as sizes_file:
        sum = 0
        for line in [x.strip() for x in sizes_file.readlines()]:
            sizes = [int(x) for x in line.split("x")]
            sizes.sort()

            wrap = functools.reduce(lambda a, b: a + b*2, sizes[0:2], 0)
            ribbon = functools.reduce(lambda a, b: a * b, sizes, 0)

            sum += wrap + ribbon

        print(sum)



if __name__ == "__main__":
    main()