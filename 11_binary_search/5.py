def find_range(arr, key):
    result = [- 1, -1]

    start, end = 0, len(arr)

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            low, high = mid, mid
            while arr[low] == key:
                low -= 1
            while arr[high] == key:
                high += 1
            return [low + 1, high - 1]
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return result


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
