class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_path(root, S, path):
    if root is None:
        return 0
    path.append(root.val)
    count = 0
    cur_sum = 0

    for i in range(len(path) - 1, -1, -1):
        cur_sum += path[i]
        if cur_sum == S:
            count += 1

    count += count_path(root.left, S, path)
    count += count_path(root.right, S, path)

    del path[-1]

    return count


def count_paths(root, S):
    return count_path(root, S, [])


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
