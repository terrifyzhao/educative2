from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    max_heap = []
    min_heap = []

    for i in range(len(capital)):
        heappush(min_heap, [capital[i], i])

    available_capital = initialCapital
    for i in range(numberOfProjects):
        while min_heap and available_capital >= min_heap[0][0]:
            capital, i = heappop(min_heap)
            heappush(max_heap, -profits[i])

        if not max_heap:
            break
        available_capital += -heappop(max_heap)

    return available_capital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
