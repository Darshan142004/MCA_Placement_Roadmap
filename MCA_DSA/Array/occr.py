arr = [10, 20, 10, 30, 10, 40]
x = 10

first = arr.index(x)
last = len(arr) - 1 - arr[::-1].index(x)
print(f"First: {first}, Last: {last}")
