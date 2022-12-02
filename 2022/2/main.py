import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import numpy as np
from typing import List
import copy
MAPPING_PART_1 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}
MAPPING_PART_2 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}
SCORE = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}
WINNER = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock",
}
ROUND_SCORE = {
    "lose": 0,
    "draw": 3,
    "win": 6
}
def read_part_1(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')  
        splitted_lines = [line.split(' ') for line in lines]
        data = [[MAPPING_PART_1[play] for play in plays] for plays in splitted_lines]   
    return data

def read_part_2(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')  
        splitted_lines = [line.split(' ') for line in lines]
        data = [[MAPPING_PART_2[play] for play in plays] for plays in splitted_lines]   
    return data

def part_1(data, verbose=False):
    utils.start_timer()
    total_score = 0
    for round in data:
        if round[0] == round[1]:
            total_score += ROUND_SCORE["draw"]
        elif WINNER[round[1]] == round[0]:
            total_score += ROUND_SCORE["win"]
        else:
            total_score += ROUND_SCORE["lose"]
        total_score += SCORE[round[1]]
    answer = total_score
    utils.pprint(1, answer)

def part_2(data,verbose=False):
    utils.start_timer()
    total_score = 0
    for round in data:
        end_results = round[1]
        total_score += ROUND_SCORE[end_results]
        if end_results == "draw":
            total_score += SCORE[round[0]]
        elif end_results == "win":
            possible_plays = ["Rock", "Paper", "Scissors"]
            possible_plays.remove(round[0])
            possible_plays.remove(WINNER[round[0]])
            total_score += SCORE[possible_plays[-1]]
        else:
            total_score += SCORE[WINNER[round[0]]]
    answer = total_score
    utils.pprint(2, answer)

if __name__ == "__main__":
    print("Advent of Code 2022 - Day 2")
    print("-----------------------------")
    print("Example 1:")
    data = read_part_1('ex_1.txt')
    part_1(copy.deepcopy(data))
    data = read_part_2('ex_1.txt')
    part_2(copy.deepcopy(data))
    print("-----------------------------")
    print("Test:")
    data = read_part_1('input.txt')
    part_1(copy.deepcopy(data))
    data = read_part_2('input.txt')
    part_2(copy.deepcopy(data))