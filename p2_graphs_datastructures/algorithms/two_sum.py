import bisect


def two_sum(filename):
    data = load_file(filename)
    data.sort()
    sum_set = set()

    for x in data:

        low = -10_000 - x
        high = 10_000 - x

        left = bisect.bisect_left(data, low)
        right = bisect.bisect_right(data, high)

        for y in data[left:right]:
            if x != y:
                sum_set.add(x+y)
    return len(sum_set)


def load_file(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(int(line))
    return data
