arr=[34,45,56,67,87,7665,54,34,34,45,34,54];
lis=[];
for i in arr:
    if i not in lis:
        lis.append(i);

print(lis);