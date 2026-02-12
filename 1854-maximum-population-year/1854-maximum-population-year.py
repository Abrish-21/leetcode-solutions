class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        min_d = float("inf")
        max_d = 0
        for b,d in logs:
            min_d = min(min_d, b)
            max_d = max(max_d, d)

        date = [0] *( max_d - min_d)

        for b,d in logs:
            date[b-min_d] += 1
            if d < max_d:
                date[d-min_d] -= 1
        for end in range(1, len(date)):
            date[end] = date[end] + date[end-1]

        max_pop = max(date)
        for log in range(len(date)):
            if date[log] ==  max_pop:
                return min_d + log
                break


        