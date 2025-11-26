arr = [2, 2, 1, 1, 2]

candidate = count = 0

for n in arr:
    if count == 0:
        candidate = n
    count += (1 if n == candidate else -1)


# verify candidate
if arr.count(candidate) > len(arr)//2:
    print("Majority:", candidate)
else:
    print("No majority element")
