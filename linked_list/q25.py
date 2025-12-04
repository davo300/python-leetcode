from linkedList import ListNode, LinkedList  # remember imports only work in the same folder!!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next 

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
   


if __name__ == "__main__":
    s = Solution()

    # Create the first linked list
    ll = LinkedList()
    for val in [1,2,3,4,5]:
        ll.add_last(val)
    
    # Call reverseKGroup with the list of Node objects
    k = 2
    result_head = s.reverseKGroup(ll.head, k)

    # Convert the result linked list back to a Python list for display
    result = []
    while result_head:
        result.append(result_head.element)  # .element if your Node class uses this
        result_head = result_head.next

    print("Result:", result)