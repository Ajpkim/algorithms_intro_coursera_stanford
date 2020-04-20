from dijkstra import dijkstra, load_graph_adjacency_list


# filename = "input_random_1_4.txt"
# filename = "input_random_2_4.txt"
# filename = "input_random_3_4.txt"
# filename = "input_random_28_256.txt"
# filename = "input_random_27_256.txt"
# filename = "input_random_15_32.txt"

filenames = ["test_cases/input_random_1_4.txt", "test_cases/input_random_2_4.txt", "test_cases/input_random_3_4.txt",
             "test_cases/input_random_28_256.txt", "test_cases/input_random_27_256.txt", "test_cases/input_random_15_32.txt"]
for filename in filenames:
    print('filename:', filename)
    g = load_graph_adjacency_list(filename)
    sp = dijkstra(g, '1')
    # print(sp)
    # break
    res = [sp['7'], sp['37'], sp['59'], sp['82'], sp['99'],
           sp['115'], sp['133'], sp['165'], sp['188'], sp['197']]
    print(res)
    print('')
    # 7,37,59,82,99,115,133,165,188,197
