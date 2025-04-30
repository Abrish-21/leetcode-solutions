class KthLargest:

    def __init__(self, k: int, nums: List[int]):
            self.heap = []
            self.k = k
            self.nums = nums
            nums.sort(reverse = True)
            for i in range(min(k, len(nums))):
                heappush(self.heap, nums[i])

            
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:

            heappop(self.heap)
        return self.heap[0]
       
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)