from random import randint


def create_array(size, max):
    return [randint(0, max) for _ in range(size)]


def count_inversions(a):
    n = len(a)

    if n <= 1:
        return a, 0
    else:
        b, x = count_inversions(a[:ceil_div(n, 2)])
        c, y = count_inversions(a[ceil_div(n, 2):])
        d, z = count_split_inversions(b, c)

        return d, (x + y + z)


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


arr = create_array(8, 10)
print(arr)
print(count_inversions(arr))
