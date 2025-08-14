class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        output = []
        while i< len(firstList) and j < len(secondList):
            f_start, f_end = firstList[i]
            s_start, s_end  = secondList[j]
            if f_start <= s_end and s_start <= f_end:
                output.append([max(f_start, s_start), min(f_end, s_end)])
            if f_end <= s_end:
                i += 1
            else:
                j += 1
        return output


        