# Definition for singly-linked list.
from typing import List


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1


if __name__ == '__main__':
    list1 = ListNode(1, None)
    list2 = ListNode(2, None)
    list1.next = ListNode(3, None)
    list2.next = ListNode(5, None)
    solution = Solution()
    sorted_list = solution.mergeTwoLists(list1, list2)

    cursor = sorted_list
    while cursor:
        print(cursor.val, end=' -> ')
        cursor = cursor.next
