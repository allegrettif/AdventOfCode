def main():
    with open("../../inputs/day2.txt", "r") as report_file:
        safes = 0
        for line in [x.strip() for x in report_file.readlines()]:
            numbers = [int(x) for x in line.split(" ")]
            safes += safeness(numbers)
            print("---")

        print(safes)
    

def safeness(numbers: list[int]) -> int:
    asc = numbers[0] - numbers[1] < 0
    for i in range(0, len(numbers)):
        if i == len(numbers) - 1:
            return 1
        
        if not is_safe(asc, numbers[i], numbers[i+1]):
            has_possibile_safe = False
            for j in range(0, len(numbers)):
                new_safe = True
                new_nums = numbers[0:j] + numbers[j+1:]
                new_asc = new_nums[0] < new_nums[1]

                for z in range(0, len(new_nums)):
                    if z == len(new_nums) - 1:
                        break

                    if not is_safe(new_asc, new_nums[z], new_nums[z + 1]):
                        new_safe = False
                        break

                has_possibile_safe |= new_safe

                print(new_nums, has_possibile_safe)
            
            return 1 if has_possibile_safe else 0
                    
    return 1





def is_safe(asc: bool, first: int, second: int) -> bool:
    diff = abs(first - second)
    print(first, second, abs(first - second), 0 < diff <= 3 and ((asc and first < second) or (not asc and first > second)))
    return 0 < diff <= 3 and ((asc and first < second) or (not asc and first > second))

    

if __name__ == "__main__":
    main()