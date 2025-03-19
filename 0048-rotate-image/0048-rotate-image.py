class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # record each of the modified elements in 
        # the matric to a dictionary and then copy it back to the matrix
        d = {}
        for i in range(len(matrix[0])-1,-1,-1):
            for j in range(len(matrix)):
                if j not in d:
                    d[j] = [matrix[i][j]]
                else:
                    d[j].append(matrix[i][j])
        # copy back the elements to the matrix
        # print(d)
        for key, array in d.items():
            matrix[key] = array
        
    

        