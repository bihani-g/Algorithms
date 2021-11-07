# Depth first search with recursion

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def check_adj(stack):
    actual_node = stack.pop()
    actual_node.visited = True
    print(f"Actual Node: {actual_node.name}")

    for n in actual_node.adjacency_list:
        if not n.visited:
            n.visited = True
            stack.append(n)
            return check_adj(stack)


def dfs_r(start_node):
    start_node.visited = True
    print(f"Actual Node: {start_node.name}")

    for n in start_node.adjacency_list:
        if not n.visited:
            return dfs_r(n)


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

    dfs_r(node1)
