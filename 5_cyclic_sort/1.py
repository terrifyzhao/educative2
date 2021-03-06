def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        index = nums[i] - 1
        if nums[index] != nums[i]:
            nums[index], nums[i] = nums[i], nums[index]
        else:
            i += 1

    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
