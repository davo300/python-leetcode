from linkedList import Node, LinkedList  # remember imports only work in the same folder!!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = Node(0)
        dummy.next = head
        prev, curr = dummy, head
        
        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next
             
            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            
            # update ptrs
            prev = curr
            curr = nxtPair
        
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    # Create the first linked list
    ll = LinkedList()
    for val in [1]:
        ll.add_last(val)
    
    # Call mergeKLists with the list of Node objects
    result_head = s.swapPairs(ll.head)

    # Convert the result linked list back to a Python list for display
    result = []
    while result_head:
        result.append(result_head.element)  # .element if your Node class uses this
        result_head = result_head.next

    print("Result:", result)