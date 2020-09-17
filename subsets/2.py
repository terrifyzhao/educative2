def find_subsets(nums):
    subsets = []
    subsets.append([])
    start, end = 0, 0
    n = len(nums)
    for i in range(n):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            sub = list(subsets[i])
            sub.append(nums[i])
            subsets.append(sub)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
