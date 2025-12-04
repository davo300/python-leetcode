# 206. Reverse Linked List

# Difficulty: Easy

# Topics: Linked List, Recursion

from linkedList import ListNode, LinkedList  # remember imports only work in the same folder!!
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":
    sol = Solution()

    # Create the first linked list
    ll = LinkedList()
    for val in [1,2,3,4,5]:
        ll.add_last(val)
    
    result_head = sol.reverseList(ll.head)

    # Convert the result linked list back to a Python list for display
    result = []
    while result_head:
        result.append(result_head.element)  # .element if your Node class uses this
        result_head = result_head.next

    print("Result:", result)    # output [4,5,1,2,3]

