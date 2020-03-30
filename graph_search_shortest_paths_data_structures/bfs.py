import queue


def generic_bfs(graph, s):
    """
    Computes breadth first search of graph and returns list of all explored nodes.

    Args:
        - graph represented as dict {node[adjacent_nodes]}
        - s, node to initiate search from

    Returns:
        - list of explored nodes throughout search of graph
    """

    explored_nodes = [s]
    que = queue.Queue()

    que.put(s)

    while que.qsize() != 0:
        node = que.get()

        for adjacent in graph[node]:
            if adjacent not in explored_nodes:
                explored_nodes.append(adjacent)
                que.put(adjacent)

    return explored_nodes


graph = {'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['a', 'd'], 'd': ['c', 'b', 'f'],
         'e': ['i', 'g'], 'f': ['d', 'h'], 'g': ['e', 'i'], 'h': ['f'], 'i': ['e', 'g']}

res = generic_bfs(graph, 'a')
print(res)
