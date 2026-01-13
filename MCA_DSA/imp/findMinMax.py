arr = [10, 20, 5, 8, 40, 3]
largest = smallest = arr[0]
for x in arr:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
        
print("Largest:", largest)
print("Smallest:", smallest)
