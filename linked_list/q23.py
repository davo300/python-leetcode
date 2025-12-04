from linkedList import Node, LinkedList  # remember imports only work in the same folder!!

# this algorithm directly builds off of q21 mergeTwoLists() function

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists or len(lists) == 0:    # if lists does not exist or is empty
            return None
        
        while len(lists) > 1:       
            mergedLists = []

            for i in range(0, len(lists), 2):   # range(start, stop, step) steps by 2 each iteration
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
        
    def mergeList(self, l1, l2):    # merge 2 lists algorithm q21 !!!
        #todo
        dummy = Node(0)    
        tail = dummy

        while l1 and l2:
            if l1.element < l2.element:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # Append the rest if one list is longer than the other
        if l1:
            tail.next = l1      
        else:
            tail.next = l2
        
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    # Create the first linked list
    ll1 = LinkedList()
    for val in [1, 4, 5]:
        ll1.add_last(val)

    # Create the second linked list
    ll2 = LinkedList()
    for val in [1, 3, 4]:
        ll2.add_last(val)

    # Create the third linked list
    ll3 = LinkedList()
    for val in [2, 6]:
        ll3.add_last(val)

    # Create the list of heads of the linked lists
    lists = [ll1.head, ll2.head, ll3.head]  # use .head to get the first node of each LinkedList
    
    # Call mergeKLists with the list of Node objects
    result_head = s.mergeKLists(lists)

    # Convert the result linked list back to a Python list for display
    result = []
    while result_head:
        result.append(result_head.element)  # .element if your Node class uses this
        result_head = result_head.next

    print("Result:", result)
