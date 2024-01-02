class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def push_after(self, prev_node_data, data):
        new_node = Node(data)
        current_node = self.head

        while current_node:
            if current_node.data == prev_node_data:
                new_node.next = current_node.next
                new_node.prev = current_node
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node
                return
            current_node = current_node.next

        print(f"Node with data {prev_node_data} not found in the list.")

    def delete_node(self, key):
        current_node = self.head

        while current_node:
            if current_node.data == key:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev

                current_node = None
                return
            current_node = current_node.next

        print(f"Node with data {key} not found in the list.")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")


# Example usage:
doubly_linked_list = DoublyLinkedList()

# Appending nodes
doubly_linked_list.push_end(1)
doubly_linked_list.push_end(2)
doubly_linked_list.push_end(3)

# Prepending a node
doubly_linked_list.push_front(0)

# Printing the doubly linked list
doubly_linked_list.print_list()

# Inserting a node after a specific node
doubly_linked_list.push_after(1, 1.5)

# Printing the doubly linked list after insertion
doubly_linked_list.print_list()

# Deleting a node
doubly_linked_list.delete_node(2)

# Printing the doubly linked list after deletion
doubly_linked_list.print_list()
