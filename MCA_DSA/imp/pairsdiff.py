arr = [1, 5, 3, 4, 2]
k = 2
seen = set(arr)

for x in arr:
    if x + k in seen:
        print(x, x + k)
