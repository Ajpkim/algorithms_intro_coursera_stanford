from karger_min_cut import *
import time

# n = 200
# to achieve (1- 1/n) success rate need to run n^2 ln(200)
# -----> 27725 trials


def test_karger(filename, trials):
    graph = get_graph_from_txt(filename)
    start = time.perf_counter()

    best, edges = run_karger_trials(graph, trials)

    end = time.perf_counter()
    elapsed_time = (end - start)

    print("trials:", trials)
    print("best:", best)
    # print('edges:', edges)
    print("minutes:{}, second:{}".format(int(elapsed_time//60), round(elapsed_time % 60, 3)))


test_karger('assignment_graph.txt', 100)

# ran on 6/28 at 6:03pm
# $ python karger_testing.py
# trials: 100
# best: 17
# minutes:0, second:13.396


# ran test at 5:24...
# $ python karger_testing.py
# trials: 10000
# best: 20
# minutes:113, second:44.162
