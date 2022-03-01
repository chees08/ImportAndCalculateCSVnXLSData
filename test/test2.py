
#pandas ile excel import etmek icin--- 

# import pandas as pd
# df = pd.read_excel (r'C:\Users\Burak\Downloads\test\Training.excel')
# print (df)

#csv import ---- 
import numpy as np
import csv
with open('Testing.csv', 'r') as f:
     data = list(csv.reader(f, delimiter=','))


matrix = np.array(data[1:])

x = matrix[0:4]
y = matrix[0:4]
A =np.array(x,dtype=float)
B =np.array(y,dtype=float)


print("[A] = \n", A)
print("\n")

print("[B] = \n", B)
print("\n")

print("[A+B]= \n", (A+B))
print("\n")

sum = (np.dot(A,B))
print("[A*B]= \n", sum)
