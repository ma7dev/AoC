import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
from typing import List, Tuple

def read(filename: str) -> Tuple[str, List[List[str]]]: 
    calls = []
    boards = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        board = []
        for i, row in enumerate(reader):
            if i == 0:
                calls = row
            elif row == []:
                if board != []:
                    boards.append(board)
                board = []
            else:
                board.append(row[0].split())
        if board != []:
            boards.append(board)
    return (calls, boards)

def solver(board: List[List[str]], call: str) -> List[List[str]]:
    for i,row in enumerate(board):
        for j, _ in enumerate(row):
            if call == row[j]:
                board[i][j] = "x"
    return board

def checker(board: List[List[str]]) -> bool:
    for row in board:
        if row.count("x") == len(row):
            return True
    for col in range(len(board[0])):
        if [row[col] for row in board].count("x") == len(board):
            return True
    return False

def summ(board: List[List[str]]) -> int:
    sum_ = 0
    for row in board:
        for col in row:
            if col == "x":
                continue
            sum_ += int(col)
    return sum_

def part_1(calls,boards,verbose=False):
    utils.start_timer()
    for call in calls:
        for board in boards:
            if board == None:
                continue
            board = solver(board,call)
            if checker(board):
                utils.pprint(1, summ(board)*int(call))
                return
        

def part_2(calls,boards,verbose=False):
    utils.start_timer()
    boards_status = [False]*len(boards)
    for call in calls:
        for i, board in enumerate(boards):
            if boards_status[i]:
                continue
            boards[i] = solver(boards[i],call)
            if checker(board):
                if sum(boards_status) == len(boards)-1:
                    utils.pprint(2, summ(board)*int(call))
                    return
                boards_status[i] = True

if __name__ == "__main__":
    print("Advent of Code 2021 - Day 4")
    print("-----------------------------")
    print("Example:")
    calls, boards = read('ex.txt')
    part_1(calls,boards)
    part_2(calls,boards)
    print("-----------------------------")
    print("Test:")
    calls, boards = read('input.txt')
    part_1(calls,boards)
    part_2(calls,boards)