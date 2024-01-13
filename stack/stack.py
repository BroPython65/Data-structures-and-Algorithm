class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)


# Example Usage:
if __name__ == "__main__":
    # Create a stack
    my_stack = Stack()

    # Push elements onto the stack
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    # Print the stack
    print("Stack:", my_stack.items)

    # Peek at the top element
    print("Top element:", my_stack.peek())

    # Pop elements from the stack
    popped_item = my_stack.pop()
    print("Popped item:", popped_item)
    print("Stack after pop:", my_stack.items)

    # Check if the stack is empty
    print("Is the stack empty?", my_stack.is_empty())

    # Get the size of the stack
    print("Size of the stack:", my_stack.size())
