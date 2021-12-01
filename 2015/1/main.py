import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
data = None
with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        data = row[0]
# part 1
utils.start_timer()
counter = 0
for i in range(len(data)):
    if data[i] == '(':
        counter += 1
    else:
        counter -= 1
utils.pprint(1,counter)
# part 2
utils.start_timer()
counter = 0
target = -1
# data = "()())"
for i in range(len(data)):
    if data[i] == '(':
        counter += 1
    else:
        counter -= 1
        if counter == -1:
            target = i+1
            break
utils.pprint(2,target)