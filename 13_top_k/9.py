from heapq import *


def find_maximum_distinct_elements(nums, k):
    min_heap = []
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    count = 0
    for key, v in dic.items():
        if v == 1:
            count += 1
        else:
            heappush(min_heap, [v, key])

    while min_heap and k > 0:
        tmp = heappop(min_heap)
        k = k - tmp[0] + 1
        if k >= 0:
            count += 1

    if k > 0:
        count -= k

    return count


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
