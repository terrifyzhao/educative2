def non_repeat_substring(str1):
    start = 0
    max_length = 0
    dic = {}

    for i in range(len(str1)):
        s = str1[i]
        if s in dic:
            start = max(start, dic[s] + 1)
            # start = dic[s] + 1
        dic[s] = i
        max_length = max(max_length, i - start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
    print("Length of the longest substring: " + str(non_repeat_substring("accbbc")))


main()
