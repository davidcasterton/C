# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def sum_levels(root, levels, level):
            if not root:
                return

            try:
                levels[level] += root.val
            except:
                levels[level] = root.val

            # print(f'{level=} {levels=} {root.val}')

            if root.left:
                levels = sum_levels(root.left, levels, level+1)
            if root.right:
                levels = sum_levels(root.right, levels, level+1)
            return levels


        levels = {}
        level = 1
        sum_levels(root, levels, level)

        level_with_max_sum = 0
        max_level_sum = -float('inf')
        for k, v in levels.items():
            if v > max_level_sum:
                # print(f'{k=} {v=} {max_level_sum=} {level_with_max_sum=}')
                level_with_max_sum = k
                max_level_sum = v
        return level_with_max_sum
