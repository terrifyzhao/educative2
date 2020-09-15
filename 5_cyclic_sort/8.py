def find_first_k_missing_positive(nums, k):
    missingNumbers = []

    n = len(nums)
    i = 0

    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    extra_num = []

    for i in range(n):
        if nums[i] != i + 1 and len(missingNumbers) < k:
            missingNumbers.append(i + 1)
            extra_num.append(nums[i])

    i = 1
    while len(missingNumbers) < k:
        tmp_num = n + i
        if tmp_num not in extra_num:
            missingNumbers.append(tmp_num)
        i += 1
    return missingNumbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
