# Implementation of heap data structure using methods that operate on lists in-place
# TODO add method for deleting from middle of heap


def heapify_min(heap):
    """
    Organizes list in-place into a minheap. Only need to look at non-leaf elements.
    This means that largest index that needs to be processed is n//2 - 1. Process 
    elements in reverse order so can simply bubble-up to correct heap property.
    """
    n = len(heap)

    for i in reversed(range(n//2)):
        _bubble_down_min(heap, i)


def heapify_max(heap):
    n = len(heap)

    for i in reversed(range(n//2)):
        _bubble_down_max(heap, i)


def extract_min(heap):
    e = heap[0]  # raises IndexError if heap is empty

    heap[0] = heap[-1]
    del heap[-1]

    if heap:
        _bubble_down_min(heap, 0)

    return e


def extract_max(heap):
    e = heap[0]

    bottom_element = heap.pop()

    if heap:
        heap[0] = bottom_element
        _bubble_down_max(heap, 0)

    return e


def minheap_push(heap, e):
    heap.append(e)
    _bubble_up_min(heap, 0, len(heap)-1)


def maxheap_push(heap, e):
    heap.append(e)
    _bubble_up_max(heap, 0, len(heap)-1)


def minheap_max_element(heap):
    size = len(heap)
    max_element = heap[size // 2]

    for i in range(1 + (size // 2), size):
        max_element = max(max_element, heap[i])

    return max_element


def maxheap_min_element(heap):
    size = len(heap)
    min_element = heap[size // 2]

    for i in range(1 + (size//2), size):
        min_element = min(min_element, heap[i])

    return min_element


def _bubble_up_min(heap, sub_tree_boundary, idx):

    e = heap[idx]

    while idx > sub_tree_boundary:
        parent_idx = (idx - 1) // 2
        parent = heap[parent_idx]
        if e < parent:
            heap[idx] = parent  # move down parent element
            idx = parent_idx
            continue
        break

    heap[idx] = e


def _bubble_up_max(heap, sub_tree_boundary, idx):

    e = heap[idx]

    while idx > sub_tree_boundary:
        parent_idx = (idx - 1) // 2
        parent = heap[parent_idx]
        if e > parent:
            heap[idx] = parent
            idx = parent_idx
            continue
        break

    heap[idx] = e


def _bubble_down_min(heap, idx):
    sub_tree_boundary = idx
    e = heap[idx]
    size = len(heap)

    child_idx = (idx * 2) + 1

    while child_idx < size:  # There is a child
        rc_idx = child_idx + 1

        if rc_idx < len(heap) and heap[rc_idx] < heap[child_idx]:
            child_idx = rc_idx

        heap[idx] = heap[child_idx]
        idx = child_idx
        child_idx = idx * 2 + 1

    heap[idx] = e
    _bubble_up_min(heap, sub_tree_boundary, idx)


def _bubble_down_max(heap, idx):
    sub_tree_boundary = idx
    e = heap[idx]

    child_idx = idx * 2 + 1
    while child_idx < len(heap):

        rc_idx = child_idx + 1

        if rc_idx < len(heap) and heap[rc_idx] > heap[child_idx]:
            child_idx = rc_idx

        heap[idx] = heap[child_idx]
        idx = child_idx
        child_idx = idx * 2 + 1

    heap[idx] = e
    _bubble_up_max(heap, sub_tree_boundary, idx)


if __name__ == '__main__':
    pass
