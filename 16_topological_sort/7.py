from collections import deque


def find_trees(nodes, edges):
    in_degree = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    for edge in edges:
        node1, node2 = edge[0], edge[1]
        in_degree[node1] += 1
        in_degree[node2] += 1
        graph[node1].append(node2)
        graph[node2].append(node1)

    queue = deque()
    for key in in_degree:
        if in_degree[key] == 1:
            queue.append(key)

    count = nodes
    while count > 2:
        leaves_len = len(queue)
        count -= leaves_len
        for i in range(leaves_len):
            node = queue.popleft()
            # in_degree[node] -= 1
            for c in graph[node]:
                in_degree[c] -= 1
                if in_degree[c] == 1:
                    queue.append(c)

    return queue


def main():
    print("Roots of MHTs: " +
          str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()
