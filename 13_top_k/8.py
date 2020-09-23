from heapq import *


def find_closest_elements(arr, k, x):
    result = []
    if x > arr[-1]:
        return arr[-k:]
    if x < arr[0]:
        return arr[0:k]

    max_heap = []
    for n in arr:
        heappush(max_heap, [-abs(x - n), n])
        if len(max_heap) > k:
            heappop(max_heap)

    while max_heap:
        result.append(heappop(max_heap)[1])

    return result


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
