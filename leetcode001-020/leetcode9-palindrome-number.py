"""
https://leetcode-cn.com/problems/palindrome-number/
《回文数》

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x):
        """
        普通的整数翻转的想法，通过取余跟小数点操作来获得翻转后的数值。
        加入了快速终止，跟0，负数，10倍数的边界处理
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x %10==0:
            return False
        z = x
        y = 0
        while True:
            tmp = z % 10
            y = y * 10 + tmp  # 翻转n位的数值
            z = int(z / 10)  # 小数点进位
            if y >= z:  # y>=z来快速终止，即此刻已经到达中位（非10倍数情况下）
                break
        return z == y or z == int(y / 10)  # 相等则为偶数位，等于1/10则为奇数位


sol = Solution()
# assert (sol.isPalindrome(121) == True)
# assert (sol.isPalindrome(-121) == False)
assert (sol.isPalindrome(10) == False)
