import re

if __name__ == "__main__":

    with open("../../inputs/day8.txt", "r") as input_file:
        steps = input_file.readline().strip()
        directions = {}

        for line in input_file.readlines()[1:]:
            start, ends = [x.strip() for x in line.split(" = ")]
            directions[start] = tuple([x.strip() for x in re.findall("\w+", ends)])

        steps_taken = 0
        closed = False
        for direction in sorted(directions.keys()):
            curr_dir = direction
            for step in steps:
                steps_taken = steps_taken + 1
                print("Taking a step", steps_taken, step, curr_dir, directions[curr_dir][1] if step == "R" else directions[curr_dir][0])
                if step == "R":
                    curr_dir = directions[curr_dir][1]
                else:
                    curr_dir = directions[curr_dir][0]
                
                if curr_dir == "ZZZ":
                    closed = True
                    break


            if closed:
                break;

        print(steps_taken)
                    


