
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


while True: 
    choice = input("Choice (add, mul): ")

    if choice in ('add', 'mul'):
        x = np.array(matrix[0:4],dtype=float)
        y = np.array(matrix[0:4],dtype=float)


        if choice == 'add':
            print("[A+B]= \n", (x+y))
        elif choice == 'mul':
            sum = (np.dot(x,y))
            print("[A*B]= \n", sum)

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
      break
    
    else:
      print("GO")