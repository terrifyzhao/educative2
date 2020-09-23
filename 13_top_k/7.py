from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = []
        for i in range(k):
            heappush(self.min_heap, nums[i])

        for num in nums[k:]:
            if num > self.min_heap[0]:
                heappop(self.min_heap)
                heappush(self.min_heap, num)

    def add(self, num):
        if num > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap, num)
        return self.min_heap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
