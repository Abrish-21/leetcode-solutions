class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)
        start = 0
        longest_s = 0
        for end in range(len(s)):
            curr_char = s[end]
            if curr_char in store and start <= store[curr_char]:
                while start <= store[curr_char]:
                    start += 1
            longest_s = max(longest_s, end - start + 1)
            store[curr_char] = end
        return longest_s
            
                
    