from linkedList import Node, LinkedList  # remember imports only work in the same folder!!

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = Node(0)
        tail = dummy        # tail gets initalized to a dummy node with element value of 0 and pointer to None

        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.element < current2.element:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next
        
        # Append the rest if one list is longer than the other
        if current1:
            tail.next = current1      
        else:
            tail.next = current2
        
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    # Create the linked list:
    ll1 = LinkedList()
    for val in [1,2,4]:
        ll1.add_last(val)       # add last used for linked list
    # Create the linked list:
    ll2 = LinkedList()
    for val in [1,3,4]:
        ll2.add_last(val)       # add last used for linked list
    result_head = s.mergeTwoLists(ll1.head, ll2.head)

    # Convert result back to list for display
    result = []
    while result_head:
        result.append(result_head.element)      # append used for arr1ays
        result_head = result_head.next

    print("Result:", result)  