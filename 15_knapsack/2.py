def can_partition(num):
    s = sum(num)

    if s % 2 != 0:
        return False

    s = s // 2

    n = len(num)

    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(s + 1):
        if i == num[0]:
            dp[0][i] = True

    for i in range(n):
        for j in range(s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    return dp[-1][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
