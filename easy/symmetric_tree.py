from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root, root)

    def isMirror(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False

        return (node1.val == node2.val) and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    solution = Solution()
    print(solution.isSymmetric(root))