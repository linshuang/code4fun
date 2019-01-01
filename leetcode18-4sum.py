"""
https://leetcode-cn.com/problems/4sum/
《四数之和》

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type t: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        i = 0
        j = len(nums) - 1
        while j - i > 2:
            while j - i > 2:  #中间隔两位
                t = target - nums[i] - nums[j]
                m = i + 1
                n = j - 1
                while m < n:  # 做逼夹
                    sum = nums[m] + nums[n]
                    if sum == t:
                        result.append([nums[i], nums[m], nums[n], nums[j]])
                        ii = m + 1
                        while ii < n and nums[ii] == nums[m]:
                            ii += 1
                        m = ii
                        jj = n - 1
                        while jj > m and nums[jj] == nums[n]:
                            jj -= 1
                        n = jj
                    elif sum > t:
                        n -= 1
                    else:
                        m += 1
                # 将i往后移动
                ii = i + 1
                while ii < j and nums[ii] == nums[i]:
                    ii += 1
                i = ii
            # 重置i
            i = 0
            # 将j往前移动
            jj = j - 1
            while jj > i  and nums[jj] == nums[j]:
                jj -= 1
            j = jj
        return result


sol = Solution()
# print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
# print(sol.fourSum([-3,-1,0,2,4,5], 0))
print(sol.fourSum([5,5,3,5,1,-5,1,-2], 4))