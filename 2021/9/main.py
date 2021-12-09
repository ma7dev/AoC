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
            data.append([int(i) for i in list(row.split()[0])])
    return data

def part_1_sol(data, verbose=False):
    valid_row = []
    num_rows = len(data)
    num_cols = len(data[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if j == 0:
                if data[i][j+1] > data[i][j]:
                    valid_row.append((i,j))
            elif j == num_cols-1:
                if data[i][j-1] > data[i][j]:
                    valid_row.append((i,j))
            else:
                if data[i][j-1] > data[i][j] and data[i][j+1] > data[i][j]:
                    valid_row.append((i,j))
    valid_col = []
    for j in range(num_cols):
        for i in range(num_rows):
            if i == 0:
                if data[i+1][j] > data[i][j]:
                    valid_col.append((i,j))
            elif i == num_rows-1:
                if data[i-1][j] > data[i][j]:
                    valid_col.append((i,j))
            else:
                if data[i-1][j] > data[i][j] and data[i+1][j] > data[i][j]:
                    valid_col.append((i,j))
    return list(set(valid_row) & set(valid_col))

def part_1(data, verbose=False):
    utils.start_timer()
    valid = part_1_sol(data, verbose=False)
    sum_ = 0
    for i,j in valid:
        sum_ += data[i][j]+1
    utils.pprint(1, sum_)
    return valid

def visited_before(i,j,visited):
    for visited_ in visited:
        if visited_[0] == i and visited_[1] == j:
            return True
    return False

def part_2(data,verbose=False):
    utils.start_timer()
    valid = part_1_sol(data, verbose=False)
    num_rows = len(data)
    num_cols = len(data[0])
    basin_sizes = []
    for i,j in valid:
        queue = []
        visited = []
        queue.append((i,j))
        visited.append((i,j))
        basic_size = 0
        while len(queue) > 0:
            i,j = queue.pop(0)
            basic_size += 1
            # right
            j_ = j+1
            while j_ < num_cols:
                if data[i][j_] != 9 and data[i][j_] > data[i][j_-1] and not visited_before(i,j_,visited):
                    queue.append((i,j_))
                    visited.append((i,j_))
                else:
                    break
                j_ += 1
            # left
            j_ = j-1
            while j_ > -1:
                if data[i][j_] != 9 and data[i][j_] > data[i][j_+1] and not visited_before(i,j_,visited):
                    queue.append((i,j_))
                    visited.append((i,j_))
                else:
                    break
                j_ -= 1
            # top
            i_ = i-1
            while i_ > -1:
                if data[i_][j] != 9 and data[i_][j] > data[i_+1][j] and not visited_before(i_,j,visited):
                    queue.append((i_,j))
                    visited.append((i_,j))
                else:
                    break
                i_ -= 1
            # bottom
            i_ = i+1
            while i_ < num_rows:
                if data[i_][j] != 9 and data[i_][j] > data[i_-1][j] and not visited_before(i_,j,visited):
                    queue.append((i_,j))
                    visited.append((i_,j))
                else:
                    break
                i_ += 1
        basin_sizes.append(basic_size)
    top_3 = sorted(basin_sizes,reverse=True)[:3]
    result = top_3[0]*top_3[1]*top_3[2]
    utils.pprint(2, result)

if __name__ == "__main__":
    print("Advent of Code 2021 - Day 8")
    print("-----------------------------")
    print("Example:")
    data = read('ex.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read('input.txt')
    part_1(copy.deepcopy(data))
    part_2(copy.deepcopy(data))