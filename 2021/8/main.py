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
            signal_patterns, output_value = row.split('|')
            signal_patterns = signal_patterns.split()
            output_value = output_value.split()
            data.append([signal_patterns, output_value])
    return data

def part_1(data,verbose=False):
    utils.start_timer()
    len_num = [2,3,4,7]
    counter = 0
    for example in data:
        for e in example[1]:
            if len(e) in len_num:
                counter += 1
    utils.pprint(1, counter)
        
def part_2(data,verbose=False):
    utils.start_timer()
    numbers = {
        0: [1,2,3,5,6,7],
        1: [3,6],
        2: [1,3,4,5,7],
        3: [1,3,4,6,7],
        4: [2,3,4,7],
        5: [1,2,4,6,7],
        6: [1,2,4,5,6,7],
        7: [1,3,6],
        8: [1,2,3,4,5,6,7],
        9: [1,2,3,4,6,7],
    }
    l = "abcdefg"
    sum_ = 0
    for example in data:
        result = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        # 1
        one = ""
        for e in example[0]:
            if len(e) == 2:
                one = "". join(sorted(e))
                result[2].extend([e[0],e[1]])
                result[4].extend([e[0],e[1]])
                break
        # 7
        seven = ""
        for e in example[0]:
            if len(e) == 3:
                seven = "".join(sorted(e))
                for char in e:
                    if char not in list(one):
                        result[0] = char
                        break
        # 4
        for e in example[0]:
            if len(e) == 4:
                for char in e:
                    if char not in result[2]:
                        result[1].append(char)
                        result[3].append(char)
                break
        # 3
        for e in example[0]:
            if len(e) == 5 and all(cc in list(e) for cc in list(seven)):
                for char in e:
                    if char not in seven:
                        if char in result[3]:
                            result[3] = char
                            result[1].remove(char)
                            result[1] = str(result[1][0])
                        else:
                            result[6] = char
                break
        # 5
        for e in example[0]:
            if len(e) == 5 and all(cc in list(e) for cc in [result[0],result[1],result[3],result[6]]):
                for char in e:
                    if char not in [result[0],result[1],result[3],result[6]]:
                        result[5] = char
                        result[2].remove(char)
                        result[2] = str(result[2][0])
                        break
                break
        for char in l:
            if char not in result:
                result[4] = char
        answer = []
        for e in example[1]:
            if len(e) == 2:
                answer.append(1)
            elif len(e) == 3:
                answer.append(7)
            elif len(e) == 4:
                answer.append(4)
            elif len(e) == 5:
                e = "".join(sorted(e))
                for num in [2,3,5]:
                    if e == "".join(sorted([result[i-1] for i in numbers[num]])):
                        answer.append(num)
                        break
            elif len(e) == 6:
                e = "".join(sorted(e))
                for num in [0,6,9]:
                    if e == "".join(sorted([result[i-1] for i in numbers[num]])):
                        answer.append(num)
                        break
            else:
                answer.append(8)
        sum_ += int("".join([str(i) for i in answer]))
        
    utils.pprint(2, sum_)

if __name__ == "__main__":
    print("Advent of Code 2021 - Day 8")
    print("-----------------------------")
    print("Example 1:")
    data = read('ex1.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))
    print("Example 2:")
    data = read('ex2.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))