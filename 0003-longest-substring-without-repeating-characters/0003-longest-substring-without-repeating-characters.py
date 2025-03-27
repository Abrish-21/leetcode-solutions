class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start  = 0
        longest_s = 0
        seen  = defaultdict(int)
        for end in range(len(s)):
            # //add the the frquency to the map
            curr_char = s[end]
            if curr_char in seen and seen[curr_char] >= start:
                start = seen[curr_char] + 1

            seen[curr_char] = end

            # now check compute the longest  length
            longest_s = max(longest_s, end - start + 1)
        return longest_s
            



        