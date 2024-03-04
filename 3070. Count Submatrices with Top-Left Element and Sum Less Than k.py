class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if i == 0: 
                    if j>0:
                        grid[i][j] = grid[i][j-1] + grid[i][j]
                    else:
                        grid[i][j] = grid[i][j]
                elif j == 0: 
                    if i>0:
                        grid[i][j] = grid[i-1][j] + grid[i][j]
                    else:
                        grid[i][j] = grid[i][j]
                    
                else: 
                    grid[i][j] = grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1] + grid[i][j]
                
                if grid[i][j]<=k: count+=1

        return count