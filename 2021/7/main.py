import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
from typing import List
import copy
import math

def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        for _, row in enumerate(f):
            data.extend([int(i) for i in row.split(',')])
    return data

def part_1(data,verbose=False):
    utils.start_timer()
    new_dict = {}
    for i in data:
        if i not in new_dict:
            new_dict[i] = {"sum": 0, "counter": 0}
        new_dict[i]["counter"] += 1
    low_fuel = math.inf
    for k, v in new_dict.items():
        for i, j in new_dict.items():
            if i != k:
                new_dict[k]["sum"] += abs(i-k) * new_dict[i]["counter"]
        low_fuel = min(low_fuel, new_dict[k]["sum"])
    utils.pprint(1, low_fuel)
        

def part_2(data,verbose=False):
    utils.start_timer()
    new_dict = {}
    for i in data:
        if i not in new_dict:
            new_dict[i] = {"sum": 0, "counter": 0}
        new_dict[i]["counter"] += 1
    low_fuel = math.inf
    val_range = [min(new_dict.keys()), max(new_dict.keys())]
    for k in range(val_range[0], val_range[1]+1):
        if k not in new_dict:
            new_dict[k] = {"sum": 0, "counter": 0}
        for i, j in new_dict.items():
            if i != k:
                new_dict[k]["sum"] += sum(range(1,abs(i-k)+1)) * new_dict[i]["counter"]
        low_fuel = min(low_fuel, new_dict[k]["sum"])
    utils.pprint(2, low_fuel)

if __name__ == "__main__":
    print("Advent of Code 2021 - Day 7")
    print("-----------------------------")
    print("Example:")
    data = read('ex.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))