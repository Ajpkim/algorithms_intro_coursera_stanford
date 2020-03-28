from karger_min_cut import *
import random
import timeit
import time

# #timing block
# start = time.perf_counter()
# end = time.perf_counter()
# elapsed_time = end - start
# print("minutes:{}, second:{}".format(int(elapsed_time//60), round(elapsed_time % 60, 3)))


# graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [1, 2, 3], 5: [1, 2]}
# edges = get_edges(graph)
# random.choice(edges)
#
# print(timeit.timeit("""import random
# graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [1, 2, 3], 5: [1, 2]}
# edges = [(node, adjacent) for node in graph for adjacent in graph[node]]
# random.choice(edges)""", number=1000000))

# print(timeit.timeit("""import random
# graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [1, 2, 3], 5: [1, 2]}
# edges = [(node, adjacent) for node in graph for adjacent in graph[node]]
# random_edge = edges[random.randint(0, len(edges)-1)]""", number=1000000))


# print(graph)
# print(edges)
# contract_nodes(graph, 1, 5)
# edges = get_edges(graph)
# print(edges)
# print("")
# print(graph)
# contract_nodes(graph, 1, 2)
# edges = get_edges(graph)
# print(edges)
# print("")
# print(graph)
# edges = get_edge_set(graph)
# print(edges)
# print("")
#
# contract_nodes(graph, 1, 2)
# print(graph)
# edges = get_edge_set(graph)
# print(edges)

# CANT USE SET BC IT DISALLOWS PARALLEL EDGES
