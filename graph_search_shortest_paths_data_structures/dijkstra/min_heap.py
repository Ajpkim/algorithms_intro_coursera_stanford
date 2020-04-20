import random
# Going to implement own heap class to consolidate understanding


class MinHeap():
    "Min heap implementation."

    def __init__(self, x=None):
        self.heap = self.build_min_heap(x) if x else []

    def build_min_heap(self, x):
        "build a min heap from scratch containing the elements in x"
        self.heap = []
        for e in x:
            self.insert(e)
        return self.heap

    def extract_min(self):
        "Return the min element atop the heap. Place the bottom element on top and then maintain heap invariant"
        min = self.heap[0]

        if len(self.heap) == 1:
            del self.heap[0]
            return min

        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._bubbledown(0)

        return min

    def insert(self, e):
        "Insert new element e into the heap and maintain heap property"
        self.heap.append(e)  # insert element at bottom of heap
        self._bubbleup(len(self.heap) - 1)  # Maintain heap prop

    def _bubbleup(self, idx):
        "maintain heap invariant by sifting up element at position idx until in legal position"
        e = self.heap[idx]

        while idx > 0:
            parent_idx = self._parent(idx)
            parent = self.heap[parent_idx]
            if e < parent:
                self._swap(idx, parent_idx)
                idx = parent_idx
                continue
            break

        self.heap[idx] = e

    def _bubbledown(self, idx):
        "Maintain heap invariant by sifting element at idx down to a leaf and then up to a legal position"

        e = self.heap[idx]

        while self._left_child(idx):

            child_idx = self._left_child(idx)

            if self._right_child(idx):
                right_child_idx = child_idx + 1
                if self.heap[right_child_idx] < self.heap[child_idx]:
                    child_idx = right_child_idx

            self.heap[idx] = self.heap[child_idx]
            idx = child_idx

        self.heap[idx] = e
        self._bubbleup(idx)

        # implementation with no bubbling up afterwards
        # e = self.heap[idx]

        # while self._left_child(idx):
        #     left_idx = self._left_child(idx)
        #     left_child = self.heap[left_idx]

        #     if self._right_child(idx):
        #         right_idx = self._right_child(idx)
        #         right_child = self.heap[right_idx]

        #         if e > left_child and e > right_child:
        #             self.heap[idx] = min(left_child, right_child)
        #             self.heap[left_idx] = max(left_child, right_child)
        #             idx = right_idx
        #             continue

        #         if e > left_child and e < right_child:
        #             self.heap[idx] = left_child
        #             self.heap[left_child] = e
        #             idx = left_idx
        #             continue

        #         if e < left_child and e < right_child:
        #             return

        #     else:  # no right child
        #         if e > left_child:
        #             self.heap[idx] = left_child
        #             idx = left_idx
        #             continue
        #         else:
        #             return

    def _swap(self, i, j):
        "swap 2 elements in the heap"
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent(self, idx):
        "return the parent idx if exists, None otherwise"
        if idx == 0:
            return None

        return (idx - 1) // 2

    def _left_child(self, idx):
        "return idx of left child if exists, None otherwise"
        res = (idx * 2) + 1
        return res if res < len(self.heap) else None

    def _right_child(self, idx):
        "return idx of right child if exists, None otherwise"
        res = (idx * 2) + 2
        return res if res < len(self.heap) else None

    def __repr__(self):
        if len(self.heap) == 0:
            return "min heap with 0 elements"
        else:
            s = f"MinHeap with {len(self.heap)} elements and min element = {self.heap[0]}\n"
            s = s + str(self.heap) + '\n\n'
            for i in range(len(self.heap)):
                e = self.heap[i]

                parent = self.heap[self._parent(i)] if i != 0 else None
                lc = self.heap[self._left_child(
                    i)] if self._left_child(i) else None
                rc = self.heap[self._right_child(
                    i)] if self._right_child(i) else None

                s = s + f"e={e}, p = {parent}, lc = {lc}, rc = {rc}\n"
            return s


def test_heap_invariant(h):

    for i in range(len(h.heap)):
        e = h.heap[i]

        if h._parent(i):
            parent = h.heap[h._parent(i)]
            if not e >= parent:
                print("HEAP MALFUNCTION")
                print(f"e={e}, parent={parent}")
                break

        if h._left_child(i):
            lc = h.heap[h._left_child(i)]
            if not e <= lc:
                print("HEAP MALFUNCTION")
                print(f"e={e}, lc={lc}")
                break

        if h._right_child(i):
            rc = h.heap[h._right_child(i)]
            if not e <= rc:
                print("HEAP MALFUNCTION")
                print(f"e={e}, rc={rc}")
                break

    # print("No violations")


def run_tests(size, min, max, num):
    for n in range(num):
        a = [random.randint(min, max) for i in range(size)]
        h = MinHeap(a)

        while len(h.heap) > 0:
            test_heap_invariant(h)
            h.extract_min()
    print("Done.")


size = 100
min = -300
max = 300
num = 500

run_tests(size, min, max, num)
