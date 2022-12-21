from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree_recursion(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q:
            return False
        if p and q is None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree_recursion(p.right, q.right) and self.isSameTree_recursion(p.left, q.left)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q:
            return False
        if p and q is None:
            return False

        # p_stack : List[TreeNode] = []
        # q_stack : List[TreeNode] = []
        stack : List[tuple(TreeNode, TreeNode)] = []

        p_current = p
        q_current = q

        same = True
        while same:
            if p_current and q_current:
                # p_stack.append(p_current)
                # q_stack.append(q_current)
                stack.append((p_current, q_current))
                p_current = p_current.left
                q_current = q_current.left
            elif p_current and q_current is None:
                same = False
            elif p_current is None and q_current:
                same = False
            #elif len(p_stack) > 0 and len(q_stack) > 0:
            elif len(stack) > 0:
                # p_current = p_stack.pop()
                # q_current = q_stack.pop()
                p_current, q_current = stack.pop()
                if p_current.val != q_current.val:
                    same = False
                p_current = p_current.right
                q_current = q_current.right
            else:
                break

        return same

if __name__ == '__main__':
    pass