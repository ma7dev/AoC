import sys
sys.path.insert(0, "../../")
from helpers import utils
# --------------------------------------------------
import csv
data = []
with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        data.append(int(row[0]))
# part 1
utils.start_timer()
counter = 0
prev = data[0]
for i in range(1,len(data)):
    if data[i] > prev:
        counter += 1
    prev = data[i]
utils.pprint(1,counter)
# part 2
utils.start_timer()
counter = 0
for i in range(len(data)-3):
    if data[i+3] > data[i]:
        counter += 1
utils.pprint(2,counter)