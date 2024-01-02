#Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    #push at front
    def push_front(self, data):
        #1. turn data into Node so that we can use it in linked list
        new_data = Node(data)
        #2. new_data -> self.head
        new_data.next = self.head
        #3. we are adding new_data at front of the linked list, so it must be head node
        self.head = new_data

    def push_after(self, prev, data):
        new_node = Node(data)#1. Turning raw data into Node
        current_node = self.head #2. will be useful when finding the previous node
        while current_node: #3. looping through the linked list
            if current_node.data == prev: #4. we found the previous data
                new_node.next = current_node.next #5. connecting new_node.next ad current_node.next
                current_node.next = new_node #6. current_node will point to new_node
                return #terminate the function
            current_node = current_node.next #7. if not found, go to next data in linked list and loop again
        print(f"Node with data {prev} not found in the list.")

    def push_end(self, data):
        new_node = Node(data)#1. Turning raw data into node
        if self.head is None:#if self.head is None, there is no data in linked list
            self.head = new_node
            return
        '''
        the goal of this function is to find a last node and point last.next to new_node
        the last node of the linked list has no next, which is None.
        while loop stop when it found a None data type.
        '''
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current_node = self.head

        # If the node to be deleted is the head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Search for the node to be deleted, keeping track of the previous node
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        # If the node is not present
        if current_node is None:
            return

        # Unlink the node from the linked list
        prev_node.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

linked = Linked_List()
linked.push_front(3)
linked.push_front(2)
linked.push_front(1)
linked.push_after(1, 1.5)
linked.push_end(5)
linked.print_list()
linked.delete_node(5)
linked.print_list()