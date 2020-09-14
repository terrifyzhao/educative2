def search_quadruplets(arr, target):
    arr.sort()
    length = len(arr)
    res = []
    for i in range(length - 3):
        for j in range(i + 1, length - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            num = target - arr[i] - arr[j]
            left = j + 1
            right = length - 1
            while left < right:
                if arr[left] + arr[right] == num:
                    res.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif arr[left] + arr[right] < num:
                    left += 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

    return res


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
