from random import randint

# Merge Sort implementation


def create_array(size, max):
    return [randint(0, max) for _ in range(size)]


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


# Test
# a = [5, 9, 15]
# b = [4, 5, 11]
# print(merge(a, b))


def merge_sort(a):
    # recursive base case
    if len(a) <= 1:
        return a

    left = merge_sort(a[:int(len(a)/2)])
    right = merge_sort(a[int(len(a)/2):])

    return merge(left, right)


# Tests
a = create_array(10, 100)
print("original array: ", a)
s = merge_sort(a)
print("sorted array: ", s)
