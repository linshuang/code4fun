from typing import List
import sys

MAX_INT = sys.maxsize


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 使用nums中每一个数对从0到+无穷的段进行分割
        # 然后拿这些段里面最小的正整数
        ranges = [[0, MAX_INT]]  # 左开，右闭
        for num in nums:
            for i in range(len(ranges)):
                r = ranges[i]
                if r[0] < num <= r[1]:
                    if num == r[0] + 1:  # 缩小
                        r[0] = num
                        if r[0] == r[1]:  # 分割作废
                            ranges.pop(i)
                            break
                    elif num == r[1]:  # 缩小
                        r[1] == num - 1
                        if r[0] == r[1]:  # 分割作废
                            ranges.pop(i)
                            break
                    else:  # 一拆二
                        ranges.pop(i)
                        r1 = [r[0], num - 1]
                        if r1[0] != r1[1]:
                            ranges.insert(i, r1)
                            i += 1
                        r2 = [num, r[1]]
                        if r2[0] != r2[1]:
                            ranges.insert(i, r2)
                            i += 1
                        break
        # 找到range里面最小的
        return ranges[0][0] + 1


sol = Solution()
num = sol.firstMissingPositive([1, 2, 0])
print(num)  # 3
num = sol.firstMissingPositive([3, 4, -1, 1])
print(num)  # 2
num = sol.firstMissingPositive([7, 8, 9, 11, 12])
print(num)  # 1
num = sol.firstMissingPositive([7, 8, 1, 9, 11, 12])
print(num)  # 2
num = sol.firstMissingPositive([7, 8, 1, 9, 11, 12, 3, 2])
print(num)  # 4
