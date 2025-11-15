arr = [1, 3, 5, 2, 2]

total = sum(arr)
left = 0

for i in range(len(arr)):
    total -= arr[i]  # right side sum
    if left == total:
        print("Equilibrium index:", i)
        break
    left += arr[i]
