from linked_list import DoublyLinkedList


class Stack:
    def __init__(self) -> None:
        self.stack = DoublyLinkedList()
        self.length = 0

    def add(self, data):
        self.length += 1
        self.stack.add_to_tail(data)

    def remove(self):
        self.length -= 1
        return self.stack.remove_from_tail().data


if __name__ == '__main__':
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    print("length", s.length)

    print(s.remove())
    print(s.remove())
    print("length", s.length)
    print(s.remove())
    print("length", s.length)
