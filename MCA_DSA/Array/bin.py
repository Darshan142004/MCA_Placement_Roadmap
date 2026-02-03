arr=(10,20,30,40,50,60,70,80,90,100,110,115,120,125,130);
x=90;
low=0;
high=len(arr)-1;
found=False;


while(low<=high):
    mid=(low+high)//2;
    if arr[mid]==x:
        print("Element found");
        found=True;
        break;
    elif arr[mid]<x:
        low+=1;
    else:
        high-=1;

if not found:
    print("Not presents")