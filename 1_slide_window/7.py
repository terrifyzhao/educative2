def length_of_longest_substring(arr, k):
    start = 0
    max_len = 0
    count_1 = 0

    for i in range(len(arr)):
        num = arr[i]
        if num == 1:
            count_1 += 1
        if i - start + 1 - count_1 > k:
            num = arr[start]
            if num == 1:
                count_1 -= 1
            start += 1
        max_len = max(i - start + 1, max_len)
    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
