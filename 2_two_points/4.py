def search_triplets(arr):
    res = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search(i + 1, arr, -arr[i], res)
    return res


def search(left, arr, num, res):
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == num:
            res.append([-num, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left - 1] == arr[left]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif arr[left] + arr[right] < num:
            left += 1
        else:
            right -= 1


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
