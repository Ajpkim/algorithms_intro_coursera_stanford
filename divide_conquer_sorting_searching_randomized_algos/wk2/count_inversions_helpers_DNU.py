from random import randint


def create_array(size, max):
    return [randint(0, max) for _ in range(size)]


def count_split_inversions(b, c):
    d = []
    b_index, c_index = 0, 0
    splits = 0

    while b_index < len(b) and c_index < len(c):
        if b[b_index] <= c[c_index]:
            d.append(b[b_index])
            b_index += 1
        else:
            d.append(c[c_index])
            c_index += 1
            splits += len(b[b_index:])

    if b_index == len(b):
        d.extend(c[c_index:])
    else:
        d.extend(b[b_index:])

    return d, splits


def ceil_div(x, y):
    return (-(-x//y))


# From wk1
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
