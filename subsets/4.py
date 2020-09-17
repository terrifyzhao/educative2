def find_letter_case_string_permutations(str):
    permutation = []
    permutation.append(str)

    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutation)
            for j in range(n):
                tmp = list(permutation[j])
                tmp[i] = tmp[i].swapcase()
                permutation.append(''.join(tmp))

    return permutation


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
