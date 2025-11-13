arr=[324,3,21,432,6,43];
if arr[0]>arr[1]:
    first,sec=arr[1],arr[0];
else:
    first,sec=arr[0],arr[1];

for i in range(2,len(arr)):
    if arr[i]<first:
        sec=first;
        first=arr[i];
    elif arr[i]<sec and arr[i]!=0:
        sec=arr[i];

print(first);
print(sec);