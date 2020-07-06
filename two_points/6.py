def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            num_sum = arr[i] + arr[left] + arr[right]
            if num_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
