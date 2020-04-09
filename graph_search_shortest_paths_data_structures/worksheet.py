
leaders = {}
leader = None


def wrapper():
    global leader
    leader = 3

    add_to_leaders()


def add_to_leaders():
    global leader
    global leaders
    leaders[leader] = 333


wrapper()
print(leaders)


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
