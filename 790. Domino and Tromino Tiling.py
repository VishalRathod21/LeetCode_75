class Solution:
    # def numTilings(self, n: int) -> int:
    #     MOD = 10**9 + 7
        
    #     # Base cases
    #     if n == 0:
    #         return 1  # An empty board has 1 way to tile
    #     if n == 1:
    #         return 1  # A 2x1 board can only be tiled with a single domino

    #     # Recursive formula
    #     return (self.numTilings(n - 1) + self.numTilings(n - 2)) % MOD
    
    def Memo(self, n: int, dp: list) -> int:
        MOD = 10**9 + 7
        
        # Base cases
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        # If already calculated, return the result
        if dp[n] != -1:
            return dp[n]
        
        # Recursive case
        dp[n] = (self.Memo(n - 1, dp) + self.Memo(n - 2, dp)) % MOD
        return dp[n]

    def Tab(self,n:int)->int:
        MOD = 10**9 + 7
        
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0]*(n+1)
        dp[1],dp[2] = 1,2
        extra = [0]*(n+1)
        extra[2] = 1

        for i in range (3,n+1):
            dp[i] = (dp[i-1]+dp[i-2]+2*extra[i-1])%MOD
            extra[i] = (dp[i-2]+extra[i-1])%MOD
        
        return dp[n]

    def numTilings(self, n: int) -> int:
        # Initialize memoization array with -1
        dp = [-1] * (n + 1)
        
        # Call the memoized helper function
        return self.Tab(n)

    
