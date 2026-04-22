class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        self.prev = [0] * (n + 1)
        
        
        self.prev[1] = 1
        self.prev[2] = 2

        for i in range(3, n + 1):
            self.prev[i] = self.prev[i-1] + self.prev[i-2]

        return self.prev[i]