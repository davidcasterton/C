# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode], ) -> List[int]:
        out = []
        # if root:
        #     if root.right:
        #         out = self.rightSideView(root.right)
        #     out.insert(0, root.val)

        def bfs(root, out, height):
            if not root:
                return

            if len(out) == height:
                out.append(root.val)
            else:
                out[height] = root.val

            bfs(root.left, out, height+1)
            bfs(root.right, out, height+1)

        bfs(root, out, 0)

        return out
