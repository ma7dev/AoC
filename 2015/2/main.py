import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
# part 1
# data = "2x3x4"
# data = data.split('x')
# data = [int(i) for i in data]
# data.sort()
utils.start_timer()
data = []
with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        tmp = [int(j) for j in row[0].split('x')]
        tmp.sort()
        data.append(tmp)
sum_ = 0
for example in data:
    sum_ += example[0]*example[1]
    sum_ += 2*example[0]*example[1]
    sum_ += 2*example[1]*example[2]
    sum_ += 2*example[0]*example[2]
utils.pprint(1,sum_)