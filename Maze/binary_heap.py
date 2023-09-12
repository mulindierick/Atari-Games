class MinHeap:
    def __init__(self) -> None:
        self.min_heap = []

    def get_left_child_index(self, parent_index):
        return (parent_index * 2) + 1

    def get_right_child_index(self, parent_index):
        return (parent_index * 2) + 2

    def get_parent_index(self, child_index):
        return (child_index-1)//2

    def has_left_child(self, index): return self.get_left_child_index(
        index) < len(self.min_heap)
    def has_right_child(self, index): return self.get_right_child_index(
        index) < len(self.min_heap)

    def has_parent(self, index): return self.get_parent_index(index) >= 0

    def get_left_child(
        self, index): return self.min_heap[self.get_left_child_index(index)]

    def get_right_child(
        self, index): return self.min_heap[self.get_right_child_index(index)]

    def get_parent(
        self, index): return self.min_heap[self.get_parent_index(index)]

    def swap(self, index1, index2):
        self.min_heap[index1], self.min_heap[index2] = self.min_heap[index2], self.min_heap[index1]

    def remove_min(self):
        if len(self.min_heap) == 1:
            return self.min_heap.pop()
        mn = self.min_heap.pop(0)
        self.min_heap.insert(0, self.min_heap[len(self.min_heap)-1])
        self.min_heap.pop()
        self.heapify_down()

        return mn

    def add_node(self, node, val):
        self.min_heap.append({"node": node, "val": val})
        self.heapify_up()

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index)["val"] < self.get_left_child(index)["val"]:
                smaller_index = self.get_right_child_index(index)
            if self.min_heap[index]["val"] < self.min_heap[smaller_index]["val"]:
                break
            else:
                self.swap(index, smaller_index)
            index = smaller_index

    def heapify_up(self):
        index = len(self.min_heap) - 1
        while (self.has_parent(index) and self.get_parent(index)["val"] > self.min_heap[index]["val"]):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def min_heap_len(self):
        return len(self.min_heap)


if __name__ == '__main__':

    bh = MinHeap()
    bh.add_node(33, 15)
    bh.add_node(34, 2)
    bh.add_node(35, 7)
    bh.add_node(36, 30)
    bh.add_node(37, 6)
    # bh.add_node(38, 6)
    # bh.add_node(39, 7)
    # bh.add_node(40, 8)
    print(bh.remove_min())
    print(bh.min_heap)

    # for i in range(bh.min_heap_len()):
    #     print(bh.remove_min())

    # print(bh.min_heap_len())
