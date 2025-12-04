# 206. Reorder Linked List

# Difficulty: Medium

# Topics: Linked List, Two Pointers, Stack, Recursion

from linkedList import ListNode, LinkedList  # remember imports only work in the same folder!!
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle 
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None

        while second:   # this loop successfully reverses the nodes in the second half
            tmp = second.next   
            second.next = prev
            prev = second
            second = tmp    # eventually, second == None == null
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


if __name__ == "__main__":
    sol = Solution()

    # Create the linked list
    ll = LinkedList()
    for val in [1,2,3,4,5]:
        ll.add_last(val)
    
    sol.reorderList(ll.head)    # modify ll in place

    # Convert the result linked list back to a Python list for display
    result = []
    curr = ll.head   # start from the head node
    while curr:
        result.append(curr.element)  # or curr.val depending on your Node definition
        curr = curr.next

    print("Result:", result)


