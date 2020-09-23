from heapq import *

from collections import deque


def reorganize_string(str, k):
    max_heap = []

    dic = {}
    for s in str:
        dic[s] = dic.get(s, 0) + 1

    for key, value in dic.items():
        heappush(max_heap, [-value, key])

    res = []
    queue = deque()
    while max_heap:
        fre, v = heappop(max_heap)
        res.append(v)
        queue.append((v, fre + 1))
        if len(queue) == k:
            v, fre = queue.popleft()
            if -fre > 0:
                heappush(max_heap, [fre, v])

    return ''.join(res) if len(res) == len(str) else ''


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
