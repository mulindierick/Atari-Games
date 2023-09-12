from linked_list import DoublyLinkedList


class Queue:
    def __init__(self) -> None:
        self.queue = DoublyLinkedList()
        self.length = 0

    def enqueue(self, data):
        self.queue.add_to_tail(data)
        self.length += 1

    def dequeue(self):
        self.length -= 1
        return self.queue.remove_from_head().data


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("length", q.length)

    print(q.dequeue())
    print("length", q.length)
    print(q.dequeue())
    print(q.dequeue())

    print(q.length)
