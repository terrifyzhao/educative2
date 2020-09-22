def find_single_numbers(nums):
    n = 0
    for num in nums:
        n = n ^ num

    bit = 1
    while bit & n == 0:
        bit = bit << 1
    num1, num2 = 0, 0

    for num in nums:
        if num & bit == 0:
            num1 = num1 ^ num
        else:
            num2 = num2 ^ num
    return [num1, num2]


def main():
    # print('Single numbers are:' +
    #       str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 3])))
    # print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
