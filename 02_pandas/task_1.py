import pandas as pd
import numpy as np
import re 

n, m = input().split()
n, m = int (n), int (m)
data = []
for i in range (n):
    a = input()
    pattern = '[0-9\-]{1,}'
    a =re.findall(pattern, a)
    a = [int(item) for item in a]
    data.append (a)
dframe = pd.DataFrame(data) 
print (sum ((dframe[dframe < -5].count(axis=0))))
print (int (abs (sum(np.sum(dframe[dframe < 0])))))
print (max(dframe.max(axis=0)))
#4 6
#  1  4  4  2  1  1
#  0  0  1  0 -1 -1
# -2 -3 -1 -5 -6 -4
# -1 -3 -3 -4 -4 -2
# 1
# 40
# 4

# 10 5
# -5 -2 -10 7 -9
# 5 -2 -6 6 9
# 5 -8 4 9 0
# 0 9 -6 2 -1
# -2 -8 7 3 0
# 9 7 -9 8 3
# 4 -9 2 -2 -3
# 8 8 -8 0 -9
# -1 -4 -6 9 -2
# -4 -6 -6 -1 -10