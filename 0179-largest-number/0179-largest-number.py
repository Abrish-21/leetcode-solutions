class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string = []
        for num in nums:
            string.append(str(num))
        string.sort(key= lambda a: a* 10, reverse = True)
        result = "".join(string)
        return "0" if result[0]== str(0) else (str(result))

        