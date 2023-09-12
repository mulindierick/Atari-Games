class Node:
    def __init__(self, prev, next, data) -> None:
        self.prev = prev
        self.next = next
        self.data = data


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(None, self.head, data)
        no_head = Node(None, None, data)
        if self.head:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = no_head
            self.tail = no_head

    def add_to_tail(self, data):
        new_node = Node(self.tail, None, data)
        head_node = Node(None, None, data)
        if (self.tail):
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = head_node
            self.tail = head_node
            
    def __str__(self) -> str:
        result = ''
        curr = self.head
        while curr:
            result += str(curr.data) + " "
            curr = curr.next
        return result

    def remove_from_head(self):
        remove = self.head
        if(self.head.next):
            self.head = remove.next
            remove.next.prev = None
            remove.next = None
        else:
            self.head = None
            self.tail = None
        return remove
    def remove_from_tail(self):
        remove = self.tail
        if(self.tail.prev):
            self.tail = remove.prev
            remove.prev.next = None
            remove.prev = None
        else:
            self.head = None
            self.tail = None
        return remove
            

    def search_for_node(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return False

    def delete(self, data):
        # find node to remove
        node = self.search_for_node(data)

        if node:
            # if node is the only one
            if self.head == node and self.tail == node:
                self.head = None
                self.tail = None

            # if node is the tail
            elif node == self.tail:
                self.tail = node.prev
                node.prev.next = None
                node.prev = None

            # if node is the head
            elif node == self.head:
                self.head = node.next
                node.next.prev = None
                node.next = None
            else:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                node.prev = None
                node.next = None


if __name__ == '__main__':
    dll = DoublyLinkedList()
 

    dll.add_to_tail(3)
    dll.add_to_tail(4)
    dll.add_to_tail(5)


    print(dll)
    dll.remove_from_head()
    dll.remove_from_tail()
    dll.remove_from_tail()
    dll.add_to_head(90)
    # dll.remove_from_head()
    print("here", dll)
   

