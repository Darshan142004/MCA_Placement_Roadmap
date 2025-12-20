arr = [4, 5, 2, 25]
n = len(arr)


stack = []
result = [-1] * n
for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)

print(result)
