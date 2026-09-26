class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        count = 0
        def dfs(node, parent):
            nonlocal count
            seen.add(node)
            count += 1

            for nbr in adj[node]:
                if nbr == parent:
                    continue
                if nbr in seen:
                    return True
                if dfs(nbr, node):
                    return True

        # need to check: connected, no cycles
        seen = set()

        # dfs: build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen.clear()
        if dfs(0, -1):
            return False

        return len(seen) == n
        