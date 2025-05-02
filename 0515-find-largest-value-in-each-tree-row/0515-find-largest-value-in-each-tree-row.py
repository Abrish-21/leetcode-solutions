# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_val  = defaultdict(lambda: float('-inf'))
        def dfs(node, level):
            if not node: return 
            max_val[level] = max(max_val[level], node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return [val for val in max_val.values()]





        

        