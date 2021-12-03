import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
import copy
from typing import List

def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for _, row in enumerate(reader):
            data.append(row[0])
    return data

def part_1(data: List[str]):
    utils.start_timer()
    val = []
    val2 = []
    for j in range(len(data[0])):
        zeros = 0
        ones = 0
        for i in range(len(data)):
            if data[i][j] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            val.append('1')
            val2.append('0')
        else:
            val.append('0')
            val2.append('1')
    gamma = int("".join(val), 2)
    ep = int("".join(val2), 2)
    re = gamma*ep
    utils.pprint(1,re)

def part_2(data: List[str]):
    utils.start_timer()
    target = copy.deepcopy(data)
    for j in range(len(data[0])):
        zeros = 0
        ones = 0
        z = []
        o = []
        if len(target) == 1:
            break
        for i in range(len(target)):
            if target[i][j] == '0':
                zeros += 1
                z.append(target[i])
            else:
                ones += 1
                o.append(target[i])
        if zeros > ones:
            target = z
        else:
            target = o
    oo = int(target[0], 2)
    target = copy.deepcopy(data)
    for j in range(len(data[0])):
        zeros = 0
        ones = 0
        z = []
        o = []
        if len(target) == 1:
            break
        for i in range(len(target)):
            if target[i][j] == '0':
                zeros += 1
                z.append(target[i])
            else:
                ones += 1
                o.append(target[i])
        if zeros <= ones:
            target = z
        else:
            target = o
    c = int(target[0], 2)
    re = c*oo
    utils.pprint(2,re)

if __name__ == "__main__":
    # data = read("ex.txt")
    data = read("input.txt")
    part_1(data)
    part_2(data)