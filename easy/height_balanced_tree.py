from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.find_height(root.left), self.find_height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        height_left = self.find_height(root.left)
        height_right = self.find_height(root.right)
        return abs(height_left - height_right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    # root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15), TreeNode(7)))  -> True

    # [3,9,20,null,null,15,7] -> True
    # root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)) )

    # [1,2,2,3,3,null,null,4,4] -> False
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))

    solution = Solution()
    print(solution.isBalanced(root))