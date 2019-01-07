# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/friend-circles/description/
《朋友圈》

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
示例 1:
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。

示例 2:
输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
"""
import os


class Solution:
    def findCircleNum(self, M):
        """
        对每个人（没被遍历过的）从其开始进行图遍历，通过标记已经遍历过的联系为0避免遍历死循环
        :type M: List[List[int]]
        :rtype: int
        """
        circle = 0
        s = set()
        for i in range(len(M)):
            if i in s:
                continue
            friends = []
            self.traverse(M, i, friends)
            circle += 1
            for f in friends:
                s.add(f)
        return circle

    def traverse(self, grid, i, friends):
        friends.append(i)
        grid[i][i] == 0
        for j in range(0, len(grid)):
            if i == j:
                continue
            # i跟j联通
            if grid[i][j] == 1:
                # 置0防止遍历无法终止
                grid[i][j] = 0
                grid[j][i] = 0
                self.traverse(grid, j, friends)  # 递归至j的朋友
        # return friends


sol = Solution()
print(sol.findCircleNum([[1, 1, 0],
                         [1, 1, 0],
                         [0, 0, 1]]))
print(sol.findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(sol.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
print(sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
