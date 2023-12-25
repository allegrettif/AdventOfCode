
from typing import List, Tuple, Dict
import re


def file_to_maps(content: List[str]):
    almanac: Dict[str, List[Tuple[int, int, int]]] = {}
    curr_type: str = None

    for line in [x.strip() for x in content]:
        if line == '':
            curr_type = None
            continue

        if line.startswith("seeds"):
            # Seed
            _, nums = [x.strip() for x in line.split(":")]
            almanac["seeds"] = [int(num) for num in re.findall("\d+", nums)]

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


def convert(values: List[int], to: str, almanac: Dict[str, List[Tuple[int, int, int]]]):
    new_values = []
    for value in values:
        converted_value: int = None
        for item_conversion in almanac[to]:
            dest, src, rng = item_conversion

            if src <= value <= src + rng:
                converted_value = dest + (value - src)
                break

        if converted_value is not None:
            new_values.append(converted_value)
        else:
            new_values.append(value)

    return new_values


with open("../../inputs/day5.txt") as input_file:
    almanac = file_to_maps(input_file.readlines())

    soils = convert(almanac["seeds"], "seed-to-soil", almanac=almanac)
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

    print(min(locations))
