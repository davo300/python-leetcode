from linkedList import Node, LinkedList  # remember imports only work in the same folder!!

# this solution uses the two pointer technique

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = Node(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    # Create the linked list:
    ll = LinkedList()
    for val in [1]:
        ll.add_last(val)       # add last used for linked list
    n = 1
    result_head = s.removeNthFromEnd(ll.head, n)

    # Convert result back to list for display
    result = []
    while result_head:
        result.append(result_head.element)      # append used for arr1ays
        result_head = result_head.next

    print("Result:", result)  