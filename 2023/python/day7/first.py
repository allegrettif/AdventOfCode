
import functools

SYMBOL_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
HAND_ORDER = ["FIVE_KIND", "FOUR_KIND", "FULL_HOUSE", "THREE_KIND", "TWO_PAIR", "ONE_PAIR", "HIGH_CARD"]


def compare(a: tuple[str, int, str, str], b: tuple[str, int, str, str]) -> int:
    a_hand, a_point, a_type, a_highest = a
    b_hand, b_point, b_type, b_highest = b
    if a_type == b_type:
        for i in range(0, len(a_hand)):
            if a_hand[i] != b_hand[i]:
                return SYMBOL_ORDER.index(a_hand[i]) - SYMBOL_ORDER.index(b_hand[i])

    return HAND_ORDER.index(a_type) - HAND_ORDER.index(b_type)

def highest_symbol(hand: str) -> str:
    highest_symbol = SYMBOL_ORDER[-1]
    for symbol in hand:
        if SYMBOL_ORDER.index(symbol) < SYMBOL_ORDER.index(highest_symbol):
                    highest_symbol = symbol

    return highest_symbol

# [A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2]
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
def convert_to_hands(file_content: list[str]) -> list[tuple[str, int, str, str]]:
    hands: list[tuple[str, int, str, str]] = []
    for line in file_content:
        hand, points = line.split(" ")

        chars = {}

        for symbol in hand:
            if symbol in chars:
                chars[symbol] = chars[symbol] + 1
                continue
            chars[symbol] = 1


        keys = chars.keys()
        hand_type: str = None
        if len(keys) == len(hand):
            # All differents
            hand_type = "HIGH_CARD"
        elif len(keys) == 1:
            # All the same
            hand_type = "FIVE_KIND"
        elif len(keys) == 2:
            # Tris and pair
            # OR
            # Four of a kind and a single
            first, second = keys
            if chars[first] == 4 or chars[second] == 4:
                hand_type = "FOUR_KIND"
            else:
                hand_type = "FULL_HOUSE"

        elif len(keys) == 3:
            # Pair and Pair and One
            # OR
            # Tris and One and One
            first, second, third = keys
            if chars[first] == 3 or chars[second] == 3 or chars[third] == 3:
                hand_type = "THREE_KIND"
            else:
                hand_type = "TWO_PAIR"

        elif len(keys) == 4:
            # Pair and One and One and One
            hand_type = "ONE_PAIR"

            

        hands.append((hand, int(points), hand_type, highest_symbol(hand)))

    return hands

def sum(acc: int, curr: tuple[int, tuple[str, int, str, str]]) -> int:
    index, hand = curr
    return acc + (hand[1] * (index + 1))

with open("../../inputs/day7.txt") as input_file:
    hands = convert_to_hands(input_file.readlines())
    hands = sorted(hands, key=functools.cmp_to_key(compare))
    hands.reverse()
    hands_points = functools.reduce(sum, enumerate(hands), 0)
    print(hands_points)