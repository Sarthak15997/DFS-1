# Time Complexity : O(m * n)
# Space Complexity : O(m * n)
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english: This code computes the distance of each cell to the nearest 0 in a binary matrix using a dynamic programming approach. It first initializes a result matrix with large values, setting 0-cells to distance 0, then performs two passes: top-left to bottom-right and bottom-right to top-left, updating each cell based on its neighbors. By taking the minimum distance from all directions, it ensures that each 1-cell contains the shortest path to a 0.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #DFS Solution
        #TC: O(2 *(m * n)) ~~ O(m * n)  SC: O(m*n)
        m, n = len(mat), len(mat[0])
        res = [[99999]* n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i > 0 and j > 0:
                        res[i][j] = min(res[i-1][j], res[i][j - 1]) + 1
                    elif i > 0:
                        res[i][j] = res[i - 1][j] + 1
                    elif j > 0:
                        res[i][j] = res[i][j - 1] + 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if mat[i][j] == 1:
                    if i < m - 1 and j < n - 1:
                        res[i][j] = min(res[i][j], min(res[i + 1][j], res[i][j + 1]) + 1)
                    elif i < m - 1:
                        res[i][j] = min(res[i][j], res[i+1][j] + 1)
                    elif j < n - 1:
                        res[i][j] = min(res[i][j], res[i][j + 1] + 1)
        
        return res
