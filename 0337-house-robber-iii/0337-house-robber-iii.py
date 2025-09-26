# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)
        def dp(root):
            if root in memo:
                return memo[root]
            if root == None:
                return 0
            val = 0
            if root.left:
                val += dp(root.left.left) + dp(root.left.right)
            if root.right:
                val += dp(root.right.left) + dp(root.right.right)
            include = val + root.val
            exclude = dp(root.left) + dp(root.right)
            memo[root] =  max(include, exclude)
            return memo[root]
        return dp(root)

        