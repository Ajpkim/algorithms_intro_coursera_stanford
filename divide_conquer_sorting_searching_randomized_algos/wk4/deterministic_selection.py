import random


def DSelect(a, i):
    """
    finds the ith order statistic of the given array

    args:
        - a, an array of length > 0
        - i, ith order statisic of a, 0 < i < len(a) + 1

    returns:
        - ith order element of array a
    """

    assert(i < len(a) + 1)
    assert(i > 0)
    assert(len(a) > 0)

    if len(a) < 2:
        return a[0]

    pivot = choose_pivot(a)

    pivot_index = partition_DSelect(a, pivot)

    if pivot_index + 1 == i:
        return a[pivot_index]

    elif pivot_index + 1 >= i:
        if pivot_index + 1 == i:
            return a[pivot_index]
        return DSelect(a[0:pivot_index], i)

    else:
        if pivot_index + 1 == i:
            return a[pivot_index]
        return DSelect(a[pivot_index+1:], i - (pivot_index + 1))

    return


def partition_DSelect(a, p):
    # find index of pivot element p
    original_pivot_index = 0
    for i in range(len(a)):
        if a[i] == p:
            original_pivot_index = i
            break

    # make pivot 1st element
    swap_with_pivot = a[0]
    a[0] = a[original_pivot_index]
    a[original_pivot_index] = swap_with_pivot
    pivot = a[0]

    i = 1
    for j in range(1, len(a)):
        if a[j] < pivot:
            swap = a[j]
            a[j] = a[i]
            a[i] = swap
            i += 1

    # move pivot to correct location
    a[0] = a[i-1]
    a[i-1] = pivot
    pivot_final_index = i - 1

    return pivot_final_index


def choose_pivot(a):
    """
    deterministically identifies a pivot p for which it is guaranteed to hold
    that (30% of a) < p < (30% of a)

    args:
        - a, an array

    returns:
        - p, pivot (to partition a around in DSelect())
    """
    # identify how many groups there will be (to help w/ building group lists)
    if len(a) % 5 == 0:
        num_groups = len(a) // 5
    else:
        num_groups = (len(a) // 5) + 1

    # build list made up of group lists
    groups = [a[i*5: i*5 + 5] for i in range(0, num_groups)]

    # sort groups so we can extract medians
    for i in range(len(groups)):
        groups[i] = merge_sort(groups[i])

    # extract medians of each group
    c = [x[(len(x)//2)] for x in groups]

    i = (len(c) // 2)
    i += 1 if i == 0 else 0

    # assign pivot as the median of medians
    p = DSelect(c, i)

    return p


def merge_sort(a):

    if len(a) <= 1:
        return a

    left = merge_sort(a[:int(len(a)/2)])
    right = merge_sort(a[int(len(a)/2):])

    return merge(left, right)


def merge(a, b):

    c = []
    a_index, b_index = 0, 0

    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index += 1
        elif a[a_index] > b[b_index]:
            c.append(b[b_index])
            b_index += 1
        else:
            c.append(a[a_index])
            a_index += 1

    if a_index == len(a):
        c.extend(b[b_index:])
    else:
        c.extend(a[a_index:])

    return c


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


sizes = [10, 11, 57, 101, 38, 58, 420]
test_DSelect(sizes)
