import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
data = []
with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        data.append([row[0].split(' ')[0],int(row[0].split(' ')[1])])
# part 1
utils.start_timer()
horizontal = 0
depth = 0
for i in range(len(data)):
    if data[i][0] == 'forward':
        horizontal += data[i][1]
    elif data[i][0] == 'down':
        depth += data[i][1]
    elif data[i][0] == 'up':
        depth -= data[i][1]
utils.pprint(1,horizontal*depth)
# part 2
utils.start_timer()
horizontal = 0
depth = 0
aim = 0
for i in range(len(data)):
    if data[i][0] == 'forward':
        horizontal += data[i][1]
        depth += data[i][1]*aim
    elif data[i][0] == 'down':
        aim += data[i][1]
    elif data[i][0] == 'up':
        aim -= data[i][1]
utils.pprint(2,horizontal*depth)