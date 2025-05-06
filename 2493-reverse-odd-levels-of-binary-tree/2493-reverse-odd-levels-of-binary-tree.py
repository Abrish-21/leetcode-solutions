from collections import deque
from typing import Optional

# Assuming TreeNode is defined like this:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            current_level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse values at odd levels
            if level % 2 == 1:
                i, j = 0, len(current_level_nodes) - 1
                while i < j:
                    current_level_nodes[i].val, current_level_nodes[j].val = (
                        current_level_nodes[j].val,
                        current_level_nodes[i].val,
                    )
                    i += 1
                    j -= 1

            level += 1

        return root
