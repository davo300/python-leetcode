class ListNode:     # from leetcode definition
    '''Lightweight, nonpublic class for storing a singly linked node.'''
    __slots__ = 'element', 'next'  # streamline memory usage

    def __init__(self, e, next_node=None):
        self.element = e
        self.next = next_node

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, e):
        newest = ListNode(e)
        newest.next = self.head
        self.head = newest
        if self.size == 0:
            self.tail = newest  # If the list was empty, set tail as well
        self.size += 1

    def add_last(self, e):
        newest = ListNode(e)
        if self.head is None:  # List is empty
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            self.tail = newest
        self.size += 1

    def remove_first(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:  # If the list becomes empty, set tail to None
            self.tail = None

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        # If there's only one element in the list
        if self.size == 1:
            self.head = None
        else:
            current = self.head
            # Traverse the list until the second-to-last node O(n)
            while current.next and current.next.next:
                current = current.next
            current.next = None  # Remove the last node
        self.size -= 1

    def display(self):
        current = self.head
        while current:
            print(current.element, end=" -> ")
            current = current.next
        print("None")

        
    # ---------- Builder for Random Pointer List (Node) ----------
    @staticmethod
    def build_random_list(arr):
        """
        arr: list of [val, random_index] where random_index points into arr
        returns: head of Node-based linked list
        """
        if not arr:
            return None

        nodes = [Node(val) for val, _ in arr]

        # next pointers
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        # random pointers
        for i, (_, rand_index) in enumerate(arr):
            if rand_index is not None:
                nodes[i].random = nodes[rand_index]

        return nodes[0]  # head



# Example usage
if __name__ == "__main__":
    sll = LinkedList()
    sll.add_last(10)
    sll.add_last(20)
    sll.add_last(30)
    print("Original List:")
    sll.display()

    sll.remove_last()
    print("\nList after removing the last element:")
    sll.display()
