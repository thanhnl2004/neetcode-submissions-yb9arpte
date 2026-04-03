class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbStairsHelper(n, memo)
    
    def climbStairsHelper(self, n: int, memo: dict) -> int:
        if n <= 2: return n
        if n in memo: return memo[n]

        memo[n] = self.climbStairsHelper(n-1, memo) + self.climbStairsHelper(n-2, memo)

        return memo[n]
        

        