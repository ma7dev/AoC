import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
from typing import List, Tuple

def read(filename: str) -> List[Tuple[str, int]]:
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for _, row in enumerate(reader):
            data.append((row[0].split(' ')[0],int(row[0].split(' ')[1])))
    return data

def part_1(data: List[Tuple[str, int]]):
    utils.start_timer()
    horizontal = 0
    depth = 0
    for i in range(len(data)):
        if data[i][0] == 'forward':
            horizontal += data[i][1]
        elif data[i][0] == 'down':
            depth += data[i][1]
        elif data[i][0] == 'up':
            depth -= data[i][1]
    utils.pprint(1,horizontal*depth)

def part_2(data: List[Tuple[str, int]]):
    utils.start_timer()
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(data)):
        if data[i][0] == 'forward':
            horizontal += data[i][1]
            depth += data[i][1]*aim
        elif data[i][0] == 'down':
            aim += data[i][1]
        elif data[i][0] == 'up':
            aim -= data[i][1]
    utils.pprint(2,horizontal*depth)

if __name__ == '__main__':
    print("Advent of Code 2021 - Day 2")
    print("-----------------------------")
    print("Example:")
    data = read('ex.txt')
    part_1(data)
    part_2(data)
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(data)
    part_2(data)