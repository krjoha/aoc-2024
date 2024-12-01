from typing import List, Tuple


def get_list_distance_part1(locations: List[Tuple[int,int]]) -> int:
    total_distance = 0
    for col1, col2 in locations:
        distance = abs(col1 - col2)
        # print(distance)
        total_distance += distance

    return total_distance

def get_list_distance_part2(locations1: List[int], locations2: List[int]) -> int:
    location2_counts = dict.fromkeys(range(min(locations2)-1, max(locations2)+1), 0)
    for location in locations2:
        location2_counts[location] += 1
    
    total_distance = 0
    for location in locations1:
        distance = location * location2_counts.get(location, 0)
        total_distance += distance

    return total_distance


if __name__ == "__main__":
    locations1 = []
    locations2 = []

    with open("data/day1.csv") as f:
        for line in f:
            col1, col2 = line.strip().split("   ")
            locations1.append(int(col1))
            locations2.append(int(col2))
    
    result_part1 = get_list_distance_part1(zip(sorted(locations1), sorted(locations2)))
    print(result_part1)

    result_part2 = get_list_distance_part2(locations1, locations2)
    print(result_part2)