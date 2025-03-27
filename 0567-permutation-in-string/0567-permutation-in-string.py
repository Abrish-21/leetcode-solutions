class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        window = collections.Counter(s2[:len(s1) - 1])
        start = 0
        for end in range(len(s1)-1, len(s2)):
            window[s2[end]]+= 1
            if window == target:
                return True
            else:
                window[s2[start]] -= 1
                if window[s2[start]] == 0:
                    del window[s2[start]]
                start += 1
        return False
        