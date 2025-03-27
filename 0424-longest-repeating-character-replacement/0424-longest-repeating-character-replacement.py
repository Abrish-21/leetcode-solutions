class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_length = 0
        start = 0
        freq_count = defaultdict(int)
        for i in range(len(s)):
            curr_char = s[i]
            freq_count[curr_char]  += 1
            max_freq = max(max_freq, freq_count[curr_char])
            # now check for the limti is exceeded
            window_size = i - start + 1
            if window_size - max_freq > k:
                # store the maximum length
                freq_count[s[start]] -= 1
                if freq_count[s[start]] == 0:
                    del freq_count[s[start]]
                start +=1
            max_length = max(max_length, i - start + 1)
        return max_length

        