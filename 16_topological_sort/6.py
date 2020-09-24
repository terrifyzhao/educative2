from collections import deque


def can_construct(originalSeq, sequences):
    res = []
    n = len(originalSeq)
    in_degree = {}
    graph = {}
    for sequence in sequences:
        for num in sequence:
            in_degree[num] = 0
            graph[num] = []

    for edge in sequences:
        for i in range(len(edge) - 1):
            parent, child = edge[i], edge[i + 1]
            in_degree[child] += 1
            graph[parent].append(child)

    if len(in_degree) != n:
        return False

    queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            queue.append(key)

    while len(queue) == 1:
        if originalSeq[len(res)] != queue[0]:
            return False
        node = queue.popleft()
        res.append(node)
        for c in graph[node]:
            in_degree[c] -= 1
            if in_degree[c] == 0:
                queue.append(c)

    return not len(queue) > 0


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
