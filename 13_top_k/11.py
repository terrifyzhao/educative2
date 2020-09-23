from heapq import *


def rearrange_string(str):
    max_heap = []
    dic = {}
    for s in str:
        dic[s] = dic.get(s, 0) + 1

    for key, value in dic.items():
        heappush(max_heap, [-value, key])

    res = []
    while max_heap:
        fre, v = heappop(max_heap)
        if res and res[-1] == v:
            return ''
        res.append(v)
        if -fre - 1 > 0:
            heappush(max_heap, [fre + 1, v])

    return "".join(res)


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
