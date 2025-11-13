arr=[20,23,25,98,57,43];

if arr[0]>arr[1]:
    first,sec=arr[0],arr[1];
else:
    first,sec=arr[1],arr[0];

for i in range(2,len(arr)):
    if arr[i]>first:
        sec=first;
        first=arr[i];
    elif arr[i]>sec and arr[i]!=first:
        sec=arr[i];
print(first)
print(sec);