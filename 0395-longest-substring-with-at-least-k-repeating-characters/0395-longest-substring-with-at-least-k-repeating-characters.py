class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        # Step 1: Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Step 2: Find a character that appears less than k times
        for char in freq:
            if freq[char] < k:
                # Step 3: Split string at this character and check each part
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # Step 4: If no split is needed, return the length of the full string
        return len(s)
        