from collections import deque


def is_scheduling_possible(tasks, prerequisites):
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

    return len(sortedOrder) == tasks


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
