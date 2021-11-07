import time


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # Insertion at beginning has O(1) TC
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if self.head:
            new_node.nextNode = self.head

        self.head = new_node

    # Insertion at end has O(N) TC
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_linkedlist(self):
        return self.numOfNodes

    def traverse_linkedlist(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove_item(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        if actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        # search miss i.e. item not in list
        if actual_node is None:
            return

        if previous_node is None:
            # i.e. the node to be removed was found in the first loop, i.e.
            # we remove the head node
            self.head = actual_node.nextNode
            self.numOfNodes = self.numOfNodes - 1

        else:
            # remove the actual_node
            previous_node.nextNode = actual_node.nextNode
            self.numOfNodes = self.numOfNodes - 1

    def find_mid(self):

        fast_pointer = self.head
        slow_pointer = self.head

        # when fast pointer reaches end of list, slow pointer reaches mid
        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer

    def reverse_linkedlist(self):

        current_node = self.head
        next_node = None
        prev_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node




# linked_list = LinkedList()
#
# linked_list.insert_start(4)
# linked_list.insert_start(3.0)
# linked_list.insert_start('adam')
# linked_list.insert_end(10)
# linked_list.traverse_linkedlist()
# linked_list.remove_item(3000)
# print('----')
# linked_list.traverse_linkedlist()
# print(linked_list.size_of_linkedlist())

# Comparing running time with arrays

# if __name__ == '__main__':
#     linked_list = LinkedList()
#
#     now = time.time()
#
#     for i in range(500000):
#         linked_list.insert_start(i)
#
#     print("Time taken for LL is : %ss" % str(time.time() - now))
#
#     array = []
#     now = time.time()
#
#     for i in range(500000):
#         array.insert(0, i)
#
#     print("Time taken for array is : %ss" % str(time.time() - now))



if __name__ == '__main__':
    ll = LinkedList()

    for i in range(101):
        ll.insert_start(i)

    print(ll.find_mid().data)

    ll.traverse_linkedlist()

    ll.reverse_linkedlist()

    ll.traverse_linkedlist()

