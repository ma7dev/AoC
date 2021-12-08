import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
from typing import List
import copy

def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        for _, row in enumerate(f):
            data.extend([int(i) for i in row.split(',')])
    return data

def part_1(data,end_day,verbose=False):
    utils.start_timer()
    curr_day = 1
    new_dict_empty = {}
    for i in range(9):
        new_dict_empty[i] = 0
    my_dict = copy.deepcopy(new_dict_empty)
    for i in range(len(data)):
        my_dict[data[i]] += 1
    while curr_day <= end_day:
        new_dict = copy.deepcopy(new_dict_empty)
        for i in range(9):
            if i > 0:
                new_dict[i-1] += my_dict[i]
            else:
                new_dict[8] += my_dict[i]
                new_dict[6] += my_dict[i]
        my_dict = copy.deepcopy(new_dict)
        curr_day += 1
    if verbose:
        print(data)
    sum_ = 0
    for v in my_dict.values():
        sum_ += v
    utils.pprint(1, sum_)
        

def part_2(data,end_day,verbose=False):
    utils.start_timer()
    curr_day = 1
    new_dict_empty = {}
    for i in range(9):
        new_dict_empty[i] = 0
    my_dict = copy.deepcopy(new_dict_empty)
    for i in range(len(data)):
        my_dict[data[i]] += 1
    while curr_day <= end_day:
        new_dict = copy.deepcopy(new_dict_empty)
        for i in range(9):
            if i > 0:
                new_dict[i-1] += my_dict[i]
            else:
                new_dict[8] += my_dict[i]
                new_dict[6] += my_dict[i]
        my_dict = copy.deepcopy(new_dict)
        curr_day += 1
    # print(curr_day, my_dict)
    if verbose:
        print(data)
    sum_ = 0
    for v in my_dict.values():
        sum_ += v
    utils.pprint(2, sum_)
if __name__ == "__main__":
    print("Advent of Code 2021 - Day 6")
    print("-----------------------------")
    print("Example:")
    data = read('ex.txt')
    part_1(copy.deepcopy(data),80)
    part_2(copy.deepcopy(data),256)
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data),80)
    part_2(copy.deepcopy(data),256)