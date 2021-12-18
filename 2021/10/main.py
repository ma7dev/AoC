import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
from typing import List
import copy

def mapping(char):
    if char == "(":
        return 1
    elif char == ")":
        return -1
    elif char == "[":
        return 2
    elif char == "]":
        return -2
    elif char == "{":
        return 3
    elif char == "}":
        return -3
    elif char == "<":
        return 4
    elif char == ">":
        return -4
def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        for _, row in enumerate(f):
            data.append(map(mapping,list(row.replace('\n', ''))))
    return data

def part_1(data, verbose=False):
    utils.start_timer()
    dict_ = {
        -1: [3,0],
        -2: [57,0],
        -3: [1197,0],
        -4: [25137,0]
    }
    for row in data:
        queue = []
        for char in row:
            if char > 0:
                queue.append(char)
            else:
                opening = queue.pop()
                if char*-1 != opening:
                    dict_[char][1] += 1
                    break
    sum_ = 0
    for _, value in dict_.items():
        sum_ += value[0]*value[1]
    utils.pprint(1, sum_)

def part_2(data,verbose=False):
    utils.start_timer()
    sum_list = []
    for row in data:
        queue = []
        complete = []
        valid = True
        for char in row:
            if char > 0:
                queue.append(char)
            else:
                opening = queue.pop()
                if char*-1 != opening:
                    valid = False
                    break
        if valid:
            sum_ = 0
            for char in reversed(queue):
                sum_ *= 5
                sum_ += char
            sum_list.append(sum_)
    sum_list.sort()
    mid = sum_list[len(sum_list)//2]
    utils.pprint(2, mid)


if __name__ == "__main__":
    print("Advent of Code 2021 - Day 10")
    print("-----------------------------")
    print("Example 1:")
    # 340773
    examples = [
        "()",
        "[]",
        "[<>({}){}[([])<>]]",
        "(((((((((())))))))))",
        "(]", # 57
        "(((()))}", # 1197
        "<([]){()}[{}])", # 3
        "{()()()>", # 25137
    ]
    data = [map(mapping,list(e)) for e in examples]
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))

    print("Example 2:")
    data = read('ex.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))

    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))