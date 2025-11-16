arr = [2, 3, 10, 6, 4, 8, 1]

min_so_far = arr[0]
max_diff = arr[1] - arr[0]

for i in range(1, len(arr)):
    max_diff = max(max_diff, arr[i] - min_so_far)
    min_so_far = min(min_so_far, arr[i])

print("Maximum difference:", max_diff)
