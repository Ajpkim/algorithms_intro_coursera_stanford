"""
Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)
"""

filename = 'SCC_assignment_graph.txt'


def kasaraju_2_pass_SCC(filename):
    g = load_graph_dict(filename)
    g_rev = reverse_graph_dict(graph)

    finishing_times = []  # nodes ordered by ascending finishing time i.e. 0th node is lowest finishing time
    leaders = {}
    DFS_loop(g_rev)

    finishing_times = finishing_times.reverse()  # reverse list to put largest finishing times in front

    g_ordered = {}  # dicts are ordered in python 3.6+
    for node in finishing_times:
        g_ordered[node] = g[node]

    leaders = {}  # reset var
    DFS_loop(g_ordered)

    sccs = [leaders[scc] for scc in leaders]

    return sccs


def DFS_loop(graph):
    global t
    global leader
    global explored_nodes

    t = 0
    leader = None
    explored_nodes = []

    for node in graph:
        if node not in explored_nodes:
            leader = node
            DFS(graph, node)


def DFS(graph, node):
    global t
    global finishing_times
    global leader
    global leaders
    global explored_nodes

    explored_nodes.append(node)
    leaders[leader].append(node)

    for head in g_rev[node]:
        if head not in explored_nodes:
            DFS(graph, head)

        finishing_times.append(node)
        t += 1


def load_graph_dict(filename):
    "Represent a directed graph from file with dict, {tail: [adjacent head nodes]}"
    graph = {}

    with open(filename, 'r') as f:
        for line in f:
            edge = line.split(' ')
            tail, head = edge[0], edge[1]
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
