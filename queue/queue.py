class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        return len(self.items)


# Example Usage:
if __name__ == "__main__":
    # Create a queue
    my_queue = Queue()

    # Enqueue elements into the queue
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    # Print the queue
    print("Queue:", my_queue.items)

    # Get the front element
    print("Front element:", my_queue.front())

    # Dequeue elements from the queue
    dequeued_item = my_queue.dequeue()
    print("Dequeued item:", dequeued_item)
    print("Queue after dequeue:", my_queue.items)

    # Check if the queue is empty
    print("Is the queue empty?", my_queue.is_empty())

    # Get the size of the queue
    print("Size of the queue:", my_queue.size())
