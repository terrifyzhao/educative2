import math


def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    small_length = math.inf
    start = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        while window_sum >= s:
            small_length = min(small_length, i - start + 1)
            window_sum -= arr[start]
            start += 1

    return 0 if small_length == math.inf else small_length


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
