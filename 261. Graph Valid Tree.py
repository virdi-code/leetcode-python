# make adj list from edges.
# run dfs with bringing previous val along.
# if visit twice, return False
# if visited not = vertices, return False

from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if not n:
            return True
        adj = { i:[] for i in range(n)}
        visited=set()
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfsp(i,prev):
            if i in visited:
                return False
            visited.add(i)
            for neib in adj[i]:
                if neib == prev:
                    continue
                if not dfsp(neib,i):
                     return False
            return True
        
        if dfsp(0,None) and len(visited) == n:
            return True
        else:
            return False
