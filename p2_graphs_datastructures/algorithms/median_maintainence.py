from p2_graphs_datastructures.data_structures import heap
from p2_graphs_datastructures.testing.heap_testing import test_maxheap, test_minheap


def median_maintainence(data_stream):
    """
    Algorithm computes the median at every point of a stream of numbers.
    For given array A of length k, result will be of length k.
    The element at position i in the result is the median of the elements
    in A from index 0 to i.

    Args:
        - An array of numbers.

    Returns:
        - List who's ith element corresponds to median of given
        array up to index i in original array.
    """
    stream_medians = []
    minheap, maxheap = [], []
    # initialize with first element before looping
    heap.maxheap_push(maxheap, data_stream[0])
    stream_medians.append(data_stream[0])

    for e in data_stream[1:]:

        # place new number in correct heap based on max and min elements
        if e < heap.maxheap_min_element(maxheap):
            heap.minheap_push(minheap, e)
        else:
            heap.maxheap_push(maxheap, e)

        # ensure heap sizes are balanced and len(maxheap) always <= len(minheap)
        if len(maxheap) > len(minheap):
            maxheap_min = heap.maxheap_min_element(maxheap)
            heap.minheap_push(minheap, maxheap_min)
            maxheap.remove(maxheap_min)  # potentially breaks the heap property
            heap.heapify_max(maxheap)

        elif len(minheap) - len(maxheap) > 1:
            minheap_max = heap.minheap_max_element(minheap)
            heap.maxheap_push(maxheap, minheap_max)
            minheap.remove(minheap_max)
            heap.heapify_min(minheap)

        # find median of numbers processed so far
        median = get_median(minheap, maxheap)
        stream_medians.append(median)

    return stream_medians


def get_median(minheap, maxheap):
    if len(minheap) == len(maxheap):
        return heap.minheap_max_element(minheap)
        # return heap.maxheap_min_element(maxheap)

    elif len(minheap) < len(maxheap):
        return heap.maxheap_min_element(maxheap)

    else:
        return heap.minheap_max_element(minheap)


def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            e = int(line.strip('\n'))
            data.append(e)

    return data


if __name__ == '__main__':
    pass
