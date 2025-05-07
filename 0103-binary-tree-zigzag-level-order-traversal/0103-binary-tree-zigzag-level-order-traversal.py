# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        level = 0
        _list = []
        while queue:
            if not root: return []
            current_level_node = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level_node.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            _list.append(current_level_node)
            if level %2 == 1:
                i, j = 0, len(current_level_node) -1 
                while i < j:
                    current_level_node[i], current_level_node[j]= (
                        current_level_node[j], current_level_node[i]
                    )
                    i += 1
                    j -= 1
            level +=1 
        return _list
                    
       



        