# TODO:
import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
import copy
import hashlib
from typing import List
def read(filename: str) -> List[str]: 
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for _, row in enumerate(reader):
            data.append(row[0])
    return data
# 1. at least three vowels
# 2. at least one letter that appears twice in a row
# 3. doesn't contain ab, cd, pq, or xy
def part_1(data,verbose=False):
    utils.start_timer()
    vowels = "aeiou"
    bad = ["ab", "cd", "pq", "xy"]
    def check(word,verbose):
        vowel_count = 0
        prev = word[0]
        if prev in vowels:
            vowel_count += 1
        nice = [False,False]
        statement = []
        for char in word[1:]:
            if char in vowels:
                vowel_count += 1
                if vowel_count == 3:
                    statement.append("at least 3 vowels")
                    nice[0] = True
            if char == prev:
                statement.append(f"a double letter - {prev}{char}")
                nice[1] = True
            elif f"{prev}{char}" in bad:
                if verbose:
                    utils.pprint(1, f"False: {prev}{char}")
                return False
            prev = char
        if all(nice):
            if verbose:
                utils.pprint(1, f"True: {', '.join(statement)}")
            return True
        else:
            if verbose:
                utils.pprint(1,f"False: not nice")
            return False
    counter = 0
    for word in data:
        word = list(word)
        if check(word,verbose):
            counter += 1
    utils.pprint(1, counter)
        

def part_2(data,verbose=False):
    utils.start_timer()
    vowels = "aeiou"
    bad = ["ab", "cd", "pq", "xy"]
    def check(word,verbose):
        vowel_count = 0
        prev = word[0]
        if prev in vowels:
            vowel_count += 1
        nice = [False,False]
        statement = []
        for char in word[1:]:
            if char in vowels:
                vowel_count += 1
                if vowel_count == 3:
                    statement.append("at least 3 vowels")
                    nice[0] = True
            if char == prev:
                statement.append(f"a double letter - {prev}{char}")
                nice[1] = True
            elif f"{prev}{char}" in bad:
                if verbose:
                    utils.pprint(1, f"False: {prev}{char}")
                return False
            prev = char
        if all(nice):
            if verbose:
                utils.pprint(1, f"True: {', '.join(statement)}")
            return True
        else:
            if verbose:
                utils.pprint(1,f"False: not nice")
            return False
    counter = 0
    for word in data:
        word = list(word)
        if check(word,verbose):
            counter += 1
    utils.pprint(1, counter)


data = read('input.txt')
# data = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu","dvszwmarrgswjxmb"]
part_1(data)
# part_2(data)