# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/two-sum/description/
《两数之和——寻找两数和为目标值得组合》

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution:
    def twoSum(self, nums, target):
        """
        逼夹法：
        1. 排序
        2. 设置头尾指针
        3. 根据头尾指针对应之和，来移动头尾指针
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()  # 从小到大排序
        i = 0  # 头指针
        j = len(nums) - 1  # 尾指针
        result = []
        while True:  # 一直循环直至i>=j
            sum = nums[i] + nums[j]
            if sum == target:  # 假如和便是目标
                result.append([i, j])  # 记录结果
                # 确定下一轮的指针
                ii = i + 1
                while ii < j and nums[ii] == nums[i] :  # 跳掉重复的
                    ii += 1
                i = ii
                jj = j - 1
                while jj > i and nums[jj] == nums[j]:  # 跳掉重复的
                    jj -= 1
                j = jj
            elif sum > target:  # 假如过大，j向前移动，即减少和
                j -= 1
            else:  # 假如过小，i向后移动，即增加和
                i += 1
            if i >= j:  # 逼夹跳出条件
                break
        if len(result) > 0:
            return result[0]
        else:
            return []


    def twoSum2(nums, target):
        """
        普通做法n^2复杂度
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        return []


# rlt=twoSum([3,2,4],6)
# print(rlt)
sol = Solution()
# print(sol.twoSum([-2, -1, 0, 1, 2], 0))
# print(sol.twoSum([3,3], 6))
print(sol.twoSum([3,2,4], 6))
