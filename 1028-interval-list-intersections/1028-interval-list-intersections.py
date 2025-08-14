class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f = 0
        s = 0
        output = []
        while f< len(firstList) and s < len(secondList):
            if secondList[s][0] <= firstList[f][1] and secondList[s][1] >= firstList[f][1]:
                output.append([max(firstList[f][0], secondList[s][0]), min(firstList[f][1], secondList[s][1])])
                if firstList[f][1] < secondList[s][1]:
                    f += 1
                elif firstList[f][1] > secondList[s][1]:
                    s += 1
                else:
                    s +=1
                    f += 1
            elif firstList[f][0] <= secondList[s][1] and firstList[f][1] >=  secondList[s][1]:
                output.append([max(firstList[f][0], secondList[s][0]), min(firstList[f][1], secondList[s][1])])
                if firstList[f][1] < secondList[s][1]:
                    f += 1
                elif firstList[f][1] > secondList[s][1]:
                    s += 1
                else:
                    s +=1
                    f += 1
            elif firstList[f][1] < secondList[s][0]:
                f += 1
            else:
                s += 1

            
        return output



        