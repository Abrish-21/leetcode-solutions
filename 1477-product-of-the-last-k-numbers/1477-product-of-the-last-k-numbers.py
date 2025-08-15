class ProductOfNumbers(object):

    def __init__(self):
        self.size = 0
        self.PrefixSumProduct = [1]
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.PrefixSumProduct = [1]
            self.size = 0
        else:
            self.PrefixSumProduct.append(self.PrefixSumProduct[self.size] * num)
            self.size += 1
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > self.size:
            return 0
        return self.PrefixSumProduct[self.size] / self.PrefixSumProduct[self.size- k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)