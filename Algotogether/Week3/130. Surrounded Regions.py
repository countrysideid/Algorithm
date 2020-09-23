class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        def dfs(board,r, c, length, width):
            if board[r][c] != 'O':
                return
            board[r][c] = 'E'
            if r < length -1: dfs(board,r +1, c, length, width)
            if c < width -1: dfs(board,r , c + 1, length, width)
            if r >0: dfs(board,r -1, c, length, width)
            if c > 0: dfs(board,r , c -1, length, width)
        length, width = len(board), len(board[0])
        from itertools import product
        borders = list(product(range(length), [0, width-1])) \
                + list(product([0, length-1], range(width)))
        
        for r, c in borders:
            dfs(board,r,c, length, width)
        
        for r in range(length):
            for c in range(width):
                if board[r][c] == 'O': board[r][c]= 'X'
                elif board[r][c] == 'E': board[r][c] = 'O'
