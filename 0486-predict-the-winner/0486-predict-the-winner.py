class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)
        def canWin(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if  i == j:
                return nums[i]
            if i > j:
                return 0
            pick_left = nums[i] - canWin(i + 1, j)
            pick_right = nums[j] - canWin(i, j-1)
            result = max(pick_left, pick_right)
            memo[(i,j)] = result
            return memo[(i,j)]
        return canWin(0, n - 1) >= 0
            


        