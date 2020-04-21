from min_heap import MinHeap


def dijkstra(filename, s):
    # graph rep: {source: [(dest, weight)]})
    graph = load_graph_adjacency_list(filename)

    distances = {}
    h = MinHeap([(0, s)])  # need to initialize MinHeap with list of elements

    while h.heap:

        distance, node = h.extract_min()

        if node in distances:
            continue  # Already processed this node

        distances[node] = distance  # Process node

        for edge in graph[node]:  # Update all adjacent nodes
            adjacent_node = edge[0]
            potential_path_dist = edge[1] + distance
            # add to heap (nodes can be added multiple times, will only be processed once)
            h.insert((potential_path_dist, adjacent_node))

    return distances


def load_graph_adjacency_list(filename):
    "Parses, and returns, a graph adjacency list represented as a dictionary, {source: [(dest, weight)]}"

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


# filename = "dijkstraData_adjacencyList.txt"

# shortest_paths = dijkstra(filename, '1')
# print(shortest_paths)
