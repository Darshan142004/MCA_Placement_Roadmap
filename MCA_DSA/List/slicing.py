n=int(input())
li=input().split()

for i in range(n):
    li[i]=int(li[i])

print(li[::-1])