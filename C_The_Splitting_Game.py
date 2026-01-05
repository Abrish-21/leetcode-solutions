from collections import defaultdict, Counter
t = int(input())
for _ in range(t):
    n = int(input())
    word = str(input())
    max_unique = 0
    left_counter = Counter()
    right_counter = Counter(word)

    for ch in word:
        left_counter[ch] += 1
        right_counter[ch] -= 1

        if right_counter[ch] == 0:
            del right_counter[ch]
        max_lenght = len(left_counter) + len(right_counter)
        max_unique = max(max_unique, max_lenght)
    print(max_unique)