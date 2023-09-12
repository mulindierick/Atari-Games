from binary_heap import MinHeap


class PriorityQueue:
    def __init__(self) -> None:
        self.priority_queue = MinHeap()

    def enqueue(self, node, priority):
        self.priority_queue.add_node(node, priority)

    def dequeue(self):
        return self.priority_queue.remove_min()


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(232, 78)
    pq.enqueue(2, 890)
    pq.enqueue(232, 89)
    pq.enqueue(443, 588)
    pq.enqueue(23, 808)
    pq.enqueue(21, 4)

    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq.priority_queue.min_heap)

    # print(pq.dequeue())
