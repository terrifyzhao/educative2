from collections import deque


def find_order(words):
    in_degree = {}
    graph = {}
    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []

    for i in range(len(words) - 1):
        for j in range(min(len(words[i]), len(words[i + 1]))):
            w1, w2 = words[i][j], words[i + 1][j]
            if w1 != w2:
                in_degree[w2] += 1
                graph[w1].append(w2)
                break

    res = []
    queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            queue.append(key)

    while queue:
        node = queue.popleft()
        res.append(node)
        for c in graph[node]:
            in_degree[c] -= 1
            if in_degree[c] == 0:
                queue.append(c)

    return ''.join(res)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
