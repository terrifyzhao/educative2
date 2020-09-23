from heapq import *


def find_Kth_smallest(lists, k):
    min_heap = []
    for i in range(len(lists)):
        heappush(min_heap, [lists[i][0], 0, lists[i]])
    value = 0
    count = 0
    while min_heap and count < k:
        value, index, arr = heappop(min_heap)
        count += 1

        if len(arr) > index + 1:
            heappush(min_heap, [arr[index + 1], index + 1, arr])

    return value


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
