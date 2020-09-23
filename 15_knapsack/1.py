from __future__ import print_function


def solve_knapsack1(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(2)]

    for i in range(2):
        dp[i][0] = 0

    for i in range(capacity + 1):
        if weights[0] <= i:
            dp[0][i] = profits[0]

    for i in range(1, n):
        for j in range(1, capacity + 1):
            profile1, profile2 = 0, 0
            profile1 = dp[(i - 1) % 2][j]
            if weights[i] <= j:
                profile2 = dp[(i - 1) % 2][j - weights[i]] + profits[i]
            dp[i % 2][j] = max(profile1, profile2)

    return dp[-1][-1]


def solve_knapsack2(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(capacity + 1):
        if weights[0] <= i:
            dp[0][i] = profits[0]

    for i in range(1, n):
        for j in range(1, capacity + 1):
            profile1, profile2 = 0, 0
            profile1 = dp[i - 1][j]
            if weights[i] <= j:
                profile2 = dp[i - 1][j - weights[i]] + profits[i]
            dp[i][j] = max(profile1, profile2)

    return dp[-1][-1]


def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    dp = [0 for _ in range(capacity + 1)]

    for i in range(capacity + 1):
        if weights[0] <= i:
            dp[i] = profits[0]

    for i in range(1, n):
        for j in range(capacity, -1, -1):
            profile1, profile2 = 0, 0
            profile1 = dp[j]
            if weights[i] <= j:
                profile2 = dp[j - weights[i]] + profits[i]
            dp[j] = max(profile1, profile2)

    return dp[-1]


def main():
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main()
