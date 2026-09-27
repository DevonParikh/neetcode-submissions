# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_map = {} #mapping val : next
        curr = head
        if curr is None:
            return False
            
        while curr.next:
            if curr.val in my_map:
                if curr.next in my_map[curr.val]:
                    return True
                else:
                    my_map[curr.val].append(curr.next)
            else:
                my_map[curr.val] = [curr.next]
            curr = curr.next
        return False