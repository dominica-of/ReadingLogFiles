import re
import datetime
from collections import defaultdict

transactions = defaultdict(dict)
with open(r"filename.log", 'r') as f:
    lines = f.readlines()
    trans = r'transaction\s(\d+)'
    time_r = r'\d+:\d+:\d+.\d+'
    for line in lines:
        a = re.search(trans, line)
        t = re.search(time_r, line)

        time_str = t.group(0) 
        time = datetime.datetime.strptime(time_str, '%H:%M:%S.%f')

        if a is not None:
        
            ID = a.group(1)
            if 'begin' in line:
                transactions[ID]['start'] = time
            if 'end' in line:
                transactions[ID]['end'] = time

            if 'end' in transactions[ID] and 'start' in transactions[ID]:
                delta_time = transactions[ID]['end'] - transactions[ID]['start']
                transactions[ID]['delta'] = delta_time.total_seconds() * 1000 


min_time = float('inf')
min_id = None
total_time = 0
delta_count = 0
for ID, data in transactions.items():
    if 'delta' in data: 
        total_time = data['delta']
        delta_count += 1

        if data['delta'] < min_time:
            min_time = data['delta']
            min_id = ID


print("Fastest transaction ID:", min_id)
print("Avg transaction time (ms):", total_time / delta_count)
