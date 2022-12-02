import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import numpy as np
from typing import List
import copy

def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n\n')  
        splitted_lines = [line.split() for line in lines]
        data = [[int(calorie) for calorie in calories] for calories in splitted_lines]   
    return data

def part_1(data, verbose=False):
    utils.start_timer()
    answer = max([sum(calories) for calories in data])
    utils.pprint(1, answer)

def part_2(data,verbose=False):
    utils.start_timer()
    # make a bucket for each elf
    answer = sum(
        sorted(
            [sum(calories) for calories in data]
        )[-3:]
    )
    utils.pprint(2, answer)

if __name__ == "__main__":
    print("Advent of Code 2022 - Day 1")
    print("-----------------------------")
    print("Example 1:")
    data = read('ex_1.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))