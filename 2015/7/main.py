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
            # split by ->
            # split by ' ' for split[0]
                # 3 elements -> [split[0][1], split[0][0], split[0][2]]
                # 2 elements -> [split[0][0], split[0][1]]
            # print(row)
            left, right = row.split('->')
            left = left.split()
            right = right.split()[0]
            if len(left) == 3:
                left = [left[1], left[0], left[2]]
            elif len(left) == 1:
                left = ['ASSIGN', left[0]]
            data.append([left, right])
    return data
def commands(cmd, params, registers):
    if len(params) == 1:
        # pre process
        if params[0] not in registers.keys():
            params[0] = max(0, min(int(params[0]),65535))
        else:
            params[0] = registers[params[0]]
        if params[0] == None:
            return None
        if cmd == 'ASSIGN':
            return params[0]
        elif cmd == 'NOT':
            return ~ params[0] & 0xffff
    else:
        # pre process
        if params[0] not in registers.keys():
            params[0] = max(0, min(int(params[0]),65535))
        else:
            params[0] = registers[params[0]]
        if params[1] not in registers.keys():
            params[1] = max(0, min(int(params[1]),65535))
        else:
            params[1] = registers[params[1]]
        if params[0] == None or params[1] == None:
            return None
        if cmd == 'AND':
            return params[0] & params[1]
        elif cmd == 'OR':
            return params[0] | params[1]
        elif cmd == 'LSHIFT':
            return params[0] << params[1]
        elif cmd == 'RSHIFT':
            return params[0] >> params[1]
        elif cmd == 'XOR':
            return params[0] ^ params[1]
    
def part_1(data,focus, verbose=False):
    utils.start_timer()
    registers = {}
    for _, target in data:
        registers[target] = None
    while len(data) > 0:
        waited = []
        for info, target in data:
            tmp = commands(info[0], info[1:] , registers)
            if tmp != None:
                registers[target] = max(0, min(tmp,65535))
            else:
                waited.append([info,target])
        data = waited
    utils.pprint(1, f"{focus}: {registers[focus]}")
        
def part_2(data,focus=['a','b'],verbose=False):
    utils.start_timer()
    backup = copy.deepcopy(data)
    registers = {}
    for _, target in data:
        registers[target] = None
    while len(data) > 0:
        waited = []
        for info, target in data:
            tmp = commands(info[0], info[1:] , registers)
            if tmp != None:
                registers[target] = max(0, min(tmp,65535))
            else:
                waited.append([info,target])
        data = waited
    backup_val = registers[focus[0]]
    data = backup
    registers = {}
    for info, target in data:
        registers[target] = None
    while len(data) > 0:
        waited = []
        for info, target in data:
            if info[0] == 'ASSIGN' and target == focus[1]:
                registers[target] = max(0, min(backup_val,65535))
            else:
                tmp = commands(info[0], info[1:] , registers)
                if tmp != None:
                    registers[target] = max(0, min(tmp,65535))
                else:
                    waited.append([info,target])
        data = waited
    utils.pprint(2, f"{focus[0]}: {registers[focus[0]]}")

if __name__ == "__main__":
    print("Advent of Code 2015 - Day 7")
    print("-----------------------------")
    print("Example:")
    data = read('ex.txt')
    focus = ['d', 'e']
    part_1(copy.deepcopy(data),focus[0])
    part_2(copy.deepcopy(data),focus)
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    focus = ['a', 'b']
    part_1(copy.deepcopy(data),focus[0])
    part_2(copy.deepcopy(data),focus)