from find_closest_pair import *
from closest_pair_helpers import *
from random import randint


# Px:  [(6, 20), (6, 10), (13, 11), (25, 22)]
# Py:  [(6, 10), (13, 11), (6, 20), (25, 22)]

# Returns WRONG result
# P1 = [(4, 20), (4, 8), (12, 24), (17, 5)]
# Px = [(4, 20), (4, 8), (12, 24), (17, 5)]
# Py = [(17, 5), (4, 8), (4, 20), (12, 24)]

# print("Px: ", Px)
#
# res = closest_pair(Px, Py)
# print("--------------")
# print("")
# print("res: ", res)
# print("brute: ", closest_pair_brute_force(Px))

# P1 = [(3, 6), (2, 9), (3, 2), (8, 2), (4, 10), (8, 9), (4, 2), (10, 10), (0, 5)]
# Px = dimensional_merge_sort(P1, 0)
# Py = dimensional_merge_sort(P1, 1)
#
# print("RESULT: ", closest_pair(Px, Py))
# brute_res = closest_pair_brute_force(Px)
# print("Brute force result: ", brute_res)
# print("wrapper function res: ", find_closest_pair(P1))

# print(5-2.9)
# a = range
# P1 = [(3, 6), (2, 9), (3, 2), (8, 2), (4, 10), (8, 9), (4, 2), (10, 10), (0, 5)]
# # Py = [(4, 2), (3, 2), (8, 9), (10, 10), (0, 5)]
#
# P1 = [(3, 6), (3, 5), (2, 9), (3, 2), (8, 2), (4, 10), (8, 9), (4, 2), (10, 10), (0, 5)]
# Px = dimensional_merge_sort(P1, 0)
# Py = dimensional_merge_sort(P1, 1)
# print(closest_pair(Px, Py))

#
# half_Px = Px[:int(len(Px)/2)]
# next_Px = Px[int(len(Px)/2):]
#
# print(half_Px)
# print(next_Px)

# testY = Py[:int(len(Py)/2)]
# testY2 = Py[int(len(Py)/2):]
# print(testY)
# print(testY2)

# Qy = [y for y in Py if y in Px]
# print(Qy)


# Px = dimensional_merge_sort(Px, 0)
# Py = dimensional_merge_sort(Px, 1)
# print(Px)
# print("num elements in Px :", len(Px))
# mid_point = Px[int(len(Px)/2)][0]
# beginningX = Px[:int(len(Px)/2)]
#
# print("mid_point: ", mid_point)
# print("beginningX: ", beginningX)
#
# beginningY = [y for y in Py if y[0] < mid_point]
# print("beginningY: ", beginningY)

# x_bar = Px[int(len(Px)/2) - 1]
# print(int(len(Px)/2))
# print(x_bar)
#
# x_bar = Px[int(len(Px)/2)]
# print(x_bar)

# Px = [(3, 6), (2, 9), (3, 2), (8, 2), (4, 10), (8, 9)]
# d = 1.5
# mid_point = (Px[-1][0]/2)
# begin = (mid_point - d)
# end = (mid_point + d)
# print(mid_point, begin, end)
#
# compX = [x for x in Px if begin < float(x[0]) < end]
# print(compX)
# compY = [y for y in Py if begin < float(x[0])]

#
# a = Px[0]
# print(type(a))
# print(type(a[0]))
# print(type(float(a[0])))
# #
# Testing closest_pair() -----------------------
# Pretty sure I'm not getting it bc the answer is a SPLIT PAIR

# answer is a SPLIT PAIR
# p1 = [(3, 6), (2, 9), (3, 2), (8, 2), (4, 10), (8, 9)]
# answer NOT a split
#
# p1 = [(3, 6), (2, 9), (3, 2), (8, 2), (4, 10), (8, 9), (2, 8)]
#
# Px, Py = dimensional_merge_sort(p1, 0), dimensional_merge_sort(p1, 1)
# print("Px: ", Px)
# print("Py: ", Py)
# mid_point = int(Px[-1][0]/2)
# print("mid_point: ", mid_point)
# Qx = [x for x in Px if x[0] <= mid_point]
# Qy = [y for y in Py if y[0] <= mid_point]
#
# Rx = [x for x in Px if x[0] > mid_point]
# Ry = [y for y in Py if y[0] > mid_point]
#
# print("------------------------------")
#
# print("Qx: ", Qx)
# print("Qy: ", Qy)
#
# print("------------------------------")
#
# Q1, Q2 = closest_pair(Qx, Qy)
# print("closest pair res: ", Q1, Q2)
# closest_pair_dist = round(calc_euclidean_dist(Q1, Q2), 3)
# print("distance: ", closest_pair_dist)
#
# print("------------------------------")
#
# BruteQ1, BruteQ2 = brute_force(Qx, Qy)
# print("brute force res: ", BruteQ1, BruteQ2)
# brute_distance = round(calc_euclidean_dist(BruteQ1, BruteQ2), 3)
# print("distance: ", brute_distance)
#
# print("-----------------------------")
# print("test: ", (Q1, Q2) == (BruteQ1, BruteQ2))

# ################################################
# not handing recursive case correctly


#
# p1 = [(randint(0, 10), randint(0, 10)) for i in range(10)]
# Px, Py = dimensional_merge_sort(p1, 0), dimensional_merge_sort(p1, 1)
# # print("p1: ", p1)
# # print("Px: ", Px)
# # print("Py: ", Py)
# # print("---------------")
# mid_point = int(Px[-1][0]/2)
# print("mid_point: ", mid_point)
#
# Qx = [x for x in Px if x[0] <= mid_point]
# Qy = [y for y in Py if y[0] <= mid_point]
#
# # Rx = Px[int(len(Px)/2):]
# Rx = [x for x in Px if x[0] > mid_point]
# Ry = [y for y in Py if y[0] > mid_point]
# # partitioning correctly
#
# print("Qx: ", Qx)
# print("Qy: ", Qy)
# print("Rx: ", Rx)
# print("Ry: ", Ry)

# Q1, Q2 = closest_pair(Qx, Qy)
# print("closest pair res: ", Q1, Q2)
# BruteQ1, BruteQ2 = brute_force(Qx, Qy)
# print("brute force res: ", BruteQ1, BruteQ2)
#
# print("test: ", (Q1, Q2) == (BruteQ1, BruteQ2))


# print("------------------")

# ----------------------------------------
# base_case_test_X = [(1, 4), (5, 100)]
# base_case_test_Y = [(5, 2), (7, 0)]
#
# #
# print(closest_pair(base_case_test_X, base_case_test_Y))
# print(brute_force(base_case_test_X, base_case_test_Y))
# print("-------------")
#
# for p in base_case_test_X:
#     for q in base_case_test_Y:
#         print(p, q)
#         print("dist: ", calc_euclidean_dist(p, q))
#

# ###########

# a = [1, 2, 3, 4, 5, 6]
# print(type(len(a)/2))


# Testing Brute Force ###########

# p1 = [(randint(0, 10), randint(0, 10)) for i in range(10)]
# p2 = p1[::-1]
#
#
# print(p1)
# print(p2)
#
# print("---")
# brute1, brute2 = brute_force(p1, p2)
# print("brute force res: ", brute1, brute2)
# brute_dist = calc_euclidean_dist(brute1, brute2)
# print("distance: ", brute_dist)
# print("---")
#
# print("hard code res: ")
#
# min_distance = 10000
# bestX, bestY = 0, 0
# for p in p1:
#     for q in p2:
#         dist = calc_euclidean_dist(p, q)
#         if dist < min_distance and dist != 0:
#             min_distance = dist
#             bestX, bestY = p, q
#
# print(bestX, bestY)
# hard_dist = calc_euclidean_dist(bestX, bestY)
# print("distance: ", hard_dist)
# print("---")
#
# print("Testing.... ", brute_dist == hard_dist)


# ----------------------------
#
# p1 = (1, 5)
# p2 = (5, 1)
#
# print(32 ** .5)
#
# print(calc_euclidean_dist(p1, p2))

# print(calc_euclidean_dist(p1, p2))

# a = float("inf")
# print(a)
#
# print(a > 10)
#
# b = a + 5
# print(type(b))

# a = 110
# b = 100
#
# if a or b < 10:
#     print("hi")
#     print(a)
# else:
#     print("na")

# a = [(2, 1), (4, 5), (9, 10)]
# print(a[-1][0]/2)

# a = [(2, 1), (4, 4), (9, 10), (3, 8)]
# mid_point = 5
# Qy = [y for y in a if y[0] < mid_point]
# print(Qy)

# test_set = []
# for i in range(0, 10):
#     test_set.append(((randint(0, 10)), randint(0, 10)))
#
# print(test_set)

# x_coords = [x_coords.append(x) for x in test_set[0]]

# x_coords = [(lambda x: x_coords.append(x) for x in test_set)]
# (lambda x: x_coords.append(x) for x in test_set)

# x_coords = [x for x in test_set[x][0]]

# print(x_coords)

# for i in range(len(test_set)):
#     x_coords.append(test_set[i][0])
#
# print(x_coords)

# x_coords = [x[0] for x in test_set]  # SUCCESS!
# print(x_coords)

# nums = [1, 2, 3, 4, 5]
#
# list_comp = [n for n in nums]
# print(list_comp)

# # a = [5, 3, 1, 2, 4, 6]
# # b = [1, 3, 5]
# # c = [2, 4, 6]
#
# # print(count_split_inversions(b, c))
#
# a = create_array(15, 10)
# print(a)
# print("---")
# print(count_inversions(a))
