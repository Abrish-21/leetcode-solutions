class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = defaultdict(int)
        for i in range(len(s)):
            char = s[i]
            last_seen[char] = i

        part = 0
        partition = []
        while part < len(s):
            left = part 
            right = last_seen[s[part]]
            max_width = right
            while left <= right:
                max_width = max(max_width, last_seen[s[left]])
                left += 1
                right  = max_width
            partition.append(max_width - part + 1)
            part = max_width + 1
        return partition
        
        