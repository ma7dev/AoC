import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
from typing import List

def read(filename: str) -> List[int]:
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for _, row in enumerate(reader):
            data.append(int(row[0]))
    return data

def part_1(data: List[int]):
    utils.start_timer()
    counter = 0
    prev = data[0]
    for i in range(1,len(data)):
        if data[i] > prev:
            counter += 1
        prev = data[i]
    utils.pprint(1,counter)

def part_2(data: List[int]):
    utils.start_timer()
    counter = 0
    for i in range(len(data)-3):
        if data[i+3] > data[i]:
            counter += 1
    utils.pprint(2,counter)

if __name__ == "__main__":
    print("Advent of Code 2021 - Day 1")
    print("-----------------------------")
    print("Example:")
    data = read("ex.txt")
    part_1(data)
    part_2(data)
    print("-----------------------------")
    print("Test:")
    data = read("input.txt")
    part_1(data)
    part_2(data)