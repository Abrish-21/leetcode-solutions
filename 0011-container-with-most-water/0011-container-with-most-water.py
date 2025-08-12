class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water  = []
        left_p = 0
        right_p = len(height) -1 
        while left_p < right_p:
            if height[left_p] < height[right_p]:
                most_water.append(height[left_p] * (right_p - left_p))
                left_p += 1
            else:
                most_water.append(height[right_p] *  (right_p - left_p))
                right_p -= 1
        return max(most_water)
        