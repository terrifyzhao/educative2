from heapq import *


def sort_character_by_frequency(str):
    max_heap = []

    dic = {}
    for s in str:
        dic[s] = dic.get(s, 0) + 1

    for k, v in dic.items():
        heappush(max_heap, [-v, k])
    res = ''
    while max_heap:
        tmp = heappop(max_heap)
        k, v = tmp[1], -tmp[0]
        res = res + k * int(v)

    return res


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
