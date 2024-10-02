"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # SOLUTION #1: BFS
    # TC: O(N) -- must process each node at least once
    # SC: O(N) -- visited object is duplicate of graph.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        d = deque([node])
        visited = {}
        while d:
            cur = d.popleft()
            visited[cur.val] = {}
            for n in cur.neighbors:
                if n.val not in visited[cur.val]:
                    visited[cur.val].update({n.val : True})
                if n.val not in visited:
                    d.append(n)
        output = { 1: Node(1)}
        for val, neighbors in visited.items():
            if val not in output:
                output[val] = Node(val)
            for n in neighbors:
                if n not in output:
                    output[n] = Node(n)
                output[val].neighbors.append(output[n])
        return output[1]


