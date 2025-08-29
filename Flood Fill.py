# Time Complexity : O(m * n)
# Space Complexity : O(m * n)
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english: This code implements flood fill using DFS to change the color of a connected area in a 2D image.It first checks the original color at (sr, sc) and avoids doing anything if it’s already the target color, then recursively fills all neighboring cells with the same original color. The recursion explores up, down, left, and right directions, updating the image in-place and returning the modified image.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #DFS Solution TC: O(m * n)  SC: O(m * n)
        if image is None:
            return image
        
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        self.m = len(image)
        self.n = len(image[0])

        self.oldcolor = image[sr][sc]
        if self.oldcolor == color:
            return image
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == self.m or j == self.n or image[i][j] != self.oldcolor:
                return

            image[i][j] = color
            for dir in self.dirs:
                r = dir[0] + i
                c = dir[1] + j
                dfs(r, c)
            
        dfs(sr, sc)
        return image
