class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = {}
        for i  in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                p = nums[i] * nums[j]
                if p not in product:
                    product[p] = 1
                else:
                    product[p] +=1
        print(product)
        # bnow let's find hte number of tuples
        tuples = 0
        
        # Compute number of valid tuples
        for count in product.values():
            if count >= 2:
                tuples += (count * (count - 1) // 2) * 8  # Combination formula times 8

                
        return 0 if len(nums) < 4 else tuples

        