from collections import Counter

n = int(input())
for _ in range(n):
    s = str(input())
    t = str(input())
    p = str(input())
    freq_s = Counter(s)
    freq_t = Counter(t)
    freq_p = Counter(p)
    def convert():
        # step 1: check if s is subsequence of t, if not return NO
        def sequence():
            order = 0
            for ch in t:
                if order < len(s)  and s[order] == ch:
                    order += 1
            return order == len(s)
        valid = True
        if sequence():
            for  char in freq_t:
                if freq_s[char] + freq_p[char] < freq_t[char]:
                    return "NO"
            return "YES"
           
        else:
            return "NO"
    print(convert())
