class Solution:
    def climbStairs(self, n: int) -> int:
        start , count = n, 0
        result = 0
        while start >= count:
            tmp = 1
            for i in range(count):
                tmp = tmp * (start-i) // (i+1)
            result += tmp
            count += 1
            start -= 1
        return result