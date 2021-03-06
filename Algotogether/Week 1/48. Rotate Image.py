class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        return matrix
