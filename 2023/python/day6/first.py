import re

def read_times(file_content: list[str]) -> dict[str, list[int]]:
    values_dict = {}
    for line in file_content:

        key, values = [x.strip() for x in line.split(":")]
        values_dict[key.lower()] = [int(x) for x in re.findall("\d+", values)]

    return values_dict


if __name__ == "__main__":
    with open("../../inputs/day6.txt") as input_file:
        board = read_times(input_file.readlines())
        races = zip(board["time"], board["distance"])
        win_ways_num = 1
        for time, record_distance in races:
            broken_records = 0
            for time_pressed in range(0, time + 1):
                remaining_time = time - time_pressed

                if remaining_time == time: continue
                distance_elapse = (remaining_time) * time_pressed

                if distance_elapse > record_distance:
                    broken_records = broken_records + 1

            win_ways_num = win_ways_num * broken_records

        print(win_ways_num)
            
            # La barca parte da velocità 0 e guadagna 1 di velocità per ogni 
            # millisecondo che è stato cliccato il tasto sopra per caricarla

