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
            break

def part_2(data: str):
    utils.start_timer()
    for i in range(10**len(data)):
        result = hashlib.md5(f"{data}{str(i)}".encode())
        if result.hexdigest()[:6] == "0"*6:
            utils.pprint(2,i)
            break


if __name__ == "__main__":
    # data = "abcdef"
    # data = "pqrstuv"
    data = "yzbqklnj"
    part_1(data)
    part_2(data)