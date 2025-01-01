class Solution:
    def removeDuplicates(self, s: str) -> str:
        if s != None:
            stack = [s[0]]
        else:
            return s
        for i in range(1, len(s)):
            # remove duplicates
            if stack:
                compare = stack[-1]
                if (s[i] == compare):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

           
        return ''.join(stack)