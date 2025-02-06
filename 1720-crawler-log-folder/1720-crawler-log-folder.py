class Solution:
    def minOperations(self, logs: List[str]) -> int:
        mystack  = []
        for log in logs:
            if log == "../":
                if mystack:
                    mystack.pop()
            else:
                if log != "./":
                    mystack.append(log)
        return len(mystack)

        