from typing import List, Optional

# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        arr_len = len(nums)
        if arr_len == 0:
            return None
        elif arr_len == 1:
            return TreeNode(nums[0], None, None)
        else:
            mid = arr_len // 2
            return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))


def in_order_traversal(node: TreeNode):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=" ")
        in_order_traversal(node.right)

if __name__ == '__main__':
    solution = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = solution.sortedArrayToBST(nums)
    in_order_traversal(root)