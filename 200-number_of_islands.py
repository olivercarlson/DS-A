class Solution:
    # SOLUTION #1: DFS
    # TC: O (M * N) where M and N = grid dimensions.
    # SC: O (M * N) 
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(grid, i,j):
            if i < len(grid) and i >= 0 and j < len(grid[i]) and j >= 0 and grid[i][j] == '1':
                grid[i][j] = 0
                for x,y in [[1,0], [-1,0], [0,1], [0,-1]]:
                    dfs(grid, i+x, j+y)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(grid, i,j)
        
        return islands

    # SOLUTION #2: BFS
    # TC: O (M*N)
    # SC: O (M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        d = deque()
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    d.append([i,j])
                    islands += 1 

                    while d:
                        x,y = d.popleft()
                        for r,c in [[1,0], [-1,0], [0,1], [0,-1]]:
                            new_r = r + x
                            new_c = c + y
                            if new_r < len(grid) and new_r >= 0 and new_c < len(grid[new_r]) and new_c >= 0 and grid[new_r][new_c] == '1':
                                grid[new_r][new_c] = 0
                                d.append([new_r,new_c])
        return islands