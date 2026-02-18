arr=[0,564,34,56,78,0,9,0,9,8];
res=[x for x in arr if x!=0];

lis=[0]*arr.count(0);
res=res+lis;

print(res);