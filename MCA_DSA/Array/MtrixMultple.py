rows=int(input("Enter number of rows"))
matrix=[]

print("Enter each row");
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)

print("matrix=",matrix);