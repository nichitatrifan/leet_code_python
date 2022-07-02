# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_str1 = ''
        num_str2 = ''

        while (l1 != None) or (l2 != None):
            if l1 != None:
                num_str1 += str(l1.val)
                l1 = l1.next
            if l2 != None:
                num_str2 += str(l2.val)
                l2 = l2.next

        result_num = int(num_str1[::-1]) + int(num_str2[::-1])
        result_str = str(result_num)

        head_result = ListNode(result_str[::-1][0], None)
        pointer = head_result

        for i in range(1,len(result_str)):
            pointer.next = ListNode(result_str[::-1][i], None)
            pointer = pointer.next

        return head_result


if __name__ == '__main__':
    solution = Solution()

    pointer_l1 = ListNode(9, None)
    l1 = pointer_l1
    for i in range(6):
        pointer_l1.next = ListNode(9, None)
        pointer_l1 = pointer_l1.next

    pointer_l2 = ListNode(9, None)
    l2 = pointer_l2
    for i in range(3):
        pointer_l2.next = ListNode(9, None)
        pointer_l2 = pointer_l2.next

    result_list = solution.addTwoNumbers(l1,l2)
    while result_list != None:
        print(result_list.val, end='')
        result_list = result_list.next
