class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 for base case
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop for ')'
                if not stack:
                    stack.append(i)  # Add base index for next valid sequence
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate max valid length
        
        return max_length
        