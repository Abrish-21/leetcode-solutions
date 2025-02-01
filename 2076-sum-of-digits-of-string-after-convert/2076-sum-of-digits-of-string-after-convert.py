class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # step1 = change letter to 1- 26
        # change to number
        # transform until k
        toInteger = ''
        for letter in s:
            toInteger += str(ord(letter)-96)
        # now let's convert it to number
        result = [int(i) for i in str(toInteger)]

        while k > 0:
            add = sum(result)
            result  = [int(i) for i in str(add)]
            k -= 1
        return add


        