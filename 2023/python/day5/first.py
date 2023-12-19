
from typing import List, Tuple, Dict
import re

def file_to_maps(content: List[str]):
    almanac: Dict[str, Tuple[int, int, int]] = {}
    curr_type: str = None

    for line in [x.strip() for x in content]:
        if line == '':
            curr_type = None
            continue

        if line.startswith("seeds"):
            # Seed
            _, nums = [x.strip() for x in line.split(":")]
            almanac["seeds"] = re.findall("\d+", nums)

        if re.search("\\smap", line):
            curr_type, _ = line.split(" ")
            almanac[curr_type] = []
            continue

        if curr_type is not None:
            dest_range, source_range, len_range = line.split(" ")
            if curr_type in almanac:
                almanac[curr_type].append((dest_range, source_range, len_range))

    
    print(almanac)
            

with open("../../inputs/day5.txt") as input_file:
    file_to_maps(input_file.readlines())