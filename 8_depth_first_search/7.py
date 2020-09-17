import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxPath:

    def __init__(self):
        pass

    def find_maximum_path_sum(self, root):
        self.max_sum = -1000
        self.find(root)
        return self.max_sum

    def find(self, root):
        if root is None:
            return 0

        left_sum = self.find(root.left)
        right_sum = self.find(root.right)

        left_sum = max(left_sum, 0)
        right_sum = max(right_sum, 0)

        cur_sum = left_sum + right_sum + root.val
        self.max_sum = max(self.max_sum, cur_sum)

        return max(left_sum, right_sum) + root.val


def main():
    max_path = MaxPath()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(max_path.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(max_path.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(max_path.find_maximum_path_sum(root)))


main()
