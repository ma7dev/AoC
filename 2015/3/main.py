import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
# data = ">"
# data = "^>v<"
# data = "^v^v^v^v^v"
# data = "^v"
data = None
with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        data = row[0]
data = list(data)
# part 1
utils.start_timer()
coords = {(0,0)}
curr = (0,0)
counter = 1
for i in data:
    curr = list(curr)
    if i == '^':
        curr[1] += 1
    elif i == 'v':
        curr[1] -= 1
    elif i == '<':
        curr[0] -= 1
    elif i == '>':
        curr[0] += 1
    curr = tuple(curr)
    coords.add(curr)
utils.pprint(1,len(coords))
# part 2
utils.start_timer()
coords = {(0,0)}
curr_santa = (0,0)
curr_robot = (0,0)
curr = None
counter = 1
for i, _ in enumerate(data):
    if i % 2 == 0:
        curr = list(curr_santa)
    else:
        curr = list(curr_robot)
    if data[i] == '^':
        curr[1] += 1
    elif data[i] == 'v':
        curr[1] -= 1
    elif data[i] == '<':
        curr[0] -= 1
    elif data[i] == '>':
        curr[0] += 1
    curr = tuple(curr)
    coords.add(curr)
    if i % 2 == 0:
        curr_santa = curr
    else:
        curr_robot = curr
utils.pprint(2,len(coords))