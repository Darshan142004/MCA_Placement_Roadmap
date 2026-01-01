s = "I am learning data structures in python"
max_len = 0
current = ""
longest = ""
for ch in s + " ":     
    if ch != " ":
        current += ch
    else:
        if len(current) > max_len:
            max_len = len(current)
            longest = current
        current = ""        
        
print("Longest word:", longest)
