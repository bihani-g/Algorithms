class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.previousNode = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data): # DLL typically insert at the end

        new_node = Node(data)
        if self.head is None: # list is initially empty
            self.head = new_node
            self.tail = new_node
        else: # at least one item in the DLL
            new_node.previousNode = self.tail
            self.tail.nextNode = new_node
            self.tail = new_node

    def traverse_forward(self):

        current_node = self.head

        while current_node is not None:
            print("%d" % current_node.data)
            current_node = current_node.nextNode

    def traverse_backward(self):

        current_node = self.tail

        while current_node is not None:
            print("%d" % current_node.data)
            current_node = current_node.previousNode

# if __name__ == '__main__':
#     dll = DoublyLinkedList()
#
#     dll.insert_end(1)
#     dll.insert_end(2)
#     dll.insert_end(3)
#
#     dll.traverse_forward()




