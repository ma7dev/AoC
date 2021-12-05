import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import numpy as np
from typing import List, Tuple

def read(filename: str) -> Tuple[List[List[int]], int, int]: 
    data = []
    max_val = -1
    max_val_y = -1
    with open(filename, 'r') as f:
        for _, row in enumerate(f):
            r = [int(i) for e in row.split('->') for i in e.replace(' ','').replace('\n','').split(',')]
            if max_val == -1:
                max_val = r[0]
                max_val_y = r[0]
            if r[0] > max_val:
                max_val = r[0]
            if r[2] > max_val:
                max_val = r[2]
            
            if r[1] > max_val_y:
                max_val_y = r[1]
            if r[3] > max_val_y:
                max_val_y = r[3]

            data.append(r)
    return data, max_val, max_val_y

def part_1(data,max_val, max_val_y,verbose=False):
    utils.start_timer()
    arr = np.zeros((max_val+1, max_val_y+1))
    for r in data:
        if r[0] == r[2]:
            # print(r)
            if r[1] <= r[3]:
                arr[r[0], r[1]:r[3]+1] += 1
            else:
                arr[r[0], r[3]:r[1]+1] += 1
        elif r[1] == r[3]:
            if r[0] <= r[2]:
                arr[r[0]:r[2]+1, r[1]] += 1
            else:
                arr[r[2]:r[0]+1, r[1]] += 1
    if verbose:
        print(arr.T)
    utils.pprint(1, len(arr[np.where(arr >= 2)]))
        

def part_2(data,max_val, max_val_y,verbose=False):
    utils.start_timer()
    arr = np.zeros((max_val+1, max_val_y+1))
    for r in data:
        if r[0] == r[2]:
            if r[1] < r[3]:
                arr[r[0], r[1]:r[3]+1] += 1
            else:
                arr[r[0], r[3]:r[1]+1] += 1
        elif r[1] == r[3]:
            if r[0] < r[2]:
                arr[r[0]:r[2]+1, r[1]] += 1
            else:
                arr[r[2]:r[0]+1, r[1]] += 1
        else:
            if r[0] < r[2]:
                if r[1] < r[3]:
                    i = 0
                    while r[0]+i < r[2]+1:
                        arr[r[0]+i, r[1]+i] += 1
                        i += 1
                else:
                    i = 0
                    while r[0]+i < r[2]+1:
                        arr[r[0]+i, r[1]-i] += 1
                        i += 1
            else:
                if r[1] <= r[3]:
                    i = 0
                    while r[2]+i < r[0]+1:
                        arr[r[0]-i, r[1]+i] += 1
                        i += 1
                else:
                    i = 0
                    while r[2]+i < r[0]+1:
                        arr[r[0]-i, r[1]-i] += 1
                        i += 1
    if verbose:
        print(arr.T)
    utils.pprint(2, len(arr[np.where(arr >= 2)]))
if __name__ == "__main__":
    print("Advent of Code 2021 - Day 5")
    print("-----------------------------")
    print("Example:")
    data,max_val, max_val_y = read('ex.txt')
    part_1(data,max_val, max_val_y)
    part_2(data,max_val, max_val_y)
    print("-----------------------------")
    print("Test:")
    data,max_val, max_val_y = read('input.txt')
    part_1(data,max_val, max_val_y)
    part_2(data,max_val, max_val_y)