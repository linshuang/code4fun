"""
https://leetcode-cn.com/problems/3sum/description/
《三数之和为0》

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        1. 排序数组
        2. 从0开始固定一个数值v
        3. 使用(0-v)在剩余的数组里做two-sum的逼夹
        4. 对于逼夹结果结合固定的数值即为结果列表的一元
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:  # 快速跳出
                break;
            target = -nums[i]
            m = i + 1
            n = len(nums) - 1
            if m >= n:
                break
            while True:  # 做逼夹
                sum = nums[m] + nums[n]
                if sum == target:
                    result.append([nums[i], nums[m], nums[n]])
                    ii = m + 1
                    while ii < n and nums[ii] == nums[m]:
                        ii += 1
                    m = ii
                    jj = n - 1
                    while jj > m and nums[jj] == nums[n]:
                        jj -= 1
                    n = jj
                elif sum > target:
                    n -= 1
                else:
                    m += 1
                if m >= n:  # 逼夹跳出条件
                    break
            ii = i + 1
            while ii < len(nums) and nums[ii] == nums[i]:
                ii += 1
            i = ii
        return result


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 0, 0, 0]))
