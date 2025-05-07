"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance  = 0
        store = {}
        for employee in employees:
            print(type(employee.subordinates))
            store[employee.id] = employee
      
        def dfs(employee):
            nonlocal importance
            importance += employee.importance
            if employee.subordinates:
                for subordinate in employee.subordinates:
                    dfs(store[subordinate])
            return importance
        for employee in employees:
            if employee.id == id:
                return dfs(employee)
        

                    
            

            