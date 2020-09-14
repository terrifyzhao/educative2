def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    small_res = 11110
    for i in range(len(arr) - 2):

        left = i + 1
        right = len(arr) - 1
        while left < right:
            res = arr[i] + arr[left] + arr[right] - target_sum

            if res == 0:
                return target_sum

            if abs(res) < abs(small_res):
                small_res = res

            if res > 0:
                right -= 1
            else:
                left += 1
    return target_sum + small_res


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
