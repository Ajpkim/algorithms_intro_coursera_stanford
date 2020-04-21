# FAILING TEST CASES


def naive_dijkstra(g, s):
    """
    Computes single source shortest-paths for a directed graph with no negative edge weights 

    Args:
        - g, graph represented with lists of nodes and edges
        - s, source node to compute shortest paths from

    Returns:
        - Dictionary of shortest paths {node: shortest path weight}
    """

    X = [s]  # list of processed nodes
    A = {s: 0}  # dictionary of shortest path distances from source node s

    while len(X) < len(g):

        e = find_min_edge(g, A, X)  # get edge tuple
        source, destination, weight = e[0], e[1], e[2]

        X.append(destination)
        A[destination] = A[source] + weight

    return A


def find_min_edge(g, A, X):
    "Returns the min crossing edge between nodes in X and nodes not in X"

    min_edge = None

    for source in X:
        for edge in g[source]:
            destination, weight = edge[0], edge[1]

            if destination not in X:  # only care about crossing edges
                if min_edge == None or weight < min_edge[2]:
                    min_edge = [source, destination, weight]
    return min_edge


def load_graph_adjacency_list(filename):
    "Parses, and returns, a graph adjacency list represented as a dictionary"

    graph = {}

    with open(filename, 'r') as f:

        for line in f:

            data = line.replace('\n', '').replace('\t', ' ').rstrip()
            data = data.split(' ')

            source = data[0]
            edges = []
            graph[source] = [(edge.split(',')[0], int(edge.split(',')[1]))
                             for edge in data[1:]]  # convert weight to int

    return graph


# filename = 'graph_search_shortest_paths_data_structures\dijkstraData_adjacencyList.txt'
# filename = 'dijkstraData_adjacencyList.txt'
# g = load_graph_adjacency_list(filename)
# print(g)


def main():
    filename = 'dijkstraData_adjacencyList.txt'
    g = load_graph_adjacency_list(filename)
    shortest_paths = naive_dijkstra(g, '1')
    print(shortest_paths)


if __name__ == '__main__':
    main()
