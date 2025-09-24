class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        city_1 = [i for i, j in costs]
        return_cost = [j - i for i, j in costs]
        return_cost.sort()
        return sum(city_1) + sum(return_cost[:len(costs) // 2])
        