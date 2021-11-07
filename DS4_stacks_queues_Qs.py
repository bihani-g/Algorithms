# max in a stack
#
# class max_stack:
#
#     def __init__(self):
#         self.main_stack = []
#         self.max_stack = []
#
#     def push(self, data):
#
#         self.main_stack.append(data)
#
#         if len(self.main_stack) == 1:
#             self.max_stack.append(data)
#             return
#
#         if data > self.max_stack[-1]:
#             self.max_stack.append(data)
#         else:
#             self.max_stack.append(self.max_stack[-1])
#
#             return
#
#     def pop(self):
#         return self.main_stack[-1]
#
#     def get_max_item(self):
#         return self.max_stack[-1]
#
#
# if __name__ == "__main__":
#     max_stack_ = max_stack()
#
#     max_stack_.push(10000)
#     max_stack_.push(5)
#     max_stack_.push(4)
#     max_stack_.push(20000)
#
#     print(f"max item is: {max_stack_.get_max_item()}")


# queue with stacks

# using 2 stacks
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


class Queue_stack:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, data):
        self.stack1.push(data)
        self.stack2.push(self.stack1.peek())

    def pop(self):

        if self.stack2.stack_size() > 0:
            print(f"{self.stack2.pop()}")
            return self.stack2.pop()
        else:
            print("Queue is empty.")


# using recursion

class Queue_recursion:

    def __init__(self):
        self.stack = Stack()

    def enqueue(self, data):
        self.stack.push(data)

    def dequeue(self):

        item = self.stack.pop()

        if self.stack.stack_size() < 1:
            print(f"{item}")
            return item

        popped_item = self.dequeue()

        self.stack.push(item)

        return popped_item


if __name__ == "__main__":
    some_q = Queue_recursion()
    j = 4

    for i in range(4):
        some_q.enqueue(i)

    while j:
        some_q.dequeue()
        j -= 1
