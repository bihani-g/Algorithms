# Breadth First Search Implementation

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):
    queue = [start_node]  # FIFO structure

    # keep iterating (visit neighbours of given vertex in queue) until the queue is empty
    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True

        print(f"actual node: {actual_node.name}")

        # lets consider the neighbours of the actual node one by one
        for n in actual_node.adjacency_list:

            if not n.visited:
                queue.append(n)


# Breadth First Search Implementation (practice)

class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def bfs(start_node):
    queue = [start_node]

    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True

        print(f"node visited: {actual_node.name}")

        for n in actual_node.adjacency_list:
            print(f"{n.name} {n.visited}")
            if not n.visited:
                n.visited = True
                queue.append(n)


if __name__ == '__main__':
    # creating the nodes or vertices
    node1 = Node('A')
    node2 = Node('C')
    node3 = Node('B')
    node4 = Node('Q')
    node5 = Node('E')

    # make the neighbours
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node3)
    node3.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)
    node5.adjacency_list.append(node1)
    node5.adjacency_list.append(node2)

    # run the BFS
    bfs(node1)
