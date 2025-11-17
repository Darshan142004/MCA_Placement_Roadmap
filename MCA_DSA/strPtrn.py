n=int(input()) #5
for i in range(n): #i=1 ,n=5
    for m in range(n):# m=0 ,
        if(i<n-(m+1)):#1<5-1
           print(" ",end=" ")
        else:
           print("#",end=" ")
    print("")
   