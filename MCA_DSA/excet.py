arr = [1, 2, 3, 4]
n = len(arr)

prefix = [1] * n
suffix = [1] * n
result = [1] * n


# prefix products
for i in range(1, n):
    prefix[i] = prefix[i-1] * arr[i-1]


# suffix products
for i in range(n-2, -1, -1):
    suffix[i] = suffix[i+1] * arr[i+1]

# multiply them
for i in range(n):
    result[i] = prefix[i] * suffix[i]

print(result)
