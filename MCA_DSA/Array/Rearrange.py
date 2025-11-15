arr = [1, -2, 3, -4, 5, -6]
pos = []
neg = []

for n in arr:
    if n >= 0:
        pos.append(n)
    else:
        neg.append(n)

result = []
i = j = 0

while i < len(pos) and j < len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i += 1
    j += 1

result += pos[i:]
result += neg[j:]

print(result)
