from typing import Optional, List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack : List[TreeNode] = []
        result_list : List[int] = []

        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                current = stack.pop()
                result_list.append(current.val)
                current = current.right
            else:
                break

        return result_list

    def inorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)

        return

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10, None, None)
    root.left = TreeNode(5, None, None)
    root.right = TreeNode(15)

    print(solution.inorderTraversal(root))