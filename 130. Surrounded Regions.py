class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def addRoom(r,c):
            if( r< 0 or r == ROWS or c<0 or c == COLS or 
            (r,c) in visit or board[r][c] != 'O'):
                return
            visit.add((r,c))
            q.append([r,c])
    
        
        
        ROWS,COLS = len(board),len(board[0])
        visit = set()
        final = set()
        q = deque()
        for i in 0,ROWS-1:
            for j in range(COLS):
                if board[i][j] == 'O':
                    q.append([i,j])
        for i in range(ROWS):
            for j in 0,COLS-1:
                if board[i][j] == 'O':
                    q.append([i,j])
                    visit.add((i,j))
        while q:
            r,c = q.popleft()
            final.add((r,c))
            addRoom(r-1 , c )
            addRoom(r , c-1 )
            addRoom(r+1 , c )
            addRoom(r , c+1 )
        for i in range(ROWS):
            for j in range(COLS):
                if(i,j) not in final:
                    board[i][j]='X'
        
        #print(final)
        
