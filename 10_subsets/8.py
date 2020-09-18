class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []
    return findUnique_trees_recursive(1, n)


def findUnique_trees_recursive(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left = findUnique_trees_recursive(start, i - 1)
        right = findUnique_trees_recursive(i + 1, end)

        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                result.append(root)

    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
