# https://adventofcode.com/2020/day/3

import time
import re
import pandas as pd

start = time.time_ns()

input_file = pd.read_csv('inputs/input_3.txt', header=None)
# coordinates
x = 0
y = 2
print(str(input_file.iloc[y]))
howmany = 0

arr = []

def getTrees(df):
    global x, y, howmany, arr
    while y < 323:
        if x > 58:
            x = 0
        # get each row as a string and look for the value
        if str(input_file.iloc[y])[x] == '#':
            #df.iloc[y] = str(input_file.iloc[y])[x].replace('#', 'X')
            #df.iloc[y] = str(x)
            howmany += 1
            arr.append([x,y,input_file.iloc[y]])
        else:
            df.iloc[y] = input_file.iloc[y]
        x += 1
        y += 3
    return df


results = getTrees(input_file)

print(results.head(50), howmany, arr)

end = time.time_ns()
print((end-start)/10000)
