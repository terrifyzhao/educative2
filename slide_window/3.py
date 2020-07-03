def longest_substring_with_k_distinct(str1, k):
    str_dic = {}
    start = 0
    max_length = 0

    for i in range(len(str1)):
        s = str1[i]
        str_dic[s] = str_dic.get(s, 0) + 1
        while len(str_dic) > k:
            s = str1[start]
            str_dic[s] -= 1
            if str_dic[s] == 0:
                del str_dic[s]
            start += 1
        max_length = max(max_length, i - start + 1)
    return max_length


def main():
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
