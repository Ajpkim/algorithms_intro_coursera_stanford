import random


def randomized_selection(a, x, l, r):
    """
    finds the xth order element in array a.

    args:
        - a an array of numbers
        - x statistic of interest (x=0 means find smallest element)
        - l, r are indice boundaries to look through

    returns:
        - xth order statisic of array a[l, r]
    """
    assert x > 0
    assert x <= len(a[l:r])  # cannot look for element outside array

    # base case
    if len(a[l:r]) < 2:
        return a[l:r][0]

    pivot_index = partition(a, l, r)

    if pivot_index + 1 == x:  # if 1st pivot selected == x... unlikely
        return a[pivot_index]

    elif pivot_index + 1 <= x:  # x is to the right of pivot
        if pivot_index + 1 == x:
            return a[pivot_index]
        else:
            new_x = x - (pivot_index + 1)
            new_l = pivot_index + 1
            return randomized_selection(a, new_x, new_l, r)

    else:  # x is to the left of pivot
        return randomized_selection(a, x, l, pivot_index)

    return


def partition(a, l, r):

    # find random pivot for partition
    pivot_index = random.randint(l, r-1)
    pivot = a[pivot_index]

    swap_with_pivot = a[l]
    a[l] = pivot
    a[pivot_index] = swap_with_pivot

    # partition array in-place around pivot element
    i = l + 1
    for j in range(l + 1, r):
        if a[j] < pivot:
            swap = a[i]
            a[i] = a[j]
            a[j] = swap
            i += 1

    # move pivot to correct location and track location
    swap_with_pivot = a[i-1]
    a[i-1] = pivot
    a[l] = swap_with_pivot
    pivot_final_index = i-1

    return pivot_final_index

# --------------------- TESTING ----------------------------
# x = 1
# print(randomized_selection(a, x, 0, len(a)))


a = [2, 7, 3, 15, 4, 14, 8, 13, 9, 5, 16, 1, 6, 10, 11, 12]


i = 1

for j in range(1, 15):
    res = randomized_selection(a, j, 0, len(a))
    if res != j:
        print("ERROR")
        print("j: {}, result: {}".format(j, res))
        break

print("done")

# for i in range(1, 16):
#     for j in range(0, 1000):
#         res = randomized_selection(a, i, 0, len(a))
#         if res != i:
#             print("ERROR... x={}, res={}".format(i, res))


def test_randomized_selection(sizes, trials):

    for size in sizes:
        a = []

        for i in range(1, size + 1):
            a.append(i)

        random.shuffle(a)

        for j in range(1, size + 1):
            for n in range(trials):

                result = randomized_selection(a, j, 0, len(a))
                if result != j:
                    print("ERROR")
                    print("size: {}, j: {}, result: {}".format(size, j, result))

    print("Test complete. No errors found.")


sizes = [3, 12, 21, 40]
trials = 5

# test_randomized_selection(sizes, trials)
