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
            # print(splitter)
            if "turn" in splitter:
                if splitter[1] == "on":
                    # print(f"turn, on {[1,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]]}")
                    data.append([1,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]])
                else:
                    # print(f"turn, off {[0,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]]}")
                    data.append([0,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]])
            else:
                # print(f"toggle {[-1,[int(x) for x in splitter[1].split(',')],[int(x) for x in splitter[3].split(',')]]}")
                data.append([-1,[int(x) for x in splitter[1].split(',')],[int(x) for x in splitter[3].split(',')]])
    return data
def validate(data):
    for cmd in data:
        # pdb.set_trace()
        if cmd[1][0] > cmd[2][0] or cmd[1][1] > cmd[2][1]:
            print(cmd)
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
            ones = np.where(arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] == 1)
            zeros = np.where(arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] == 0)
            arr[zeros] = 1
            arr[ones] = 0
        if verbose:
            utils.pprint(1, arr[np.where(arr == 1)].size)
    utils.pprint(1, arr[np.where(arr == 1)].size)
        

def part_2(data,verbose=False):
    utils.start_timer()
    utils.pprint(2, "")

# data = read('ex.txt')
data = read('input.txt')
validate(data)
# print(data)
# part_1(data,verbose=True)
# part_2(data)

# TODO:
import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import numpy as np
from typing import List
import pdb
def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        for _, row in enumerate(f):
            splitter = row.split()
            # print(splitter)
            if "turn" in splitter:
                if splitter[1] == "on":
                    # print(f"turn, on {[1,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]]}")
                    data.append([1,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]])
                else:
                    # print(f"turn, off {[0,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]]}")
                    data.append([0,[int(x) for x in splitter[2].split(',')],[int(x) for x in splitter[4].split(',')]])
            else:
                # print(f"toggle {[-1,[int(x) for x in splitter[1].split(',')],[int(x) for x in splitter[3].split(',')]]}")
                data.append([-1,[int(x) for x in splitter[1].split(',')],[int(x) for x in splitter[3].split(',')]])
    return data
def validate(data):
    for cmd in data:
        if cmd[1][0] > cmd[2][0]:
            print(cmd)
        if cmd[1][1] > cmd[2][1]:
            print(cmd)
def part_1(data,verbose=False):
    utils.start_timer()
    arr = np.zeros([1000,1000])
    for action in data:
        pdb.set_trace()
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
            ones = np.where(arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] == 1)
            zeros = np.where(arr[
                action[1][0]:action[2][0]+1,
                action[1][1]:action[2][1]+1
            ] == 0)
            arr[zeros] = 1
            arr[ones] = 0
        if verbose:
            utils.pprint(1, arr[np.where(arr == 1)].size)
    utils.pprint(1, arr[np.where(arr == 1)].size)
        

def part_2(data,verbose=False):
    utils.start_timer()
    utils.pprint(2, "")

data = read('ex.txt')
# data = read('input.txt')
# validate(data)
# print(data)
part_1(data,verbose=True)
# part_2(data)