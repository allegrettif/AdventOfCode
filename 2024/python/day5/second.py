from functools import reduce

def get_rules(rules_str: list[str]):
    return [(int(starting), int(ending)) for starting, ending in [rule_str.split("|") for rule_str in rules_str]]

def get_print_sequence(prints_str: list[str]):
    return [[int(num) for num in  sequence.split(",")] for sequence in prints_str]

def swap_with_rules_in_place(rules: list[tuple[int, int]], sequence: list[int]):
    new_slice = sequence[:]
    
    while not is_valid_sequence(rules, new_slice):
        for starting, ending in rules:
            try:
                start_index = new_slice.index(starting)
                end_index = new_slice.index(ending)
                
                if start_index < end_index:
                    continue
                
                temp = new_slice[start_index]
                new_slice[start_index] = new_slice[end_index]
                new_slice[end_index] = temp
                
            except ValueError:
                continue
            
    return new_slice

def is_valid_sequence(rules: tuple[int, int], sequence: list[int]):
    is_correct = True
    for starting, ending in rules:
        try:
            is_correct &= sequence.index(starting) < sequence.index(ending)
        except ValueError:
            continue
        
    return is_correct

def main():
    
    with open("../../inputs/day5.txt", "r") as print_file:
        lines = [x.strip() for x in print_file.readlines()]
        rules = get_rules(lines[:lines.index('')])
        orders = get_print_sequence(lines[lines.index('')+1:])
        
        sum = 0
        for sequence in orders:
            if not is_valid_sequence(rules, sequence):
                new_sequence = swap_with_rules_in_place(rules, sequence)
                sum += new_sequence[int(len(sequence) / 2)]
                
        print(sum)
            
if __name__ == "__main__":
    main()