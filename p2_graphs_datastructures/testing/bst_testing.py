import random

from p2_graphs_datastructures.data_structures.binary_search_tree import BST, Node


def check_bst_property(bst):
    data_elements = bst.ordered()
    for data in data_elements:
        node = bst.search(data)

        if node.parent:
            if node == node.parent.left:
                assert node <= node.parent

            if node == node.parent.right:
                assert node > node.parent

        if node.left:
            assert node >= node.left

        if node.right:
            assert node < node.right


def test_bst(num=100, size=100, smallest=-100, largest=100):
    print('Testing Binary Search Tree')
    print(f'{num} trials with {size} elements [{smallest}:{largest}]')
    for n in range(num):
        bst = BST([random.randint(smallest, largest) for i in range(size)])
        check_bst_property(bst)
    print('Passed Test')


num = 100
size = 100
smallest = -1000
largest = 1000

if __name__ == '__main__':
    pass

# ################################################################################

# bst = BST([random.randint(0, 500) for i in range(100)])
# check_bst_property(bst)


# x = [10, 25, 78, 12, 8, 99, 16, 74, 5, 0]
# print(x)
# b = BST(x)
# s = b.build_tree_str()
# print(s)
# print()


# q = queue.Queue()
# q.put(None)
# print(q.qsize())

# a = 'a b c\nd e f\ng h i'
# # print(a)
# # for line in a:
# #     print(line)
# b = a.split('\n')
# print(b)
# x = [random.randint(0, 100) for i in range(10)]
# print(b.ordered())
# # print(b.select(2))
# c = [b.select(i) for i in range(1, len(x) + 1)]
# print(c)
# print(len(x))
# print(b.select(5))
# print()
# d = b.rank(0)
# print(d)


# print(b.root.size)
# b.delete(78)
# b.delete(5)
# print(b.ordered())
# print(b.root.size)
# c = b.predecessor(16, get_node=True)
# print(c)
# print(c.size)
# print()
# a = BST()
# print(BST().build(x))


# b = a.build(x)
# print(b)
# a.insert(55)
# a.insert(50)
# for i in range(10):
#     print(i)
#     a.insert(i)

# a.insert(100)
# for i in range(90, 50, -10):
#     a.insert(i)
# print(f'predessor of {i+10}: {a.predecessor(i+10)}')
# print(f'successor of {i+10}: {a.successor(i+10)}\n')


# a.insert(55)
# a.insert(333)
# a.insert(75)
# large = a.max()
# small = a.min()
# print(large)
# print(small)
# print(a.successor(100))
# print(a.predecessor(60))
# print('\n\n')

# ordered = a.ordered()
# print(f'ordered = {ordered}')
# print(a.tree)

# print(a.size)
# print(a.predecessor(9))
