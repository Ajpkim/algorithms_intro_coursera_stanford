import random
import heapq
from heap import *


def test_minheap(minheap):
    for i in range(len(minheap)):
        e = minheap[i]

        if not i == 0:
            parent = minheap[(i-1) // 2]
            if e < parent:
                print("HEAP MALFUNCTION")
                print(f"e = {e}, parent = {parent}")
                return False

        lci = (i*2) + 1
        rci = lci + 1

        if lci < len(minheap):
            lc = minheap[lci]
            if e > lc:
                print("HEAP MALFUNCTION")
                print(f"e = {e}, lc = {lc}")
                return False

        if rci < len(minheap):
            rc = minheap[rci]
            if e > rc:
                print("HEAP MALFUNCTION")
                print(f"e = {e}, rc = {rc}")
                return False
    return True


def test_maxheap(maxheap):
    for i in range(len(maxheap)):
        e = maxheap[i]

        if not i == 0:
            parent = maxheap[(i-1) // 2]
            if e > parent:
                print("HEAP MALFUNCTION")
                print(f"e = {e}, parent = {parent}")
                return False

        lci = (i*2) + 1
        rci = lci + 1

        if lci < len(maxheap):
            lc = maxheap[lci]
            if e < lc:
                print("HEAP MALFUNCTION")
                print(f"e = {e}, lc = {lc}")
                return False

        if rci < len(maxheap):
            rc = maxheap[rci]
            if e < rc:
                print("HEAP MALFUNCTION")
                print(f"e = {e}, rc = {rc}")
                return False
    return True
    # print("No violations")


def test_heapify(heap_type, size, low, high, num):
    if heap_type == 'min':
        for i in range(num):
            h = [random.randint(low, high) for i in range(size)]
            heapify_min(h)
            test_minheap(h)

    elif heap_type == 'max':
        for i in range(num):
            h = [random.randint(low, high) for i in range(size)]
            heapify_max(h)
            test_maxheap(h)
    else:
        print(f'Error: heap_type: {heap_type} is not valid ')


def run_tests(heap_type, size, low, high, num):
    print('testing', heap_type, 'heap...\n')
    if heap_type == 'min':
        for n in range(num):
            starting_vals = [random.randint(low, high) for i in range(size)]
            h = copy.deepcopy(starting_vals)

            heapify_min(h)
            extracted_vals = []

            while len(h) > 0:
                test_minheap(h)
                extracted_vals.append(extract_min(h))

            starting_vals.sort()
            extracted_vals.sort()

            if not starting_vals == extracted_vals:
                print("ERROR: VALUES MODIFIED BY HEAP OPERATIONS")
                print('starting vals:', starting_vals)
                print('extracted_vals:', extracted_vals)
                break

        print("Done.")

    elif heap_type == 'max':
        for n in range(num):
            starting_vals = [random.randint(low, high) for i in range(size)]
            h = copy.deepcopy(starting_vals)

            heapify_max(h)
            extracted_vals = []

            while len(h) > 0:
                test_maxheap(h)
                extracted_vals.append(extract_max(h))

            starting_vals.sort()
            extracted_vals.sort()

            if not starting_vals == extracted_vals:
                print("ERROR: VALUES MODIFIED BY HEAP OPERATIONS")
                print('starting vals:', starting_vals)
                print('extracted_vals:', extracted_vals)
                break

        print("Done.")

    else:
        print(f'Error: heap_type: {heap_type} is not valid ')


# # TESTING HEAP
heap_type = 'max'
size = 100
low = -100
high = 100
num = 100

if __name__ == '__main__':
    run_tests(heap_type, size, low, high, num)
