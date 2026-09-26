class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]

        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        not_seen = set(range(n))

        def dfs(node, parent):
            not_seen.remove(node)

            for nbr in adj[node]:
                if nbr == parent:
                    continue
                if nbr in not_seen:
                    dfs(nbr, node)
        
        while not_seen:
            unseen = not_seen.pop()
            not_seen.add(unseen)
            
            dfs(unseen, -1)
            count += 1

        return count

        