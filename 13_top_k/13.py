from heapq import *
from collections import deque


def schedule_tasks(tasks, k):
    intervalCount = 0

    dic = {}
    for task in tasks:
        dic[task] = dic.get(task, 0) + 1

    max_heap = []
    for key, value in dic.items():
        heappush(max_heap, [-value, key])

    while max_heap:
        tmp_list = []
        n = k + 1
        while n > 0 and max_heap:
            intervalCount += 1
            fre, key = heappop(max_heap)
            if -fre > 1:
                tmp_list.append([fre + 1, key])
            n -= 1

        for fre, key in tmp_list:
            heappush(max_heap, [fre, key])

        if max_heap:
            intervalCount += n

    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
