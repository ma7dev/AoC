import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import hashlib

def part_1(data: str):
    utils.start_timer()
    for i in range(10**len(data)):
        result = hashlib.md5(f"{data}{str(i)}".encode())
        if result.hexdigest()[:5] == "0"*5:
            utils.pprint(1,i)
            return
    utils.pprint(2,"Not found")

def part_2(data: str):
    utils.start_timer()
    for i in range(10**len(data)):
        result = hashlib.md5(f"{data}{str(i)}".encode())
        if result.hexdigest()[:6] == "0"*6:
            utils.pprint(2,i)
            return
    utils.pprint(2,"Not found")


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 4")
    print("-----------------------------")
    print("Example 1:")
    data = "abcdef"
    part_1(data)
    part_2(data)
    print("Example 2:")
    data = "pqrstuv"
    part_1(data)
    part_2(data)
    print("-----------------------------")
    print("Test:")
    data = "yzbqklnj"
    part_1(data)
    part_2(data)