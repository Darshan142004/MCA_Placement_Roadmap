if __name__ == '__main__':
    n = 6
    arr = (5,8,2,4,61,4);
    my_list = list(arr);
    
    if my_list[0] > my_list[1]:
        max1 = my_list[0]
        max2 = my_list[1]
    else:
        max1 = my_list[1]
        max2 = my_list[0]
        
    # --- Iteration Step (Loop through the rest of the list) ---
    # Start iterating from the 3rd element (index 2)
    for num in my_list[2:]:
        if num > max1:
            # New largest found
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            # New second largest found (and not the same as the top max)
            max2 = num    
            
    print(max2)