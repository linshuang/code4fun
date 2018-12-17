"""
https://leetcode-cn.com/problems/container-with-most-water/
《盛最多水的容器》

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。


图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。


示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""
import math
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        # for i in range(len(height)):
        i = 0
        while i < len(height):
            h1 = height[i]
            if h1 == 0:
                continue
            j = j_start = i+ max(1, math.ceil(max_area/h1))
            for j in range(j_start, len(height)):
                h2 = height[j]
                area = (j-i)*min(h1,h2)
                if max_area < area:
                    max_area = area
            i = j
        return max_area

sol=Solution()
assert(sol.maxArea([1,8,6,2,5,4,8,3,7])==49)
assert(sol.maxArea([])==0)
assert(sol.maxArea([1,1,1,1,1,1,1])==6)