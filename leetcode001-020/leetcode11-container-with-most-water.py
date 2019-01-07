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


class Solution:
    def maxArea(self, height):
        """
        设置两个指针p1,p2分别指向数组头尾，将指向较小数的指针向较大数的方向移动，每次计算area_cur，比对max_area，最终得到最大面积
        在移动较小数值指针p_min的过程中，等价于进行了剪枝，剔除了左边为p_min，右边为(p_min,p_max)或(p_max,p_min)[两者等价，后只写前一种]之间的所有可能。
        那么需要证明左边为p_min，右边为(p_min,p_max)之间的所有可能产生的面积area_cut  均差于是当前情况的。
        证：area_cut=min(height[p_min],height[p_right])*abs(p_right-p_min)
                <height[p_min]*abs(p_max-p_min) = area_cur
        故每次的剪枝，都是合理
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        i = 0
        j = len(height) - 1
        while i < j:  # 双指针
            h1 = height[i]
            h2 = height[j]
            area = (j - i) * min(h1, h2)
            if area > max_area:
                max_area = area
            # 执行较小数的指针向较大数的方向移动
            if h1 < h2:
                i += 1
                while i < j and height[i] <= h1:  # 移动到小于较小数的数的位置是没有意义的，故直接跳过
                    i += 1
            else:
                j -= 1
                while j > i and height[j] <= h2:
                    j -= 1
        return max_area

sol=Solution()
assert(sol.maxArea([1,8,6,2,5,4,8,3,7])==49)
assert(sol.maxArea([])==0)
assert(sol.maxArea([1,1,1,1,1,1,1])==6)