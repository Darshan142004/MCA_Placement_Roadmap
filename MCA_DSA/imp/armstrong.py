n = 153
temp = n
s = 0
while temp > 0:
    digit = temp % 10
    s += digit ** 3
    temp //= 10  
    
print("Armstrong" if s == n else "Not Armstrong")
