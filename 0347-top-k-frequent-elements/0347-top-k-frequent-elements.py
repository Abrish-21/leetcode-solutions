class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        res = []
        for i in nums:
            counts[i] = counts.get(i,0) +1
        temp = list()
        for i,v in counts.items():
            temp.append((v,i))
        temp = sorted(temp, reverse= True)
        for i,v in temp:
            res.append(v)
            
        return res[:k]
