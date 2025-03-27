class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        target  = collections.Counter(p)
        window = collections.Counter(s[: len(p)-1])
        for i in range(len(p)-1, len(s)):
            current_char = s[i]
            window[current_char] += 1
            if window == target:
                result.append(i- len(p) + 1)
            window[s[i-len(p) + 1]] -= 1
            if window[s[i-len(p) + 1]] == 0:
                del window[s[i-len(p) + 1]]
        return result
        