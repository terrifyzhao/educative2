from collections import deque


def find_permutations(nums):
    result = []

    permutation = deque()
    permutation.append([])

    for num in nums:
        n = len(permutation)

        for _ in range(n):
            old_permutation = permutation.popleft()
            for i in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(i, num)

                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    permutation.append(new_permutation)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
