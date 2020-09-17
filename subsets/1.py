def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        for i in range(len(subsets)):
            sub = list(subsets[i])
            sub.append(num)
            subsets.append(sub)
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
