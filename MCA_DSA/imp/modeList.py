n=int(input())
li=input().split()

for i in range(n):
    li[i]=int(li[i])

maxC=0
maxE=li[0]

for i in li:
    count=0
    for j in li:
        if j==i:
            count+=1
    if maxC<count:
        maxC=count
        maxE=i
print("mode is",maxE,"count",maxC)
