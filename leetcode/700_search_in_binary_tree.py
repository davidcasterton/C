# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        subtree = None
        if root.left:
            subtree = self.searchBST(root.left, val)
            if subtree:
                return subtree
        if root.right:
            subtree = self.searchBST(root.right, val)
            if subtree:
                return subtree
        if root.val == val:
            return root

        return None
