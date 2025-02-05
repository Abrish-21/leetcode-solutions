class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        else:
            indx  = 0
            s_arry = [i for i in s]
            goal_arry = [i for i in goal]
            # change both to arrays
            while indx < len(s):
                s_arry.append(s_arry[0])
                del s_arry[0]
                if(s_arry == goal_arry):
                    return True
                indx +=1
                print(s_arry)
                print(goal_arry)
            return False



        