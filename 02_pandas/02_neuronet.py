import pandas as pd
import numpy as np

file_path_1 = input ()
file_path_2 = input ()
text_a , text_b= [], []
with open(file_path_1, "r") as file:
    for line in file:
        text_a.append(line.split())
with open(file_path_2, "r") as file:
    for line in file:
        text_b.append(line.split())
dframe_a = pd.DataFrame(text_a) 
print (dframe_a)
dframe_b = pd.DataFrame(text_a) 
print (dframe_b)
dframe_a2 = dframe_a*dframe_a
print (dframe_a2)
    