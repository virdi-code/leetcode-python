# go from pac and atl to the grid.
# two hash sets. pac and atl
# start from boundaries.



class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(h),len(h[0])
        pac = set()
        atl = set()
        res =[]
        def dfs(r,c,visited,prevH):
            if( (r,c) in visited or r<0 or c<0 or r==ROWS or c==COLS or  h[r][c] <prevH):
                return
            visited.add((r,c))
            dfs(r+1,c,visited,h[r][c])
            dfs(r-1,c,visited,h[r][c])
            dfs(r,c+1,visited,h[r][c])
            dfs(r,c-1,visited,h[r][c])
             
        
        for c in range(COLS):
            dfs(0,c,pac,h[0][c])
            dfs(ROWS-1,c,atl,h[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r,0,pac,h[r][0])
            dfs(r,COLS-1,atl,h[r][COLS-1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))
                    
        return res
