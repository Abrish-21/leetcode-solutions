class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:k-1])

        start = 0
        output = []
        for end in range(k-1, len(s)):
            curr = s[end]
            s_counter[curr] += 1

            if s_counter == p_counter:
                output.append(start)

            # removing the left most    
            s_counter[s[start]] -= 1
            if s_counter[s[start]] == 0:
                del s_counter[s[start]]
            start += 1

        return output


        