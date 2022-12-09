def make_change(amount, coins):
    # Initialize an empty list to store the change.
    change = []

    # Sort the coins in descending order.
    coins = sorted(coins, reverse=True)

    # Iterate through the coins in descending order.
    for coin in coins:
        # If the coin is less than or equal to the remaining amount,
        # add it to the change and subtract it from the remaining amount.
        if coin <= amount:
            change.append(coin)
            amount -= coin

    # Return the change.
    return change

# Test the greedy algorithm on a sample amount and set of coins.
amount = 63
coins = [1, 5, 10, 25]
print(make_change(amount, coins))  # should print [25, 25, 10, 1, 1, 1]
