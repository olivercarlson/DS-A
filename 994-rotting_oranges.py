from collections import deque
class Solution:
    # SOLUTION #1: BFS
    # TC: O(2*M*N) == O(M*N) -- visiting each item in grid at most 2x -- initial scan to find items for deque (1x) + all oranges being rotten = iterating over entire deque (1x).
    # SC: O(2*M*N) == O(M*N) -- storing all items of the grid in the deque worst case. 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        d = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    d.append([i,j])
        new_level = deque()
        while d:
            x,y = d.popleft()
            for r,c in [[1,0], [-1, 0], [0,1], [0,-1]]:
                new_r = x + r
                new_c = y + c
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[new_r]) and grid[new_r][new_c] == 1:
                    new_level.append([new_r,new_c])
                    grid[new_r][new_c] = 2
                    fresh -= 1
            
            if len(d) == 0 and len(new_level) > 0:
                d = new_level
                new_level = deque()
                ans += 1

        if fresh > 0:
            return -1

        return ans






    