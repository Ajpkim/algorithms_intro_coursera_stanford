from find_closest_pair import *

# testing with for loop


def test_closest_pair(size, max, nums):
    for i in range(nums):
        P1 = [(randint(0, max), randint(0, max)) for i in range(nums)]
        Px = dimensional_merge_sort(P1, 0)

        brute_result = closest_pair_brute_force(Px)
        find_closest_pair_result = find_closest_pair(P1)

        if(brute_result[0] != find_closest_pair_result[0]):
            print("FAILED")
            print("Px = ", Px)
            print("brute_result = ", brute_result)
            print("find_closest_pair_result = ", find_closest_pair_result)
            return

    print("PASSED! Tested {} arrays of {} numbers ranging".format(nums, size),
          "from 0 to {} with no errors".format(nums, size, max))


test_closest_pair(10, 25, 100)


# Error Finder ... find counterexamples and debug #####
# P1 = [(randint(0, 25), randint(0, 25)) for i in range(4)]
# Px = dimensional_merge_sort(P1, 0)
# Py = dimensional_merge_sort(P1, 1)
#
# # Debugging set up: #####
# print("Px: ", Px)
# print("Py: ", Py)
# closest_pair_result = closest_pair(Px, Py)
# brute_res = closest_pair_brute_force(Px)
# find_result = find_closest_pair(P1)
# print("")
# print("")
# print("closest_pair: ", closest_pair_result)
# print("brute_force: ", brute_res)
# print("find_closest_pair: ", find_result)
# print("---------->>>>>>", closest_pair_result[0] == brute_res[0] == find_result[0])


# ############################################
# P1 = [(2, 25), (3, 15), (6, 19), (23, 25)]
# Px = [(2, 25), (3, 15), (6, 19), (23, 25)]
# Py = [(3, 15), (6, 19), (2, 25), (23, 25)]
#
# print("Px: ", Px)
# print("Py: ", Py)
# closest_pair_result = closest_pair(Px, Py)
# brute_res = closest_pair_brute_force(Px)
# find_result = find_closest_pair(P1)
# print("")
# print("")
# print("closest_pair: ", closest_pair_result)
# print("brute_force: ", brute_res)
# print("find_closest_pair: ", find_result)
# print("---------->>>>>>", closest_pair_result[0] == brute_res[0] == find_result[0])


# ############################################
# Px:  [(6, 20), (6, 10), (13, 11), (25, 22)]
# Py:  [(6, 10), (13, 11), (6, 20), (25, 22)]
#
#
# P1 = [(randint(0, 25), randint(0, 25)) for i in range(4)]
# Px = dimensional_merge_sort(P1, 0)
# Py = dimensional_merge_sort(P1, 1)
# print("Px: ", Px)
# print("Py: ", Py)
# closest_pair_result = closest_pair(Px, Py)
# print("closest_pair: ", closest_pair_result)
# brute_res = closest_pair_brute_force(Px)
# print("brute_force: ", brute_res)
# find_result = find_closest_pair(P1)
# print("find_closest_pair: ", find_result)
# print("----------")
# print("same results?....", closest_pair_result[0] == brute_res[0] == find_result[0])

# ############################################
# P1 = [(4, 20), (4, 8), (12, 24), (17, 5)]
# Px = [(4, 20), (4, 8), (12, 24), (17, 5)]
# Py = [(17, 5), (4, 8), (4, 20), (12, 24)]
#
# print("Px: ", Px)
# print("Py: ", Py)
# closest_pair_result = closest_pair(Px, Py)
# print("closest_pair: ", closest_pair_result)
# brute_res = closest_pair_brute_force(Px)
# print("brute_force: ", brute_res)
# find_result = find_closest_pair(P1)
# print("find_closest_pair: ", find_result)
# print("----------")
# print("same results?....", closest_pair_result[0] == brute_res[0] == find_result[0])
