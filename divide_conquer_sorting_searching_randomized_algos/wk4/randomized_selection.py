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

    assert x <= len(a[l:r])  # cannot look for element outside array

    # base case
    if len(a[l:r]) < 2:
        return a[l:r]

    pivot_index = partition(a, l, r)

    if pivot_index == x:  # if 1st pivot selected == x... unlikely
        return a[x]

    elif pivot_index <= x + l:  # x is to the right of pivot
        if pivot_index == x + l:
            return a[pivot_index]
        else:
            randomized_selection(a, (x - (pivot_index + 1)), pivot_index + 1, r)

    else:  # x is to the left of pivot
        randomized_selection(a, x, l, pivot_index)

    return a[x]


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


a = [2, 7, 3, 15, 4, 14, 8, 13, 9, 5, 0, 1, 6, 10, 11, 12]

for i in range(0, 15):
    for j in range(0, 10000):
        res = randomized_selection(a, i, 0, len(a))
        if res != i:
            print("ERROR... x={}, res={}".format(i, res))
