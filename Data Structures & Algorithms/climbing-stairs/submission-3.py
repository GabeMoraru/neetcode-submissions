class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0, 1]
        for i in range(n):
            tmp = arr[1]
            arr[1] = arr[0] + arr[1]
            arr[0] = tmp
        return arr[1]
        