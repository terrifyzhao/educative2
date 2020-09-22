def flip_and_invert_image(matrix):
    for row in matrix:
        l = len(row) - 1
        for i in range(len(row) // 2):
            row[i], row[l - i] = row[l - i], row[i]
        for i in range(len(row)):
            row[i] = row[i] ^ 1
    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
