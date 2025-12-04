# 138. 

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from linkedList import ListNode, Node, LinkedList  # remember imports only work in the same folder!!
from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None } 

        cur = head

        while cur:      # create hashmap full of original node keys, with corresponding duplicate values
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head      # iterate through list again
        
        while cur:                  # wire up all the duplicate node values from the hashmap 
            copy = oldToCopy[cur]              # using the orgional list as a guide and .next and .random 
            copy.next = oldToCopy[cur.next]    # pointers to wire up the values.
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]  # returning the hashmap key of the orginal head returns the value of the duplicate head


if __name__ == "__main__":
    sol = Solution()
    arr = [[7,None],[13,0],[11,4],[10,2],[1,0]]

    head = LinkedList.build_random_list(arr)    # use the generated linkedList class
    ans = sol.copyRandomList(head)

    # Convert back to array for easy checking
    result, mapping = [], {}
    i, curr = 0, ans
    while curr:
        mapping[curr] = i
        curr = curr.next
        i += 1

    curr = ans
    while curr:
        result.append([curr.val, mapping.get(curr.random, None)])
        curr = curr.next

    print("Result:", result)