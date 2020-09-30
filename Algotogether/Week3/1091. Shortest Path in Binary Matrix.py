class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        q = [(0, 0, 1)]
        for i,j,d in q:
            if i == n-1 and j == n-1: return d
            for x, y in [(i+1,j),(i-1,j), (i+1,j-1), (i,j-1), (i-1,j-1), (i+1,j+1), (i,j+1), (i-1,j+1)]:
                if 0<=x <= n-1 and 0<= y < n and grid [ x][ y] == 0:
                    grid [x][y] =1
                    q.append(( x, y, d+1))
        return -1
        
