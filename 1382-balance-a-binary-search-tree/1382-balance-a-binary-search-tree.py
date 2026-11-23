# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_vals = []

        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)

        def build_balanced(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(
                sorted_vals[mid],
                build_balanced(left, mid - 1),
                build_balanced(mid + 1, right),
            )

        inorder(root)
        return build_balanced(0, len(sorted_vals) - 1)
        