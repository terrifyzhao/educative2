def find_single_number(arr):
    res = arr[0]
    for num in arr[1:]:
        res = res ^ num
    return res


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()
