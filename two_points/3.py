def make_squares(arr):
    n = len(arr)

    res = [0 for _ in range(n)]

    i = 0
    j = n - 1
    index = n - 1
    while i <= j:
        left = arr[i] * arr[i]
        right = arr[j] * arr[j]

        if left < right:
            res[index] = right
            j -= 1
        else:
            res[index] = left
            i += 1
        index -= 1
    return res


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
