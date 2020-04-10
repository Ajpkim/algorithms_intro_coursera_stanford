import sys
from kasaraju_2_pass_scc import *

sys.setrecursionlimit(10**6)
# print(sys.getrecursionlimit())
# filename = "kasaraju_test_cases/33300.txt"  # success
# filename = "kasaraju_test_cases/33200.txt"  # success
# filename = "kasaraju_test_cases/63210.txt"  # success
filename = "kasaraju_test_cases/31100.txt"  # success
# filename = "kasaraju_test_cases/32_10.txt"

# filename = "SCC_assignment_graph.txt"

# g = load_graph_dict(filename)
# print(g)
#
# g_rev = reverse_graph_dict(g)
# print(g_rev)

res = kasaraju_2_pass_SCC(filename)
print(res)


# a = [i for i in range(10)]
# print(a)
#
# a.reverse()
# print(a)

# leaders = {}
# leader = None
#
#
# def wrapper():
#     global leader
#     leader = 3
#     # global igloo
#     igloo = 10
#
#     add_to_leaders()
#
#
# def add_to_leaders():
#     global igloo
#     igloo = 44
#
#     global leader
#     global leaders
#     leaders[leader] = 339
#
#
# wrapper()
# print(leaders)
# print(igloo)


# a = [[111, 11, 122], [11, 111], [12, 122], [13, 133], [14, 444], [15, 555]]
# b = dict(enumerate(a))
# print(b)
#
#
# def reverse_graph_dict(graph):
#     "Reverses direction of directed graph, {tail:[adjacent heads]}"
#     g_rev = {}
#
#     # for i in graph.items()
#
#     for k in graph:
#         for v in graph[k]:
#             if v not in g_rev:
#                 g_rev[v] = [k]
#             else:
#                 g_rev[v].append(k)
#     return g_rev
#
#
# c = reverse_graph_dict(b)
# # print(c)
# # print(len(c))
# print(b)
#
# d = [b[x] for x in b]
# print(d)
