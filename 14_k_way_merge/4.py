from heapq import *


def find_smallest_range(lists):
    min_heap = []
    start, end = 0, 1000
    max_value = 0
    for arr in lists:
        heappush(min_heap, [arr[0], 0, arr])
        max_value = max(max_value, arr[0])

    while len(min_heap) == len(lists):
        value, index, arr = heappop(min_heap)
        if end - start > max_value - value:
            end = max_value
            start = value
        if len(arr) > index + 1:
            heappush(min_heap, [arr[index + 1], index + 1, arr])
            max_value = max(max_value, arr[index + 1])

    return [start, end]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
"""
Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
"""
