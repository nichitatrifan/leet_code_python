from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == "__main__":
    # [3,9,20,null,null,15,7] -> 2
    # root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    # [2,null,3,null,4,null,5,null,6] -> 5
    root = TreeNode(2,None,TreeNode(3,None, TreeNode(4, None, TreeNode(5,None,TreeNode(6)))))

    solution = Solution()
    print(solution.minDepth(root))