class Solution:
    # SOLUTION #1: BFS
    # TC: O(M*N) -- iterating over M * N matrix 
    # SC: O(M*N) -- auxillary space from worst case visited dict (additionally, if no input modification is allowed, would need to copy answer either way, O(M*N))
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = {}
        d = deque()

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    d.append([i,j])
                if mat[i][j] == 1:
                    visited[f"{i,j}"] = False
        l = deque()
        dist = 1
        while d:
            x,y = d.popleft()
            for r,c in [[1,0], [-1,0], [0,1], [0,-1]]:
                new_x = x+r
                new_y = y+c
                if f"{new_x,new_y}" in visited and visited[f"{new_x,new_y}"] == False:
                    visited[f"{new_x,new_y}"] = True
                    mat[new_x][new_y] = dist
                    l.append([new_x,new_y])
            if len(d) == 0 and len(l) != 0:
                dist += 1
                d = l
                l = deque()
        return mat
        