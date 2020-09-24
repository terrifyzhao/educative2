from collections import deque


def find_order(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return False

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        in_degree[child] += 1
        graph[parent].append(child)

    queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            queue.append(key)

    while queue:
        node = queue.popleft()
        sortedOrder.append(node)
        for c in graph[node]:
            in_degree[c] -= 1
            if in_degree[c] == 0:
                queue.append(c)

    if len(sortedOrder) != tasks:
        return []
    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
