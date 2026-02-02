n = 4

for i in range(1, n+1):
    left = "".join(str(x) for x in range(1, i))
    right = "".join(str(x) for x in range(i, 0, -1))
    print(" "*(n-i) + left + right)
