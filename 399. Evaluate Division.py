class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a,b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1/value

        def dfs(start, end, visited):
            
            if start == end:
                return 1.0
            
            visited.add(start)

            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor , end, visited)
                    if result != -1.0:
                        return val*result
            return -1.0
        
        result = []
        for a,b in queries:
          if a not in graph or b not in graph :
            result.append(-1.0)
        
          else:
            visited = set()
            result.append(dfs(a,b,visited))
    
        return result 
