from heapq import *
import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def find_sliding_window_median(self, nums, k):
        result = []
        start = 0
        for i in range(len(nums)):
            if not self.maxHeap or -self.maxHeap[0] > nums[i]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance()

            if i + 1 >= k:
                if len(self.minHeap) == len(self.maxHeap):
                    result.append((self.minHeap[0] - self.maxHeap[0]) / 2)
                else:
                    result.append(-self.maxHeap[0])
                num = nums[start]
                start += 1
                if num <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -num)
                else:
                    self.remove(self.minHeap, num)

                self.rebalance()
        return result

    def rebalance(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def remove(self, heap, num):
        index = heap.index(num)

        heap[index] = heap[-1]
        del heap[-1]
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
