class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Convert the list to a set for O(1) average time lookups
        num_set = set(nums)
        
        result = []
        n = len(nums)
        
        # Iterate from 1 to n and check for missing numbers
        for i in range(1, n + 1):
            if i not in num_set:
                result.append(i)
                
        return result