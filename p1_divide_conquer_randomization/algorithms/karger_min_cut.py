import copy
import datetime
import random
import time


def run_karger_trials(graph, trials):
    best = None

    for i in range(trials):
        graph_copy = copy.deepcopy(graph)
        crossing_edges = karger_min_cut(graph_copy)

        if best == None or crossing_edges < best:
            best = crossing_edges

    return best


def karger_min_cut(graph):
    """
    finds min cut of undirected graph with probability at least 1/(number of nodes)

    args:
        - graph represented as an adjacency list dictionary {vertex:[adjacent_vertices]}

    return:
        - int, with at least 1/n prob of being crossing edges of min cut
    """
    while len(graph.keys()) > 2:

        edges = [(node, adjacent)
                 for node in graph for adjacent in graph[node]]
        random_edge = random.choice(edges)

        n1 = random_edge[0]
        n2 = random_edge[1]

        contract_nodes(graph, n1, n2)

    for edges in graph.values():
        num_crossing_edges = len(edges)
        break

    return num_crossing_edges, edges


def contract_nodes(graph, n1, n2):
    """
    Contract nodes n1, n2, making n1 a supernode
    1) Combine connection lists
    2) Remove n2 from graph
    3) Redirect all references in graph to n2 to n1 (supernode)
    4) Remove self loops within n1 connections
    """

    # combine connection lists
    graph[n1].extend(graph[n2])

    # remove n2
    graph.pop(n2)

    # redirect all references to n2 to n1
    for vals in graph.values():
        for i in range(len(vals)):
            if vals[i] == n2:
                vals[i] = n1

    # remove self loops
    super_node_connections = [x for x in graph[n1] if x != n1]
    graph[n1] = super_node_connections


def get_graph_from_txt(filename):
    """
    Create graph represented as an adjacency list according to the file data
    """
    graph = {}

    with open(filename, 'r') as f:
        for line in f:
            vertex_data = line.split()
            vertex_label = vertex_data[0]
            connections = [vertex_data[x] for x in range(1, len(vertex_data))]
            graph[vertex_label] = connections

    return graph
