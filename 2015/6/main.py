# TODO:
import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import numpy as np
from typing import List
import pdb
from rich import print

def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        for _, row in enumerate(f):
            splitter = row.split()
            if "turn" in splitter:
                if splitter[1] == "on":
                    data.append([1,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]])
                else:
                    data.append([0,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]])
            else:
                data.append([-1,[int(x) for x in splitter[1].split(',')],[int(x) for x in splitter[3].split(',')]])
    return data
def part_1(data,verbose=False):
    utils.start_timer()
    arr = np.zeros([1000,1000])
    for action in data:
        if action[0] == 1:
            arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] = 1
        elif action[0] == 0:
            arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] = 0
        else:
            arr_ones = np.ones([1000,1000]) * -1
            arr_ones[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] = 1
            ones = np.equal(arr,arr_ones)
            arr_ones[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] = 0
            zeros = np.equal(arr,arr_ones)
            arr[zeros] = 1
            arr[ones] = 0
        if verbose:
            utils.pprint(1, arr[np.where(arr == 1)].size)
    utils.pprint(1, arr[np.where(arr == 1)].size)
        

def part_2(data,verbose=False):
    utils.start_timer()
    arr = np.zeros([1000,1000])
    for action in data:
        if action[0] == 1:
            arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] += 1
        elif action[0] == 0:
            arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] -= 1
            arr[np.where(arr < 0)] = 0
        else:
            arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] += 2
        if verbose:
            utils.pprint(2, np.sum(arr[np.where(arr>0)]))
    utils.pprint(2, np.sum(arr[np.where(arr>0)]))

if __name__ == "__main__":
    print("Advent of Code 2015 - Day 6")
    print("-----------------------------")
    print("Example 1:")
    data = read('ex1.txt')
    part_1(data)
    part_2(data)
    print("Example 2:")
    data = read('ex2.txt')
    part_1(data)
    part_2(data)
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(data)
    part_2(data)