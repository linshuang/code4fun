from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 计算微分
        dif = [0 for i in range(len(nums) - 1)]
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:  # 升序
                dif[i] = -1
            elif nums[i] < nums[i + 1]:  # 降序
                dif[i] = 1
        # 找到最后一个升序，那么对应位置的num就是需要被提升的数
        idx = -1
        for i in range(0, len(dif)):
            if dif[i] == 1:
                idx = i

        if idx == -1:  # 都是降序
            nums.sort()
        else:  # 找到从idx开始后面里比nums[idx]大的最小的数，交互，然后把idx之后的列表进行排序
            idx2 = idx + 1
            minnum = nums[idx2]
            for i in range(idx + 1, len(nums)):
                if nums[idx] < nums[i] < minnum:
                    idx2 = i
                    minnum = nums[idx2]
            nums[idx2] = nums[idx]
            nums[idx] = minnum
            nums2 = nums[idx + 1:]
            nums2.sort()
            nums[idx + 1:] = nums2
            nums[idx] = minnum


sol = Solution()
nums = [5,4,7,5,3,2]
sol.nextPermutation(nums)
print(nums)
nums = [1, 3, 2]
sol.nextPermutation(nums)
print(nums)
nums = [2, 3, 1]
sol.nextPermutation(nums)
print(nums)
nums = [1, 2, 3]
sol.nextPermutation(nums)
print(nums)
nums = [3, 1, 2]
sol.nextPermutation(nums)
print(nums)
nums = [3, 2, 1]
sol.nextPermutation(nums)
print(nums)
nums = [3, 2, 2.5, 1]
sol.nextPermutation(nums)
print(nums)
nums = [1, 1, 5]
sol.nextPermutation(nums)
print(nums)
nums = [2, 1, 5]
sol.nextPermutation(nums)
print(nums)
nums = [1]
sol.nextPermutation(nums)
print(nums)
