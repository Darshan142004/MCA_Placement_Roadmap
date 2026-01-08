# rows=int(input("Enter number of rows"))
# matrix=[]

# print("Enter each row");
# for i in range(rows):
#     row=list(map(int,input().split()))
#     matrix.append(row)

# print("matrix=",matrix);

import numpy as np


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = np.array(A) @ np.array(B)
print(result)