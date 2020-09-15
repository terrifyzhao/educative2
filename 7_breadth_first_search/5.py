class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from collections import deque


def find_minimum_depth(root):
    queue = deque()
    queue.append(root)
    depth = 0
    while queue:
        depth += 1
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return -1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
