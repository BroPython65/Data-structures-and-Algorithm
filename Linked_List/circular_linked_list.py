class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        self.head = new_node

    def push_after(self, prev_node_data, data):
        new_node = Node(data)
        current_node = self.head

        while current_node:
            if current_node.data == prev_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

            if current_node == self.head:
                print(f"Node with data {prev_node_data} not found in the list.")
                return

    def delete_node(self, key):
        if not self.head:
            print("List is empty.")
            return

        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.data == key:
                if prev_node:
                    prev_node.next = current_node.next
                    if current_node == self.head:
                        self.head = current_node.next
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = current_node.next
                    self.head = current_node.next if current_node.next != current_node else None

                current_node = None
                return
            prev_node = current_node
            current_node = current_node.next

            if current_node == self.head:
                print(f"Node with data {key} not found in the list.")
                return

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return

        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print(" (head)")


# Example usage:
circular_linked_list = CircularLinkedList()

# Appending nodes
circular_linked_list.push_end(1)
circular_linked_list.push_end(2)
circular_linked_list.push_end(3)

# Prepending a node
circular_linked_list.push_front(0)

# Printing the circular linked list
circular_linked_list.print_list()

# Inserting a node after a specific node
circular_linked_list.push_after(1, 1.5)

# Printing the circular linked list after insertion
circular_linked_list.print_list()

# Deleting a node
circular_linked_list.delete_node(2)

# Printing the circular linked list after deletion
circular_linked_list.print_list()
