from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)

                vertices = len(component)
                degree_sum = sum(len(graph[node]) for node in component)
                edges_count = degree_sum // 2

                if edges_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans