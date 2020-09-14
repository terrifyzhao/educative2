def pair_with_targetsum(arr, target_sum):
    i = 0
    j = len(arr) - 1

    while i < j:

        s = arr[i] + arr[j]
        if s == target_sum:
            return [i, j]
        elif s > target_sum:
            j -= 1
        else:
            i += 1

    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
