
from typing import List, Tuple, Dict, Union
from math import floor
import functools
import re
import os
import concurrent.futures

# (31 10)
# (40 30 15)

# 24 < 30
#     24 + 15 = 39 > 30

# 31 > 30
#     41 < 45
#         (41, 10)

def worker(seed_group: Tuple[int, int], almanac: Dict[str, List[Tuple[int, int, int]]]) -> int:
    srt, rng = seed_group
    extended_seeds = [srt + i for i in range(0, rng)]

    soils = convert(extended_seeds, "seed-to-soil", almanac=almanac)
    fertilizers = convert(soils, "soil-to-fertilizer", almanac=almanac)
    water = convert(fertilizers,
                    "fertilizer-to-water", almanac=almanac)
    light = convert(water, "water-to-light", almanac=almanac)
    temperatures = convert(
        light, "light-to-temperature", almanac=almanac)
    humidity = convert(temperatures,
                       "temperature-to-humidity", almanac=almanac)
    locations = convert(humidity,
                        "humidity-to-location", almanac=almanac)

    return min(locations)

def generate_numbers(rng: Tuple[int, int]) -> List[int]:
    start, offset = rng
    return [start + i for i in range(0, offset)]

# def generate_seeds(seeds_info: List[Tuple[int, int]]) -> List[int]:

#     seeds = []
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         futures = {executor.submit(
#             generate_numbers, info): info for info in seeds_info}

#         for index, future in enumerate(concurrent.futures.as_completed(futures)):
#             result = future.result()
#             seeds.extend(result)
#             print("ended", index, future.done())

#     return seeds


def file_to_maps(content: List[str]) -> Dict[str, List[Union[Tuple[int, int, int], Tuple[int, int]]]]:
    almanac: Dict[str, List[Tuple[int, int, int]]] = {}
    curr_type: str = None

    for line in [x.strip() for x in content]:
        if line == '':
            curr_type = None
            continue

        if line.startswith("seeds"):
            # Seed
            _, nums = [x.strip() for x in line.split(":")]
            seeds_infos: List[str] = [
                tuple([int(num) for num in x.split(" ")]) for x in re.findall("\d+ \d+", nums)]

            almanac["seeds"] = seeds_infos
            continue

        if re.search("\\smap", line):
            curr_type, _ = line.split(" ")
            almanac[curr_type] = []
            continue

        if curr_type is not None:
            dest_range, source_range, len_range = [
                int(num) for num in line.split(" ")]
            if curr_type in almanac:
                almanac[curr_type].append(
                    (dest_range, source_range, len_range))

    return almanac


# def multi_thread_convert(from_values: List[int], to_values: List[Tuple[int, int, int]]) -> List[int]:
#     new_values = []
#     for value in from_values:
#         converted_value: int = None
#         for item_conversion in to_values:
#             dest, src, rng = item_conversion

#             if src <= value <= src + rng:
#                 converted_value = dest + (value - src)
#                 break

#         if converted_value is not None:
#             new_values.append(converted_value)
#         else:
#             new_values.append(value)

#     return new_values

enum_bello = {
    "SOIL": "seed-to-soil",
    "FERTILIZER": "soil-to-fertilizer",
    "WATER": "fertilizer-to-water",
    "LIGHT": "water-to-light",
    "TEMPERATURE": "light-to-temperature",
    "HUMIDITY": "temperature-to-humidity",
    "LOCATION": "humidity-to-location"
}

TO_PRINT = None

def convert(values: List[int], to: str, almanac: Dict[str, List[Union[Tuple[int, int, int], List[int]]]]):
    print(to, len(almanac[to]))
    new_values = []
    for v_index, value in enumerate(values):
        converted_value: int = None
        for index, item_conversion in enumerate(almanac[to]):
            dest, src, rng = item_conversion
            # os.system('clear')

            if src <= value <= src + rng:
                converted_value = dest + (value - src)
                if to == TO_PRINT:
                    print(f"Value: {value} Map: {(dest, src, rng)} Mapped: {converted_value}")
                break

        if converted_value is not None:
            new_values.append(converted_value)
        else:
            new_values.append(value)

    print(new_values)

    return new_values

def remove_duplicates(acc: List[Tuple[int, int]], curr: Tuple[int, int]):
    if acc is None:
        return [curr]
    
    if curr not in acc:
        acc.append(curr)
        return acc
    
    return acc

# TO_CHECK = (61, 7)
# TO_CHECK = (61, 9)
# TO_CHECK = (55, 13)

def convert_group(groups: List[Tuple[int, int]], to_groups: List[Tuple[int,int,int]], to: str):
    new_groups = []

    for g_srt, g_rng in groups:
        g_end = g_srt + g_rng - 1
        to_remove = False

        for dest, src, rng in to_groups:
            src_end = src + rng - 1

            if g_srt < src:
                # Caso esterno sinistra

                if g_end < src:
                    no_change = (g_srt, g_rng)
                    if no_change not in new_groups: new_groups.append(no_change)
                    if to == TO_PRINT:
                        print(f"Group\t{(g_srt, g_rng)}\tMap\t{(dest, src, rng)}\tResults\t{[no_change]}")
                    continue

                elif src <= g_end <= src_end:
                    
                    remaining_left = src - g_srt
                    remaining_inside = g_rng - remaining_left
                    
                    left = (g_srt, remaining_left)
                    inside = (dest, remaining_inside)

                    if (g_srt, g_rng) in new_groups:
                        new_groups.remove((g_srt, g_rng))

                    if inside not in new_groups: new_groups.append(inside)
                    if left not in new_groups: new_groups.append(left)
                    if to == TO_PRINT:
                        print(f"Group\t{(g_srt, g_rng)}\tMap\t{(dest, src, rng)}\tResults\t{[left, inside]}")
                    continue

                else:

                    remaining_left = src - g_srt
                    remaining_inside = rng
                    remaining_right = g_end - src_end
                    
                    left = (g_srt, remaining_left)
                    inside = (dest, remaining_inside)
                    right = (src_end + 1, remaining_right)

                    if (g_srt, g_rng) in new_groups:
                        new_groups.remove((g_srt, g_rng))

                    if left not in new_groups: new_groups.append(left)
                    if inside not in new_groups: new_groups.append(inside)
                    if right not in new_groups: new_groups.append(right)
                    if to == TO_PRINT:
                        print(f"Group\t{(g_srt, g_rng)}\tMap\t{(dest, src, rng)}\tResults\t{[left, inside, right]}")
                    continue

            elif g_srt > src_end:
                # Caso esterno a destra
                no_change = (g_srt, g_rng)
                if no_change not in new_groups: new_groups.append(no_change)
                if to == TO_PRINT:
                    print(f"Group\t{(g_srt, g_rng)}\tMap\t{(dest, src, rng)}\tResults\t{[no_change]}")
                continue

            else:
                if g_end <= src_end:
                    offset = g_srt - src
                    inside = (dest + offset, g_rng)

                    if (g_srt, g_rng) in new_groups:
                        new_groups.remove((g_srt, g_rng))
                    if inside not in new_groups: new_groups.append(inside)
                    if to == TO_PRINT:
                        print(f"Group\t{(g_srt, g_rng)}\tMap\t{(dest, src, rng)}\tResults\t{[inside]}")
                    continue
                
                else:
                    offset = g_srt - src
                    remaining_inside = g_rng - (g_end - src_end)
                    remaining_right = g_rng - remaining_inside

                    inside = (dest + offset, remaining_inside)
                    right = (src_end + 1, remaining_right)


                    if (g_srt, g_rng) in new_groups:
                        new_groups.remove((g_srt, g_rng))
                    if inside not in new_groups: new_groups.append(inside)
                    if right not in new_groups: new_groups.append(right)
                    if to == TO_PRINT:
                        print(f"Group\t{(g_srt, g_rng)}\tMap\t{(dest, src, rng)}\tResults\t{[inside, right]}")
                    continue



    return new_groups

def test(seeds: List[Tuple[int, int]]):
    soils = convert_group(seeds, almanac["seed-to-soil"],"seed-to-soil" )
    fertilizers = convert_group(soils, almanac["soil-to-fertilizer"],"soil-to-fertilizer" )
    water = convert_group(fertilizers, almanac["fertilizer-to-water"],"fertilizer-to-water" )
    lights = convert_group(water, almanac["water-to-light"],"water-to-light" )
    temperatures = convert_group(lights, almanac["light-to-temperature"], "light-to-temperature")
    humidity = convert_group(temperatures, almanac["temperature-to-humidity"], "temperature-to-humidity")
    locations = convert_group(humidity, almanac["humidity-to-location"], "humidity-to-location")

    return min(locations)

if __name__ == "__main__":
    with open("../../inputs/day5.txt") as input_file:
        almanac = file_to_maps(input_file.readlines())
        # for key in almanac.keys():
        #     print(f"Key: {key} Values: {almanac[key]}")

        seeds: List[Tuple[int, int]] = almanac["seeds"]
        # new_seeds = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(seeds)) as executor:
            futures = {executor.submit(test, [seed_group]): seed_group for seed_group in seeds}

            for future in concurrent.futures.as_completed(futures):
                print(future.result())

        # for srt, rng in seeds:
        #     new_seeds.extend([srt + i for i in range(0, rng)])
        

        # print(sorted(new_seeds))
        # soils = convert(new_seeds, "seed-to-soil", almanac=almanac)
        # fertilizers = convert(soils, "soil-to-fertilizer", almanac=almanac)
        # water = convert(fertilizers, "fertilizer-to-water", almanac=almanac)
        # lights = convert(water, "water-to-light", almanac=almanac)
        # temperatures = convert(lights, "light-to-temperature", almanac=almanac)
        # humidity = convert(temperatures, "temperature-to-humidity", almanac=almanac)
        # locations = convert(humidity, "humidity-to-location", almanac=almanac)

        # print(min(locations))

        # minimum: int = None
        # for srt, end in locations:
        #     if minimum is None:
        #         minimum = srt
        #         continue

        #     if minimum > srt:
        #         minimum = srt

        # print(minimum)
        # print(min(locations))

        # soils = convert(almanac["seeds"], "seed-to-soil", almanac=almanac)
        # fertilizers = convert(soils, "soil-to-fertilizer", almanac=almanac)
        # water = convert(fertilizers,
        #                 "fertilizer-to-water", almanac=almanac)
        # light = convert(water, "water-to-light", almanac=almanac)
        # temperatures = convert(
        #     light, "light-to-temperature", almanac=almanac)
        # humidity = convert(temperatures,
        #                    "temperature-to-humidity", almanac=almanac)
        # locations = convert(humidity,
        #                     "humidity-to-location", almanac=almanac)


