from collections import deque


def find_subarrays(arr, target):
    res = []
    start = 0
    num = 1
    for i in range(len(arr)):
        num *= arr[i]

        while num >= target and start < i:
            num /= arr[start]
            start += 1
        l = deque()
        for j in range(i, start - 1, -1):
            l.appendleft(arr[j])
            res.append(list(l))

    return res


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
