"""
https://leetcode-cn.com/problems/3sum/description/
������֮��Ϊ0��

����һ������ n ������������ nums���ж� nums ���Ƿ��������Ԫ�� a��b��c ��ʹ�� a + b + c = 0 ���ҳ��������������Ҳ��ظ�����Ԫ�顣
ע�⣺���в����԰����ظ�����Ԫ�顣

����, �������� nums = [-1, 0, 1, 2, -1, -4]��
����Ҫ�����Ԫ�鼯��Ϊ��
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        1. ��������
        2. ��0��ʼ�̶�һ����ֵv
        3. ʹ��(0-v)��ʣ�����������two-sum�ıƼ�
        4. ���ڱƼн����Ϲ̶�����ֵ��Ϊ����б��һԪ
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:  # ��������
                break;
            target = -nums[i]
            m = i + 1
            n = len(nums) - 1
            if m >= n:
                break
            while True:  # ���Ƽ�
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
                if m >= n:  # �Ƽ���������
                    break
            ii = i + 1
            while ii < len(nums) and nums[ii] == nums[i]:
                ii += 1
            i = ii
        return result


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 0, 0, 0]))
