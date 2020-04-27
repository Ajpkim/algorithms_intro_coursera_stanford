import queue  # for printing bst
import random  # for testing

# Implementation of a binary search tree


class Node():
    "Class to handle  data within binary search tree."

    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.size = 1  # size of sub-tree rooted at node

    def __lt__(self, other_node):
        if self.data < other_node.data:
            return 1
        elif self.data == other_node.data:
            return 0
        else:
            return -1

    def __le__(self, other_node):
        if self.data <= other_node.data:
            return 1
        elif self.data == other_node.data:
            return 0
        else:
            return -1

    def __repr__(self):
        return str(self.data)


class BST():
    "Binary search tree implementation."

    def __init__(self, initial_data=None):
        self.root = None
        self.size = 0
        self.nodes = None
        if initial_data:
            self.build(initial_data)

    def build(self, elements):
        "Build, or add to existing, binary search tree with given elements"
        for e in elements:
            self.insert(e)
        return self.ordered()

    def search(self, data):
        "Return node with given data."
        if self.root.data == data:
            return self.root

        if data <= self.root.data:
            return self._recursive_search(data, self.root.left)
        else:
            return self._recursive_search(data, self.root.right)

    def _recursive_search(self, data, current_node):
        "Function to recursively search bst for given data."
        if data == current_node.data:
            return current_node
        else:
            if data <= current_node.data and current_node.left:
                return self._recursive_search(data, current_node.left)

            elif data > current_node.data and current_node.right:
                return self._recursive_search(data, current_node.right)

            else:
                return None

    def insert(self, data):
        "Insert data into bst and maintain bst property."
        self.size += 1

        if self.root == None:
            self.root = Node(data)
        else:
            self._recursive_insert(data, self.root)

    def _recursive_insert(self, data, current_node):
        "Recursively find correct place to insert new data."
        if data <= current_node.data:
            if current_node.left == None:
                current_node.left = Node(data, parent=current_node)
                self._increase_parent_sizes(current_node.left)
            else:
                self._recursive_insert(data, current_node.left)
        else:
            if current_node.right == None:
                current_node.right = Node(data, parent=current_node)
                self._increase_parent_sizes(current_node.right)
            else:
                self._recursive_insert(data, current_node.right)

    def _increase_parent_sizes(self, node):
        while node.parent:
            node = node.parent
            node.size += 1

    def _decrease_parent_sizes(self, node):
        while node.parent:
            node = node.parent
            node.size -= 1

    def delete(self, data):
        "Delete given data from bst."
        node = self.search(data)
        if not node:
            return False  # data isn't in tree
        else:
            return self.delete_node(node)

    def delete_node(self, node):
        "Helper function to delete nodes from bst while maintaining bst property."

        def num_children(node):
            n = 0
            if node.left:
                n += 1
            if node.right:
                n += 1
            return n

        num_children = num_children(node)

        if num_children == 0:  # Case 1. Delete leaf node.
            self._decrease_parent_sizes(node)
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

            return True

        if num_children == 1:  # Case 2. Splice child into node position.
            self._decrease_parent_sizes(node)
            if node.left:
                child = node.left
            else:
                child = node.right

            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child

            child.parent = node.parent

            return True

        if num_children == 2:  # Case 3. Swap with successor and recurse.
            successor = self.successor(node.data, get_node=True)
            node.data = successor.data
            return self.delete_node(successor)

    def predecessor(self, data, get_node=False):
        "Return the predecessor data (or node, if get_node==True) from bst"
        node = self.search(data)
        if not node:
            return False

        if node.left != None:
            node = node.left
            while node.right != None:
                node = node.right
            return node if get_node else node.data

        else:
            while node.parent != None:
                node = node.parent
                if node.data < data:
                    return node if get_node else node.data

            return None

    def successor(self, data, get_node=False):
        "Return the predecessor data (or node, if get_node==True) from bst"
        node = self.search(data)
        if not node:
            return False

        if node.right != None:
            node = node.right
            while node.left != None:
                node = node.left
            return node if get_node else node.data
        else:
            while node.parent != None:
                node = node.parent
                if node.data > data:
                    return node if get_node else node.data
            return None  # No successor bc data is max element in tree

    def rank(self, data):
        "Return the ith order statistic that given data represents in the bst"
        return self._recursive_rank(data, self.root, 1)  # No 0 rank element

    def _recursive_rank(self, data, current_node, rank):
        if data == current_node.data:
            return rank

        elif data < current_node.data:
            return self._recursive_rank(data, current_node.left, rank)

        else:
            rank_adjustment = current_node.left.size + 1 if current_node.left else 1
            rank += rank_adjustment
            return self._recursive_rank(data, current_node.right, rank)

    def select(self, ith_order_statistic):
        "Return the ith order element from the BST with node as root (default node is tree root)"
        if ith_order_statistic < 1 or ith_order_statistic > self.size:
            return None
        return self._recursive_select(self.root, ith_order_statistic)

    def _recursive_select(self, node, ith_order_statistic):
        num_left_nodes = node.left.size if node.left else 0

        if num_left_nodes + 1 == ith_order_statistic:
            return node.data

        elif num_left_nodes >= ith_order_statistic:
            return self._recursive_select(node.left, ith_order_statistic)

        else:
            # adjust ith_order_statistic for removed left nodes and root
            return self._recursive_select(node.right, ith_order_statistic - num_left_nodes - 1)

    def min(self):
        "Return the min element in bst"
        node = self.root
        while node.left != None:
            node = node.left
        return node.data

    def max(self):
        "Return the max element in bst"
        node = self.root
        while node.right != None:
            node = node.right
        return node.data

    def ordered(self):
        "Return an ordered list of data in bst"
        processed = []
        self.recursive_traversal(self.root, processed)
        return processed

    def recursive_traversal(self, current_node, processed):
        "Recursively process nodes in order to produce ordered list"

        if current_node.left:
            self.recursive_traversal(current_node.left, processed)

        processed.append(current_node.data)

        if current_node.right:
            self.recursive_traversal(current_node.right, processed)

    def __repr__(self):
        que = queue.Queue()
        que.put(self.root)
        que.put('\n')

        s = 'Binary Search Tree. Node(Parent)\n'

        while que.qsize():
            node = que.get()

            if node != '\n':
                s = s + str(node) + f'({node.parent})' + '  '

                if node.left:
                    que.put(node.left)

                if node.right:
                    que.put(node.right)

            else:
                s = s + '\n'
                if que.qsize() == 0:
                    break
                else:
                    que.put('\n')
        return s


if __name__ == '__main__':
    pass
