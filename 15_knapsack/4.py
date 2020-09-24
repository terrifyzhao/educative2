def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [False for _ in range(s // 2 + 1)]

    dp[0] = True

    for i in range(s // 2 + 1):
        dp[i] = num[0] == i

    for i in range(1, n):
        for j in range(s // 2, -1, -1):
            if not dp[j] and j >= num[i]:
                dp[j] = dp[j - num[i]]

    sum1 = 0
    for i in range(s // 2, -1, -1):
        if dp[i]:
            sum1 = i
            break

    sum2 = s - sum1

    return abs(sum1 - sum2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
