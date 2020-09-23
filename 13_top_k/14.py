from heapq import *


class FrequencyStack:

    def __init__(self):
        self.max_heap = []
        self.dic = {}

    def push(self, num):
        self.dic[num] = self.dic.get(num, 0) + 1
        heappush(self.max_heap, [-self.dic[num], num])

    def pop(self):

        return heappop(self.max_heap)[1]


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
