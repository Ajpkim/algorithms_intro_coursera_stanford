# TODO finish delete method and tracking nodes within tree class.. use self.nodes?


class Node():
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BST():
    def __init__(self, initial_data=None):
        # self.tree = self.build(x) if x else []
        self.root = None
        self.size = 0
        self.nodes = None

    def build(self, elements):
        pass

    def search(self, data):
        if self.root.data == data:
            return self.root

        if data <= self.root.data:
            return self._recursive_search(data, self.root.left)
        else:
            return self._recursive_search(data, self.root.right)

    def _recursive_search(self, data, current_node):
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
        self.size += 1

        if self.root == None:
            self.root = Node(data)
        else:
            self._recursive_insert(data, self.root)

    def _recursive_insert(self, data, current_node):
        if data <= current_node.data:
            if current_node.left == None:
                current_node.left = Node(data, parent=current_node)
            else:
                self._recursive_insert(data, current_node.left)
        else:
            if current_node.right == None:
                current_node.right = Node(data, parent=current_node)
            else:
                self._recursive_insert(data, current_node.right)

    def delete(self, data):
        node = self.search(data)
        if not node:
            return False  # data isn't in tree
        if node.left == None and node.right == None:
            # REMOVE FROM TREE
            pass

    def predecessor(self, data):
        node = self.search(data)
        if not node:
            return False

        if node.left != None:
            node = node.left
            while node.right != None:
                node = node.right
            return node.data

        else:
            while node.parent != None:
                node = node.parent
                if node.data < data:
                    return node

            return None

    def successor(self, data):
        node = self.search(data)

        if not node:
            return False

        if node.right != None:
            node = node.right
            while node.left != None:
                node = node.left
            return node.data

        else:
            while node.parent != None:
                node = node.parent
                if node.data > data:
                    return node.data
            return None  # Given data is max element in tree

    def rank(self, data):
        pass

    def select(self, z):
        pass

    def min(self):
        node = self.root
        while node.left != None:
            node = node.left
        return node.data

    def max(self):
        node = self.root
        while node.right != None:
            node = node.right
        return node.data

    def ordered(self):
        processed = []
        self.recursive_traversal(self.root, processed)
        return processed

    def recursive_traversal(self, current_node, processed):

        if current_node.left:
            self.recursive_traversal(current_node.left, processed)

        processed.append(current_node.data)

        if current_node.right:
            self.recursive_traversal(current_node.right, processed)
