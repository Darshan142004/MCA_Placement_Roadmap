arr = [10, 20, 10, 30, 20, 10]
freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
for key, value in freq.items():
    print(f"{key}: {value}")
