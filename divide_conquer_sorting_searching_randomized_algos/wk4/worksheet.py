# from deterministic_selection import *
import random
from import *
import timeit
import time
start_time = time.perf_counter()

graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [1, 2, 3], 5: [1, 2]}


edges = get_edge_set(graph)
print(edges)


# for i in range(1000):
#     print(graph)
# print("")
# num_crossing_edges = karger_min_cut(graph)

end = time.perf_counter()
print("time:", end-start_time)
# print('result:', num_crossing_edges)
# print('')
# print('final graph', graph)


# wrong = 0
# right = 0
# for i in range(1000):
#     graph = {1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2, 4], 4: [1, 2, 3], 5: [1, 2]}
#     num_crossing_edges = karger_min_cut(graph)
#
#     if num_crossing_edges != 2:
#         wrong += 1
#     else:
#         right += 1
#
# print("right:", right)
# print("wrong", wrong)
# print("percent right:", right/wrong)


# print(graph.values())
# print(len(graph.values()))


# for edges in graph.values():
#     num_crossing_edges = len(edges)
#     break
# print(num_crossing_edges)


# print(len(graph.values()[0]))
# print(graph.items())
# print(len(graph.items()))
# wrong = 0
# for i in range(1000):
#     num_crossing_edges = karger_min_cut(graph)
#     if num_crossing_edges != :
#         wrong += 1
# print(wrong)


# print("graph:", graph)
# num_crossing_edges = karger_min_cut(graph)
# print(num_crossing_edges)

# troubleshooting self loops
# n1 = 1
# n2 = 2
# graph = contract_nodes(graph, n1, n2)
# print(graph)

# print(graph[1][0])

# for i in range(len(graph[1])):
# supernode_connections = []
# for connection in graph[n1]:
#     if connection != n1:
#         supernode_connections.append(connection)
# super_node_connections = [x for x in graph[n1] if x != n1]
# print(super_node_connections)
# graph = contract_nodes(graph, n1, n2)
# contract_nodes(graph, n1, n2)
# print(graph)


# n1 = 1
# n2 = 2
# print("graph:", graph)
# num_crossing_edges = karger_min_cut(graph)
# print(num_crossing_edges)

# edges = get_edge_set(graph)
# print(edges)
# print(a)
# print(graph)
# print("")
# contract_nodes(graph, n1, n2)
# print(graph)
# print("")
# print(len(graph.values()))
# print("")
# print(graph.values())
# print("")
# print(graph.items())
# val1 = graph.values()[0]
#
# for val in graph.values():
#     print(val)
# edges = get_edge_set(graph)
#
# print("As set:\n", edges)
# print("As tuple:\n", tuple(edges))
# print("")

# print(len(edges))


# graph = {'a': ['z', 'c'], 'b': ['x', 'y'], 'c': ['z', 'a']}
# print(a)
# print(a.items())
# print(a.values())
# for entry in a:
#     print(a[entry])

# random.seed()
#
# edges = set()
# for entry in graph:
#     src = entry
#     for i in range(len(graph[entry])):
#         dest = graph[entry][i]
#         edge = (min(src, dest), max(src, dest))
#         edges.add(edge)
# # print(edges)
# # random_edge = edges[random.randint(0, len(edges)-1)]
# # print(random_edge)
# print(edges)
# # random_edge = random.choice(tuple(edges))
# random_edge = random.choice(tuple(edges))
# print(random_edge)
# random_edge = edges.pop()
# second_edge = edges.pop()
# print(random_edge)
# print(second_edge)


# prtin

# sizes = [10, 11, 57, 101, 38, 58, 420]
#
#
# def test_DSelect(sizes):
#
#     for size in sizes:
#         a = []
#         for i in range(1, size + 1):
#             a.append(i)
#
#         random.shuffle(a)
#
#         for i in range(1, size + 1):
#             result = DSelect(a, i)
#             if result != i:
#                 print("ERROR")
#                 print("size: {}, i: {}, result: {}".format(size, i, result))
#                 return
#
#     print("Test complete. No errors found.")
#

# test_DSelect(sizes)


# ###### Testing randomized_selection ###
# x = 1
# print(randomized_selection(a, x, 0, len(a)))


# b = [6, 7, 8, 9, 10]
# c = randomized_selection(b, 5, 0, len(b))

#


# a = [2, 7, 3, 15, 4, 14, 8, 13, 9, 5, 16, 1, 6, 10, 11, 12]
# a = [1, 2, 3, 4, 5]
# for j in range(1, 16):
#     res = randomized_selection(a, j, 0, len(a))
#     if res != j:
#         print("ERROR")
#         print("j: {}, result: {}".format(j, res))
#         break

# print("done")

# for i in range(1, 16):
#     for j in range(0, 1000):
#         res = randomized_selection(a, i, 0, len(a))
#         if res != i:
#             print("ERROR... x={}, res={}".format(i, res))

#
# a = []
# for i in range(6, 11):
#     a.append(i)
# #
# #
# # # random.shuffle(a)
# # # print("shuffled a: ", a)
# #
# # # pivot = choose_pivot(a)
# # # print("pivot: ", pivot)
# #
# i = DSelect(a, 5)
# print("\n")
# print(i)

# sorted_a = merge_sort(a)
# print("sorted a: ", sorted_a)
#
# print("-----")
#
# #
# #
# print("")
# pivot = choose_pivot(a)
# print("pivot: ", pivot)

# # # print(52 % 5)
# #
# # # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # print(a[0:5])
# #
# a = []
# for i in range(0, 26):
#     a.append(i)
#
# print(a)
# print("")
#
# if len(a) % 5 == 0:
#     num_groups = len(a) // 5
#
# else:
#     num_groups = (len(a) // 5) + 1
#
# print("num_groups = ", num_groups)
#
# groups = [a[i*5: i*5 + 5] for i in range(0, num_groups)]
# print(groups)
#
# c = [x[(len(x)//2)] for x in groups]
#
# print(c)

# groups = []
# for group in range(0, num_groups):
#     group_start = group * 5
#     groups.append(a[group_start: group_start + 5])

# print(groups)
# print("")
# print(groups[0][5//2])

# a = [0, 1, 2, 3, 4]
#
# print(a[(5//2)])
