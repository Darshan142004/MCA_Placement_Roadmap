arr1=["darsh",2004,"Bhagwat"]
for i in arr1:
    print(i);
print(len(arr1));
print(arr1[2])
arr1[1]=14;
print(arr1[1]);
s=input("Enter 4th arr1ay element");
arr1.append(s);
print(arr1[3]);
arr2=arr1; # copy
for i in arr2:
    print(i);


#reverse
start=0;
end=len(arr1)-1;
while(start<end):
    arr1[start],arr1[end]=arr1[end],arr1[start];
    start+=1;
    end-=1;
    
for i in arr1:
    print(i);

arr3=(3,5,2,4,6,235,4);
summ=0;
for i in arr3:
    summ=summ+i;
    avgg=summ/(len(arr3));
print("sum is=",summ," AVG=",avgg);
print(max(arr3));
print(min(arr3));

