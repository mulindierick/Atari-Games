from unittest import result
from random import randint

from time import perf_counter
from matplotlib import pyplot as plt
import numpy as np


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
        if self.head:
            #point prev of curr head to added node
            self.head.prev = new_node 
        else:
            self.tail = new_node  

        #shift the head to the added node
        self.head = new_node 
        
    def __str__(self) -> str:
        result = ''
        curr = self.head
        while curr:
            result += str(curr.data) + " "
            curr = curr.next
        return result


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
        
    def insertion_sort(self):

        forward = self.head.next

        while forward:
            curr = forward.data
            back = forward.prev

            while back and back.data > curr:
                back.next.data, back.data = back.data, back.next.data
                back = back.prev
            back = forward.prev
            forward = forward.next
        
    def merge_sort_helper(self, head):

        def merge(dll1, dll2):
            
            dummy = Node(None, None, None)
            tail = dummy
            while dll1 and dll2:
                if dll1.data < dll2.data:
                    tail.next = dll1
                    dll1 = dll1.next
                else:
                    tail.next = dll2
                    dll2 = dll2.next
                tail = tail.next
            while dll1:
                tail.next = dll1
                dll1 = dll1.next
                tail = tail.next
            while dll2:
                tail.next = dll2
                dll2 = dll2.next
                tail = tail.next
            return dummy.next

        def get_mid_node(head):
            left = head
            second = head.next
            while second:
                second = second.next
                if second:
                    left = left.next
                    second = second.next
            return left

        # megersort 
        if not head or not head.next:
            return head

        left = head
        temp = get_mid_node(head)

        right = temp.next
        temp.next = None
        right.prev = None
        
        dll1 = self.merge_sort_helper(left)
        dll2 = self.merge_sort_helper(right)
        return merge(dll1, dll2)

    def merge_sort(self, dll):
        h = self.merge_sort_helper(dll.head)
        dll.head = h
        return dll

      
    def quick_sort(self, head, tail):

        def get_pivot(head, tail):

            # make tail the pivot 
            pivot = tail
            
            #left pointer start at none - prev of head
            left = head.prev 

            #right pointer starts at head
            right = head

            # keep looping until right point == to th tail
            while right != tail:

                # if the data of right point is less than or equal to data of tail
                if right.data <= pivot.data:

                    # move left pointer forward 
                    if left is None:
                        left = head
                    else:
                        left = left.next
                    
                    # swap left point data with right pointer data
                    left.data, right.data = right.data, left.data

                # move right pointer forward
                right = right.next

            # incase list is sorted in decending order
            # move left pointer forward 
            if left is None:
                left = head
            else:
                left = left.next
            
            # finall swap the pivot with left pointer
            left.data, pivot.data = pivot.data, left.data
            return left

        # reversively call quicksort of get_pivot untl tail == head
        if tail and head != tail.next:
            pivot = get_pivot(head, tail)
            self.quick_sort(head, pivot.prev)
            self.quick_sort(pivot.next, tail)
          

if __name__ == '__main__':

    list_dll_insert = []
    list_dll_merge = []
    list_dll_quick = []

    list_dll_len = []
    list_dll_time_insert = []
    list_dll_time_merge = []
    list_dll_time_quick = []

    for i in range(1, 100):
        dll = DoublyLinkedList()
        for i in range(0, 10*i):
            dl = randint(0, 200)
            dll.add_to_head(dl)

        list_dll_insert.append(dll)
        list_dll_merge.append(dll)
        list_dll_quick.append(dll)

        list_dll_len.append(10*i)
        dll = DoublyLinkedList()
        
    for d in list_dll_insert:

        # insertion sort time
        start_insert = perf_counter()
        d.insertion_sort()
        end_insert = perf_counter()
        time_elapsed_insert = (end_insert - start_insert)
        list_dll_time_insert.append(time_elapsed_insert)

        # merge sort times 
        start_merge = perf_counter()
        d.merge_sort(d)
        end_merge = perf_counter()
        time_elapsed_merge = (end_merge - start_merge)
        list_dll_time_merge.append(time_elapsed_merge)

        # quick sort times 

        start_quick = perf_counter()
        d.quick_sort(d.head, d.tail)
        end_quick = perf_counter()
        time_elapsed_quick = (end_quick - start_quick)
        list_dll_time_quick.append(time_elapsed_quick)

    # plot the times of each sort
    plt.plot(list_dll_len, list_dll_time_insert, label='Insertion sort')
    plt.plot(list_dll_len, list_dll_time_merge, label='Merge sort')
    plt.plot(list_dll_len, list_dll_time_quick, label='Quick sort')
    plt.legend()
    plt.show()