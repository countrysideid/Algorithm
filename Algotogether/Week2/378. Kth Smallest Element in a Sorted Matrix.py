class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap,matrix[i][j])
                
        return heapq.nsmallest(k,heap)[-1]
