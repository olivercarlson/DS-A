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
    # TC: O(N+M) -- must process each vertex + edge at least once
    # SC: O(N) -- visited is a store of all vertices
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
    # SOLUTION #2: DFS
    # TC: O(N+M) -- must process each vertex and each edge at least once.
    # SC: O(N) -- visited object is duplicate of all nodes (and call stack is size of O(N) too)
    def dfs(self, node, copy, visited = {}):
        if copy.val in visited:
            return
        visited[copy.val] = copy
        for n in node.neighbors:
            if n.val not in visited:
                new_node = Node(n.val)
                copy.neighbors.append(new_node)
                self.dfs(n, new_node, visited)
            else:
                copy.neighbors.append(visited[n.val])
        return node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copy = Node(1)
        visited = {}
        self.dfs(node, copy, visited)
        return copy