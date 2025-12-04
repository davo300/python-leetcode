# 61. Rotate List
# Topics: Linked List, Two pointers

from linkedList import ListNode, LinkedList  # remember imports only work in the same folder!!
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:      # if num rotations is equal to length means LL doesn't change
            return head
        
        # Move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):     # 5 - 2 - 1 = 2
            cur = cur.next      # make the rotation
        newHead = cur.next  
        cur.next = None     # set last element to point to null
        tail.next = head    # connect the initial tail element to point to the inital start of list
        return newHead      # after rotation has been made and pointers adjusted, our list has been rotated


if __name__ == "__main__":
    s = Solution()

    # Create the first linked list
    ll = LinkedList()
    for val in [1,2,3,4,5]:
        ll.add_last(val)
    
    # Call rotateRight() with the list of Node objects
    k = 2
    result_head = s.rotateRight(ll.head, k)

    # Convert the result linked list back to a Python list for display
    result = []
    while result_head:
        result.append(result_head.element)  # .element if your Node class uses this
        result_head = result_head.next

    print("Result:", result)    # output [4,5,1,2,3]