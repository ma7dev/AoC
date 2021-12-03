import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
from typing import List

def read(filename: str) -> List[List[int]]:
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for _, row in enumerate(reader):
            tmp = [int(j) for j in row[0].split('x')]
            tmp.sort()
            data.append(tmp)
    return data
    
def part_1(data: List[List[int]]):
    utils.start_timer()
    sum_ = 0
    for example in data:
        sum_ += example[0]*example[1]
        sum_ += 2*example[0]*example[1]
        sum_ += 2*example[1]*example[2]
        sum_ += 2*example[0]*example[2]
    utils.pprint(1,sum_)

def part_2(data: List[List[int]]):
    utils.start_timer()
    sum_ = 0
    for example in data:
        sum_ += 2*example[0]+2*example[1]
        sum_ += example[0]*example[1]*example[2]
    utils.pprint(1,sum_)

if __name__ == '__main__':
    # data = "2x3x4"
    # data = "1x1x10"
    # data = data.split('x')
    # data = [[int(i) for i in data]]
    # data.sort()
    data = read('input.txt')
    part_1(data)
    part_2(data)