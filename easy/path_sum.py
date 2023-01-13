from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            targetSum -= root.val

            if targetSum == 0 and root.left and root.right is None:
                return False or self.hasPathSum(root.left, targetSum)
            elif targetSum == 0 and root.right and root.left is None:
                return False or self.hasPathSum(root.right, targetSum)
            elif targetSum == 0 and root.left is None and root.right is None:
                 return True
            else:
                return False or self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        else:
            return False


if __name__ == "__main__":
    # [1,2,3]

    # root = [1,2]
    # target_sum = 1 -> False
    # root = TreeNode(1,TreeNode(2))
    # target_sum = 1

    # root = [1,-2,-3,1,3,-2,null,-1]
    # target_sum = -1                    -> True
    root = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
    target_sum = -1

    solution = Solution()
    print(solution.hasPathSum(root, target_sum))