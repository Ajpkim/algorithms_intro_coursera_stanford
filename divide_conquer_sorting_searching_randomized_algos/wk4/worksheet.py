from deterministic_selection import *
import random

sizes = [10, 11, 57, 101, 38, 58, 420]


def test_DSelect(sizes):

    for size in sizes:
        a = []
        for i in range(1, size + 1):
            a.append(i)

        random.shuffle(a)

        for i in range(1, size + 1):
            result = DSelect(a, i)
            if result != i:
                print("ERROR")
                print("size: {}, i: {}, result: {}".format(size, i, result))
                return

    print("Test complete. No errors found.")


test_DSelect(sizes)


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
