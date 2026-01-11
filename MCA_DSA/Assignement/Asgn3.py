def minimumAddedCoins(coins, target):
    coins.sort()
    reachable = 0
    added = 0
    i = 0

    while reachable < target:
        if i < len(coins) and coins[i] <= reachable + 1:
            reachable += coins[i]
            i += 1
        else:
            added += 1
            reachable += reachable + 1

    return added

print(minimumAddedCoins([1, 4, 10], 19))     

print(minimumAddedCoins([1, 4, 5, 7, 19], 19))

print(minimumAddedCoins([1, 1, 1], 20))       
