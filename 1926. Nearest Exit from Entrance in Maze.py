from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        m, n = len(maze), len(maze[0])  # Dimensions of the maze
        
        # Initialize the queue for BFS with the entrance point and steps as 0
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'  # Mark the entrance as visited
        
        while queue:
            x, y, steps = queue.popleft()
            
            # Check if we are at a border cell (and not the entrance itself)
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x != entrance[0] or y != entrance[1]):
                return steps
            
            # Explore the four possible directions (up, down, left, right)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'  # Mark as visited
                    queue.append((nx, ny, steps + 1))
        
        return -1  # If no exit is found
