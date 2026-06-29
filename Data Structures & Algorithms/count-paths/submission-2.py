class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevrow = [0] * n

        # array[m][n] = array[i][j]

        for i in range(m - 1, -1, -1):
            newrow = [0] * n
            newrow[-1] = 1

            for j in range(n - 2, -1, -1):
                newrow[j] = prevrow[j] + newrow[j + 1]
            prevrow = newrow
        
        return prevrow[0]