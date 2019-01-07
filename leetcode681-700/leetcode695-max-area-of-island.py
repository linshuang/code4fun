# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/max-area-of-island/description/
《岛屿的最大面积》

给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        遍历二维表里所有的点，从点开始递归地进行图遍历，递归过程中走过的点被标0防止多次被遍历
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self.traverse(grid, i, j)
                if area > max_area:
                    max_area = area
        return max_area

    def traverse(self, grid, i, j):
        if grid[i][j] == 0:  # 为0则直接返回
            return 0

        tmp_area = grid[i][j]  # 面积
        grid[i][j] = 0  # 走过该点，置0
        for m in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            ii = i + m[0]
            jj = j + m[1]
            if ii < 0 or jj < 0 or ii > len(grid) - 1 or jj > len(grid[0]) - 1:
                continue
            else:
                tmp_area += self.traverse(grid, ii, jj)  # 递归至旁边的点
        return tmp_area


sol = Solution()
print(sol.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
print(sol.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
