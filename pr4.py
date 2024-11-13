# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.

def knapsack(weights, values, w, n):
    dp = [[0 for _ in range(W+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w-=weights[i-1]
    return dp[n][W], selected_items

weights = [2,3,4,5]
values = [1,2,5,6]
W=8
n=len(weights)

max_value, selected_items = knapsack(weights, values, W, n)
print("Maximum value in knapsack:", max_value)
print("Selected items (0-indexed):", selected_items)

'''
Output:

Maximum value in knapsack: 8
Selected items (0-indexed): [3, 1]
'''