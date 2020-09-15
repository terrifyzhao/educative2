from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []

    queue = deque()
    queue.append(root)

    direction = True
    while queue:
        size = len(queue)
        cur = deque()
        for _ in range(size):
            node = queue.popleft()
            if direction:
                cur.append(node.val)
            else:
                cur.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        direction = not direction
        result.append(list(cur))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
