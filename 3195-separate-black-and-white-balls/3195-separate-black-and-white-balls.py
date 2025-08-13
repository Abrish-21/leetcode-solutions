class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        white_pos = 0
        for curr_pos, val in enumerate(s):
            if val == "0":
                swap += curr_pos - white_pos
                white_pos += 1
        return swap