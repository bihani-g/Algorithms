# LIFO structure

class Stack:

    def __init__(self):
        self.stack = []  # 1D array will be used to implement the stack behavior

    # insert item into stack : O(1) time
    def push(self, data):
        self.stack.append(data)

    # remove and return item out of stack : O(1) time
    def pop(self):
        data = self.stack[-1]  # picks the last item of the 1D array
        del self.stack[-1]
        return data

    # returns last item without removing it
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


some_stack = Stack()

some_stack.push(1)
some_stack.push(2)
some_stack.push(3)


# print(f"size: {some_stack.stack_size()}")
# print(f"popped item: {some_stack.pop()}")
# print(f"size: {some_stack.stack_size()}")
# print(f"peek item: {some_stack.peek()}")
# print(f"size: {some_stack.stack_size()}")
# print(f"peek item: {some_stack.peek()}")

# print(f"max in stack is: {some_stack.max_in_stack()}")
