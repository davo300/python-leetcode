# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from Python.leetcode.linked_list.linkedList import Node, LinkedList  # remember imports only work in the same folder!!

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def listNodeToList(node):
            result = []
            while node:
                result.append(node.element)         # append used for arrays
                node = node.next
            return result

        def listToListNode(a):
            dummy = Node(0)                         # intialize with dummy element
            current = dummy
            for val in a:
                current.next = Node(val)
                current = current.next
            return dummy.next



        # Main Logic
        a1 = listNodeToList(l1)
        a2 = listNodeToList(l2)
        r1 = a1[::-1]                               # Reverse Array
        r2 = a2[::-1]                               # Reverse Array
        num1 = int(''.join(map(str, r1)))  
        num2 = int(''.join(map(str, r2))) 
        sum = num1 + num2
        sumArray = list(map(int, str(sum)))  
        a3 = sumArray[::-1]                         # Reverse Array
        l3 = listToListNode(a3)         
        return l3

def main():
# Create two linked lists: 342 + 465 = 807
    ll1 = LinkedList()
    for val in [2, 4, 9]:
        ll1.add_last(val)       # add last used for linked lists

    ll2 = LinkedList()
    for val in [5, 6, 4, 9]:
        ll2.add_last(val)       # add last used for linked lists

    sol = Solution()
    result_head = sol.addTwoNumbers(ll1.head, ll2.head)

    # Convert result back to list for display
    result = []
    while result_head:
        result.append(result_head.element)      # append used for arrays
        result_head = result_head.next

    print("Result:", result)  # Should print [7, 0, 8]
    


if __name__ == "__main__":
    main()