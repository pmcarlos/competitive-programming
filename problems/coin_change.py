def rec_coin(target, coins, knownResults):
    min_coins = target
    print(target)
    if target in coins:
        knownResults[target] = 1
        return 1
    elif knownResults[target] > 0:
        return knownResults[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target - i, coins, knownResults)
        if num_coins < min_coins:
            min_coins = num_coins
            knownResults[target] = min_coins
    return min_coins


target = 15
coins = [1, 5, 10, 25]
known_results = [0] * (target + 1)

print(rec_coin(target, coins, known_results))

