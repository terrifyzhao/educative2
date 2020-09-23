from heapq import *


def find_k_frequent_numbers(nums, c):
    min_heap = []

    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for k, v in dic.items():
        heappush(min_heap, [v, k])
        if len(min_heap) > c:
            heappop(min_heap)

    res = []
    while min_heap:
        res.append(heappop(min_heap)[1])

    return res


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
