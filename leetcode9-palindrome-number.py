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
            y = y * 10 + tmp
            z = int(z / 10)
            if y >= z:
                break
        print(y)
        return z == y or z == int(y / 10)


sol = Solution()
# assert (sol.isPalindrome(121) == True)
# assert (sol.isPalindrome(-121) == False)
assert (sol.isPalindrome(10) == False)
