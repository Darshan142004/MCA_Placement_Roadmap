arr = [1, 4, 5, 3, 2]
target = 6

seen = set()
for num in arr:
    diff = target - num
    if diff in seen:
        print(num, diff)
    seen.add(num)
