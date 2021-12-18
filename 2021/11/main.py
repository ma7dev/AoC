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
        for _, row in enumerate(f):
            data.append([int(i) for i in list(row.replace('\n', ''))])
    return np.array(data)
def in_list(i, j, array):
    for row in array:
        if i == row[0] and j == row[1]:
            return True
    return False
def part_1(data, verbose=False):
    utils.start_timer()
    # increment every thing by 1
    # reset 10s to 0, add to flashed
    # increment every thing adjacent to 0 by 1
    # reset 10s to 0, add to flashed
    # increment every thing adjacent to 0 by 1
    num_flashed = 0
    for step in range(100):
        data += 1
        flashed = []
        while True:
            new_flashed = []
            for row in range(data.shape[0]):
                for col in range(data.shape[1]):
                    if data[row][col] >= 10 and not in_list(row,col,flashed):
                        num_flashed += 1
                        data[row][col] = 0
                        new_flashed.append((row,col))
            if len(new_flashed) == 0:
                break
            flashed.extend(new_flashed)
            for i,j in new_flashed:
                # up
                if j > 0 and not in_list(i,j-1,flashed):
                    data[i][j-1] += 1
                # down
                if j < data.shape[1]-1 and not in_list(i,j+1,flashed):
                    data[i][j+1] += 1
                # left
                if i > 0 and not in_list(i-1,j,flashed):
                    data[i-1][j] += 1
                # right
                if i < data.shape[0]-1 and not in_list(i+1,j,flashed):
                    data[i+1][j] += 1
                # up-right
                if i < data.shape[0]-1 and j < data.shape[1]-1 and not in_list(i+1,j+1,flashed):
                    data[i+1][j+1] += 1
                # up-left
                if i < data.shape[0]-1 and j > 0 and not in_list(i+1,j-1,flashed):
                    data[i+1][j-1] += 1
                # down-right
                if i > 0 and j < data.shape[1]-1 and not in_list(i-1,j+1,flashed):
                    data[i-1][j+1] += 1
                # down-left
                if i > 0 and j > 0 and not in_list(i-1,j-1,flashed):
                    data[i-1][j-1] += 1
    utils.pprint(1, num_flashed)

def part_2(data,verbose=False):
    utils.start_timer()
    num_flashed = 0
    goal = False
    step = 0
    while True:
        step += 1
        data += 1
        flashed = []
        while True:
            new_flashed = []
            for row in range(data.shape[0]):
                for col in range(data.shape[1]):
                    if data[row][col] >= 10 and not in_list(row,col,flashed):
                        num_flashed += 1
                        data[row][col] = 0
                        new_flashed.append((row,col))
            if len(new_flashed) == 0:
                break
            flashed.extend(new_flashed)
            if len(flashed) == 10*10:
                goal = True
                break
            for i,j in new_flashed:
                # up
                if j > 0 and not in_list(i,j-1,flashed):
                    data[i][j-1] += 1
                # down
                if j < data.shape[1]-1 and not in_list(i,j+1,flashed):
                    data[i][j+1] += 1
                # left
                if i > 0 and not in_list(i-1,j,flashed):
                    data[i-1][j] += 1
                # right
                if i < data.shape[0]-1 and not in_list(i+1,j,flashed):
                    data[i+1][j] += 1
                # up-right
                if i < data.shape[0]-1 and j < data.shape[1]-1 and not in_list(i+1,j+1,flashed):
                    data[i+1][j+1] += 1
                # up-left
                if i < data.shape[0]-1 and j > 0 and not in_list(i+1,j-1,flashed):
                    data[i+1][j-1] += 1
                # down-right
                if i > 0 and j < data.shape[1]-1 and not in_list(i-1,j+1,flashed):
                    data[i-1][j+1] += 1
                # down-left
                if i > 0 and j > 0 and not in_list(i-1,j-1,flashed):
                    data[i-1][j-1] += 1
        if goal:
            break
    utils.pprint(2, step)

if __name__ == "__main__":
    print("Advent of Code 2021 - Day 11")
    print("-----------------------------")
    print("Example 1:")
    data = read('ex_1.txt')
    part_1(copy.deepcopy(data))
    # all won't flash at the same time... Sadge
    # part_2(copy.deepcopy(data))
    print("Example 2:")
    data = read('ex_2.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))