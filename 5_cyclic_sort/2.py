def find_missing_number(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if j < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return -1


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
