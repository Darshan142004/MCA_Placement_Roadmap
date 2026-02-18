arr = [5, 2, 9, 1, 7]
n = len(arr)

for i in range(n-1):         # Total passes
    for j in range(n-1-i):   # Compare adjacent
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
print("Bubble Sorted:", arr)
