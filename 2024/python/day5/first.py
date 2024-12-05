def get_rules(rules_str: list[str]):
    return [(int(starting), int(ending)) for starting, ending in [rule_str.split("|") for rule_str in rules_str]]

def get_print_sequence(prints_str: list[str]):
    return [[int(num) for num in  sequence.split(",")] for sequence in prints_str]

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
            if is_valid_sequence(rules, sequence):
                sum += sequence[int(len(sequence) / 2)]
                
        print(sum)
            
if __name__ == "__main__":
    main()