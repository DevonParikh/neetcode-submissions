# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        if curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                sorted_list = ListNode(curr1.val, None)
                curr1 = curr1.next
            else:
                sorted_list = ListNode(curr2.val, None)
                curr2 = curr2.next
            head = sorted_list
        elif curr1 is None and curr2 is None:
            return curr1
        elif curr1 is None:
            return curr2
        else:
            return curr1
        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                sorted_list.next = ListNode(curr2.val, None)
                curr2 = curr2.next
                sorted_list = sorted_list.next
            elif curr2 is None:
                sorted_list.next = ListNode(curr1.val, None)
                curr1 = curr1.next
                sorted_list = sorted_list.next
            elif curr1.val <= curr2.val:
                sorted_list.next = ListNode(curr1.val, None)
                curr1 = curr1.next
                sorted_list = sorted_list.next
            else:
                sorted_list.next = ListNode(curr2.val, None)
                curr2 = curr2.next
                sorted_list = sorted_list.next
        return head
