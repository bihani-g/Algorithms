# binary search trees

class Node:

    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # insert data in BST
    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    # Where to insert data (left subtree or right subtree)
    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def check_rightmost(self, node):
        if node.rightChild:
            return self.check_rightmost(node.rightChild)
        else:
            return node.data

    def check_leftmost(self, node):
        if node.leftChild:
            return self.check_leftmost(node.leftChild)
        else:
            return node.data

    def get_max(self):
        if self.root:
            return self.check_rightmost(self.root)

    def get_min(self):
        if self.root:
            return self.check_leftmost(self.root)


    # remove nodes in BST

    def remove_node(self, data, node):

        if not data:
            return

        if data < node.data:
            return self.remove_node(data, node.leftChild)
        elif data > node.data:
            return self.remove_node(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing leaf node...")

                parent = node.parent

                if parent and parent.leftChild == node:
                    parent.leftChild = None
                if parent and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rightChild is not None:
                print("Removing node with right child...")

                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild

                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.leftChild is not None and node.rightChild is None:
                print("Removing node with left child...")

                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild

                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print("Removing node with two children...") # replace node with predecessor

                predecessor = self.get_predeccessor(node.leftChild)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def remove(self, data):
        if self.root:
            return self.remove_node(data, self.root)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)


if __name__ == "__main__":
    someBST = BinarySearchTree()
    someBST.insert(10)
    someBST.insert(2)
    someBST.insert(8)
    someBST.insert(12)
    someBST.insert(23)
    someBST.insert(54)

    print("Our BST is the following.")
    someBST.traverse()
    print(f"Min. data value in this BST is: {someBST.get_min()}")
    print(f"Max. data value in this BST is: {someBST.get_max()}")

    someBST.remove(12)
    print("Our BST is the following.")
    someBST.traverse()
