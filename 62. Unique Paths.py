class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     memo = {}

    #     def helper(i, j):
    #         # Base case: If we reach the bottom-right corner, there's exactly one path
    #         if i == m - 1 and j == n - 1:
    #             return 1
    #         # If out of bounds, there are no paths
    #         if i >= m or j >= n:
    #             return 0
    #         # Check memoization dictionary
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         # Recursive calls: move right and down
    #         memo[(i, j)] = helper(i + 1, j) + helper(i, j + 1)
    #         return memo[(i, j)]

    #     return helper(0, 0)
   
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for _ in range(m)]

        for i in range (m):
            dp[i][0] = 1
        for j in range (n):
            dp[0][j] = 1


        for i in range(1,m):
            for j in range(1,n):

                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            
        return dp[m-1][n-1]
