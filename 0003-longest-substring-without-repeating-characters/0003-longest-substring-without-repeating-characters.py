class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        start = 0
        if s == "":
            return 0
        max_length = 1
        for end in range(len(s)):
            curr = s[end]

            while curr in seen and seen[curr] >= start:
                start += 1

            max_length = max(max_length, end - start + 1)

            seen[curr] = end
        return max_length
          

            