# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head:ListNode):
    while head != None:
        print(f"{head.val}->", end="")
        head = head.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        repeats : dict[int:int] = {}

        current : ListNode = head
        previous : ListNode = None

        while current != None:
            # saving the repeats
            if current.val not in repeats:
                repeats[current.val] = 0
            else:
                repeats[current.val] += 1

            # checking if we need to remove the node
            if current.val in repeats and repeats[current.val] > 0:
                repeats[current.val] -= 1
                current = current.next
                previous.next = current
            else:
                if previous != None:
                    current = current.next
                    previous = previous.next
                else:
                    previous = current
                    current = current.next
        return head

if __name__ == '__main__':
    head : ListNode = ListNode(1, None)
    currernt : ListNode = head
    for i in range(1,5):
        currernt.next = ListNode(i, None)
        currernt = currernt.next

    node1 = ListNode(1, ListNode(1, ListNode(2,None)))
    print_list(node1)
    solution = Solution()
    solution.deleteDuplicates(node1)
    print()
    print_list(node1)