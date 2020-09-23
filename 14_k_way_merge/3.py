from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1

    min_heap = []
    for row in matrix:
        heappush(min_heap, [row[0], 0, row])

    count = 0
    while min_heap and count < k:
        number, index, row = heappop(min_heap)
        count += 1
        if len(row) > index + 1:
            heappush(min_heap, [row[index + 1], index + 1, row])

    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
