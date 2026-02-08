arr=[2,3,4,5,6,7,8,9,11,23,43,45,67,87,88]
arrE=[]
arrO=[]
for i in arr:
    if(i % 2 ==0):
        arrE.append(i)
    else:
        arrO.append(i)
print(arrE)

print(arrO)
    