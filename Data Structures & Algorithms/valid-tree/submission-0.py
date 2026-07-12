class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Build graph with adjacency list (add each other as edges since undirected)
        DFS through graph with starting node
        If cycle detected, return False
        If not all nodes reached (len(visited) != n), return False
        Otherwise, return True
        '''
        if not n:
            return True
        
        graph = { node: [] for node in range(n) }

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()
        def dfs(curr, prev):
            # cycle detected if a later node made it's way back to an already visited node
            if curr in visited:
                return False
            
            # mark current node as visited
            visited.add(curr)
            for neighbor in graph[curr]:
                # neighbor != prev ensures that it does not go back and forth infinitely
                # since edges are undirected
                if neighbor != prev and not dfs(neighbor, curr):
                    return False

            return True
            
        # len(visited) == n checks that graph is fully connected
        return dfs(0, -1) and len(visited) == n

            

