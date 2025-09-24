class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count  = defaultdict(int)
        rabbit = 0
        for ans in answers:
            if ans not in count:
                count[ans] = 1
            else:
                count[ans] += 1
        print(count)
        for key in count:
            x  = (key + 1) * math.ceil(count[key] / (key + 1))
            rabbit +=  x 
        return rabbit


            
            
                

        