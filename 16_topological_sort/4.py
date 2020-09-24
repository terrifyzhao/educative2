from collections import deque


def print_orders(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return False

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
    graph = {i: [] for i in range(tasks)}  # adjacency list graph

    # b. Build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    print_all_topological_sorts(graph, inDegree, sources, sortedOrder)


def print_all_topological_sorts(graph, inDegree, sources, sortedOrder):
    if sources:
        for node in sources:
            sortedOrder.append(node)
            next_sources = deque(sources)
            next_sources.remove(node)
            for c in graph[node]:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    next_sources.append(c)

            print_all_topological_sorts(graph, inDegree, next_sources, sortedOrder)

            sortedOrder.remove(node)
            for c in graph[node]:
                inDegree[c] += 1

    # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between tasks, or
    # we have not processed all the tasks in this recursive call
    if len(sortedOrder) == len(inDegree):
        print(sortedOrder)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
