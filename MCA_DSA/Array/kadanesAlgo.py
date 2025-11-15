arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
current = arr[0]

for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    max_sum = max(max_sum, current)

print("Maximum subarray sum:", max_sum)
