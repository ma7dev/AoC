import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import numpy as np
from typing import List
import copy

def read_part_1(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')  
        data = [
            (line[:len(line)//2], line[len(line)//2:]) 
            for line in lines
        ]
    return data

def read_part_2(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')  
        data = [
            (lines[i], lines[i+1], lines[i+2]) 
            for i in range(0,len(lines),3)
        ]
    return data

def part_1(data, verbose=False):
    utils.start_timer()
    repeated = []
    for rucksack in data:
        first_compartment = list(rucksack[0])
        for char in rucksack[1]:
            if char in first_compartment:
                repeated.append(char); break
    sum_ = 0
    for char in repeated:
        ascii_char = ord(char)
        if ascii_char < 97:
            sum_ += (ascii_char-65+27)
        else:
            sum_ += (ascii_char-97+1)
    answer = sum_
    utils.pprint(1, answer)

def part_2(data,verbose=False):
    utils.start_timer()
    repeated = []
    for group in data:
        first_rucksack = list(group[0])
        second_rucksack = list(group[1])
        for char in group[2]:
            if char in first_rucksack and char in second_rucksack:
                repeated.append(char); break
    sum_ = 0
    for char in repeated:
        ascii_char = ord(char)
        if ascii_char < 97:
            sum_ += (ascii_char-65+27)
        else:
            sum_ += (ascii_char-97+1)
    answer = sum_
    utils.pprint(2, answer)

if __name__ == "__main__":
    print("Advent of Code 2022 - Day 3")
    print("-----------------------------")
    print("Example 1:")
    data = read_part_1('ex_1.txt')
    part_1(copy.deepcopy(data))
    data = read_part_2('ex_1.txt')
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read_part_1('input.txt')
    part_1(copy.deepcopy(data))
    data = read_part_2('input.txt')
    part_2(copy.deepcopy(data))