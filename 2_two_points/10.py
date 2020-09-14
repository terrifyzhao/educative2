def next_valid_index(string, index):
    backspace_n = 0
    # # 要先记录#的个数，如果每次-2，遇到##的情况就凉了
    while index >= 0:
        if string[index] == '#':
            backspace_n += 1
        elif backspace_n > 0:
            backspace_n -= 1
        else:
            break
        index -= 1
    return index


def backspace_compare(str1, str2):
    i = len(str1) - 1
    j = len(str2) - 1

    while i >= 0 and j >= 0:
        next_i = next_valid_index(str1, i)
        next_j = next_valid_index(str2, j)

        if next_i < 0 and next_j < 0:
            return True
        if next_i < 0 or next_j < 0:
            return False
        if str1[next_i] != str2[next_j]:
            return False
        i = next_i - 1
        j = next_j - 1
    return True


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
