class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        
        def get(s):
            quot, rem = divmod(s-1, N)
            row = N -1 - quot
            col = rem if row%2 != N%2 else N-1-rem
            return row, col
        dist = {1:0}
        q = collections.deque([1])
        while q:
            s = q.popleft()
            if s == N*N: return dist[s]
            for s2 in range(s+1, min(s+6, N*N)+1):
                r,c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    q.append(s2)
        return -1
                    
