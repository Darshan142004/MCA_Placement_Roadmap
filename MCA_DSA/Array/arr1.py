arr=(10,30,20,40,50,40,70,90,49,99);
x=50;
found=False;
for i in arr:
    if(x==i):
        print("Element found");
        found=True;
        break;
if not found:
    print("Not present");