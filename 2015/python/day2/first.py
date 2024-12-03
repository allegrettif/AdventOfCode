def main():
    with open("../../inputs/day2.txt", "r") as sizes_file:
        sum = 0
        for line in [x.strip() for x in sizes_file.readlines()]:
            l, w, h = [int(x) for x in line.split("x")]
            min_el = min([l*w, w*h, l*h])
            sum += 2*l*w + 2*w*h + 2*h*l + min_el

        print(sum)



if __name__ == "__main__":
    main()