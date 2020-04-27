import sys
import time

# kasaraju_2_pass_scc

# USE THREADS
# USE STACK FOR DFS?


def main(filename):
    SCCs = kasaraju_2_pass_SCC(filename)
    print("Number of nodes in each SCC:", SCCs)


def kasaraju_2_pass_SCC(filename):
    print('endering algo', flush=True)
    g = load_graph_dict(filename)
    g_rev = reverse_graph_dict(g)
    print('got the graphs', flush=True)

    global leaders
    global finishing_times
    # explored_nodes = []
    # nodes ordered by ascending finishing time i.e. 0th node is lowest finishing time
    finishing_times = []
    leaders = {}

    print('about to enter 1st loop', flush=True)
    DFS_loop(g_rev)

    # reverse list in-place to put largest finishing times in front
    finishing_times.reverse()

    g_ordered = {}  # dicts are ordered in python 3.6+
    # logic for ensuring that nodes without any outgoing edges are still correctly DFS'ed on
    for node in finishing_times:
        try:
            g_ordered[node] = g[node]
        except:
            g_ordered[node] = []

    leaders = {}  # reset var

    print('about to enter 2nd loop', flush=True)

    DFS_loop(g_ordered)

    sccs = [len(leaders[scc]) for scc in leaders]

    return sccs


def DFS_loop(graph):
    print('inside DFS LOOP', flush=True)
    global leaders
    global leader
    global explored_nodes
    global t
    t = 0
    leader = None
    explored_nodes = []

    global recursion_counter
    recursion_counter = 0

    for node in graph:
        if node not in explored_nodes:

            leader = node
            leaders[leader] = []

            DFS(graph, node)


def DFS(graph, node):
    global t
    global finishing_times
    global leader
    global leaders
    global explored_nodes

    global recursion_counter
    recursion_counter += 1
    print(f'DFS: {recursion_counter}', flush=True)

    explored_nodes.append(node)
    leaders[leader].append(node)

    # handle cases when node has no outgoing edges (g_rev cases)
    if node not in graph:
        finishing_times.append(node)
        return

    for head_node in graph[node]:
        if head_node not in explored_nodes:
            DFS(graph, head_node)
    finishing_times.append(node)
    t += 1


def load_graph_dict(filename):
    "Represent a directed graph from file with dict, {tail: [adjacent head nodes]}"
    graph = {}

    with open(filename, 'r') as f:
        for line in f:
            edge = line.split(' ')
            # convert to int for test cases
            tail, head = int(edge[0]), int(edge[1])
            if tail not in graph:
                graph[tail] = [head]
            else:
                graph[tail].append(head)
    return graph


def reverse_graph_dict(graph):
    "Reverses direction of directed graph, {tail:[adjacent heads]}"
    g_rev = {}
    for k in graph:
        for v in graph[k]:
            if v not in g_rev:
                g_rev[v] = [k]
            else:
                g_rev[v].append(k)
    return g_rev


# test cases:
# filename = "kasaraju_test_cases/33300.txt"  # success
# filename = "kasaraju_test_cases/33200.txt"  # success
# filename = "kasaraju_test_cases/63210.txt"  # success
# filename = "kasaraju_test_cases/31100.txt"  # success

# When I set the recursionlimit to a high number the call just passes out on the command line...

sys.setrecursionlimit(10**7)
filename = 'SCC_assignment_graph.txt'
# print(sys.getrecursionlimit())
if __name__ == '__main__':
    start = time.perf_counter()
    main(filename)
    end = time.perf_counter()
    print(end-start, 'seconds')
