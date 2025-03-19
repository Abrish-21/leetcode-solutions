class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # first create a dictionary to record each element
        d = {}
        m = len(mat)
        n = len(mat[0])
        # since every element in the same diagonal will 
        # have the same index sum, let's use that as a key to the dictionary
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        # now we got all the elements, we can simply pick the diagonal order
        result = []
        for key,matrix in d.items():
            if key%2 == 0:
                [result.append(x) for x in matrix[::-1]]
            else:
                [result.append(x) for x in matrix]
        return result
           




        