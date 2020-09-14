def fruits_into_baskets(fruits):
    start = 0
    max_length = 0
    dic = {}

    for i in range(len(fruits)):
        f = fruits[i]
        dic[f] = dic.get(f, 0) + 1

        while len(dic) > 2:
            f = fruits[start]
            dic[f] -= 1
            if dic[f] == 0:
                del dic[f]
            start += 1
        max_length = max(max_length, i - start + 1)

    return max_length


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
