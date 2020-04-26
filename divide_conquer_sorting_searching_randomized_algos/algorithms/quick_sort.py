from random import randint


def quick_sort(a, left, right):

    if len(a[left:right]) < 2:
        return a

    i, j = partition(a, left, right)

    quick_sort(a, left, i - 1)
    quick_sort(a, i, right)

    return a


def partition(a, left, right):
    """
    partitions array in-place between indices l, r

    args:
        - a is the array to be partitioned
        - l is the left boundary of the array a that is being partioned
        - r is the right boundary of the array a that is being partioned

    returns:
        - array that is partiotioned in between indices l, r around a[l]
    """
    if len(a[left:right]) < 2:
        return a

    # choose random pivot
    pivot_index = find_partition(a, left, right)

    # swap first element with pivot element
    swap_with_pivot = a[left]
    a[left] = a[pivot_index]
    a[pivot_index] = swap_with_pivot
    pivot = a[left]

    i = left + 1  # boudary index of <p and >p elements within partioned portion

    for j in range(left + 1, right):

        if a[j] < pivot:
            to_move = a[i]
            a[i] = a[j]
            a[j] = to_move
            i += 1

    swap_with_pivot = a[i-1]
    a[i-1] = pivot
    a[left] = swap_with_pivot

    # return indices for boundaries around pivot
    return i, j


def find_partition(a, left, right):
    return randint(left, right-1)

# ##################################
# a = [3, 2, 5, 7, 9, 0, 1, 5]
# print("original array", a)
# # # # test=partition(a, 0, len(arr))
# # # # print("partitioned array", test)
# result = quick_sort(a, 0, len(a))
# print(result)


a = [1, 2, 99, 43, 78, 21, 3, 7, 2, 102, 503, 33, 1, 0, 5, 2, 8, 2, 7]
print(a)
print(quick_sort(a, 0, len(a)))
