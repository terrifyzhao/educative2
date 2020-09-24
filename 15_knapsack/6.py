def find_target_subsets(num, s):
    s = (s + sum(num)) // 2
    n = len(num)

    dp = [[0 for _ in range(s + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for j in range(s + 1):
        if j == num[0]:
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num[i]:
                dp[i][j] += dp[i - 1][j - num[i]]

    return dp[-1][-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
