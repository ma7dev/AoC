import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv

def read(filename: str) -> str:
    data = None
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for _, row in enumerate(reader):
            data = row[0]
    return data

def part_1(data):
    utils.start_timer()
    counter = 0
    for i in range(len(data)):
        if data[i] == '(':
            counter += 1
        else:
            counter -= 1
    utils.pprint(1,counter)

def part_2(data):
    utils.start_timer()
    counter = 0
    target = -1
    for i in range(len(data)):
        if data[i] == '(':
            counter += 1
        else:
            counter -= 1
            if counter == -1:
                target = i+1
                break
    utils.pprint(2,target)
    
if __name__ == "__main__":
    print("Advent of Code 2015 - Day 1")
    print("-----------------------------")
    print("Example 1:")
    data = "(())"
    part_1(data)
    part_2(data)
    print("Example 2:")
    data = "((("
    part_1(data)
    part_2(data)
    print("Example 3:")
    data = "))((((("
    part_1(data)
    part_2(data)
    print("Example 4:")
    data = ")))"
    part_1(data)
    part_2(data)
    print("Example 5:")
    data = ")"
    part_1(data)
    part_2(data)
    print("Example 6:")
    data = "()())"
    part_1(data)
    part_2(data)
    print("-----------------------------")
    print("Test:")
    data = read("input.txt")
    part_1(data)
    part_2(data)