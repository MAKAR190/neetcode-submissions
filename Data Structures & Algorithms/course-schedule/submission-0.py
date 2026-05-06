from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        finished = set()

        for a, b in prerequisites:
            graph[a].append(b)
        
        path = set()

        def dfs(node):
            if node in path:
                return False
            
            if node in finished:
                return True

            path.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in finished:
                    if not dfs(neighbor):
                        return False
                    else:
                        finished.add(neighbor)

            path.remove(node)
            return True
        
        for i in range(numCourses):
            if i not in finished:
                if not dfs(i):
                    return False
                else:
                    finished.add(i)

        return len(finished) == numCourses