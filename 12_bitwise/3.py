def calculate_bitwise_complement(n):
    tmp = n
    count = 0
    while tmp:
        tmp = tmp >> 1
        count += 1

    return n ^ pow(2, count) - 1


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
