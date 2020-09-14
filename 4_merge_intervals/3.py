def merge(intervals_a, intervals_b):
    result = []
    i = 0
    j = 0

    while i < len(intervals_a) and j < len(intervals_b):
        a = intervals_a[i]
        b = intervals_b[j]
        if b[0] <= a[1] <= b[1] or a[0] <= b[1] <= a[1]:
            result.append([max(a[0], b[0]), min([a[1], b[1]])])
        if a[1] < b[1]:
            i += 1
        else:
            j += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
