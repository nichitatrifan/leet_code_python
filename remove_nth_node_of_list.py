#Definition for singly-linked list.
from sympy import false


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head:ListNode, n: int) -> ListNode:
        size = 0
        cursor = head
        removed = False

        while cursor != None:
            size+=1
            cursor = cursor.next

        if size == n:
            head = head.next
        else:
            cursor = head
            while not removed and cursor != None:
                size-=1
                if size == n:
                    cursor.next = cursor.next.next
                    removed = True
                cursor = cursor.next
        return head
                

def print_list(head:ListNode):
    cursor = head
    while(cursor != None):
        print(cursor.val, end=' ')
        cursor = cursor.next

if __name__ == '__main__':
    head = ListNode(1, None)
    cursor = head
    for n in range(2,11):
        cursor.next = ListNode(n,None)
        cursor = cursor.next
    
    print_list(head)

    n = int(input('Enter the n: '))
    solution = Solution()
    head = solution.removeNthFromEnd(head, n)
    print('--------------')
    print_list(head)
