# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def dfs(node):
            nonlocal max_diff
            max_val = node.val
            min_val = node.val
            if node.left:
                left_min, left_max = dfs(node.left)
                max_val = max(max_val, left_max)
                min_val = min(min_val, left_min)
            if node.right:
                right_min, right_max = dfs(node.right)
                max_val = max(max_val, right_max)
                min_val = min(min_val, right_min)
            max_diff= max(max_diff, abs(max_val- node.val), abs(min_val - node.val))
            return [min_val, max_val]
        dfs(root)
        return max_diff
        
            
            
            



        # def dfs(node):
        #     if not node: return 
        #     min_val  = float('inf')
        #     max_val = 0
        #     curr_level = []
        #     if node.left:
        #         curr_level.append(node.left.val)
        #     if node.right:
        #         curr_level.append(node.right.val)
        #     max_val = max()
        #     min_val = min(min_val, min(curr_level))
        #     max_diff = max(abs(max_val - node.val),  abs(min_val - node.val))
        #     print(max_val, min_val)
        #     dfs(node.left)
        #     dfs(node.right)
        #     return max_diff
        # return dfs(root)
        
        
            


        