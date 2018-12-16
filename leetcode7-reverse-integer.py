"""
https://leetcode-cn.com/problems/reverse-integer/description/
《整数反转》

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def __init__(self):
        self.left_boundry = -(2 << 30)
        self.right_boundry = (2 << 30) - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = x < 0
        y = 0
        x = abs(x)
        while x > 0:
            x1 = x % 10
            y = y * 10 + x1
            x = int(x / 10)

        if is_neg:
            y = -y
        if not (self.left_boundry <= y <= self.right_boundry):
            return 0
        return y

print(pow(2,31))
print(2<<31)

sol = Solution()
# assert (sol.reverse(123)== 321)
# assert (sol.reverse(120)== 21)
# assert (sol.reverse(-123)== -321)
# assert (sol.reverse(0)==0)
# assert (sol.reverse(10000)==1)
# assert (sol.reverse(100001)==100001)
# assert (sol.reverse(-100001)==-100001)
assert (sol.reverse(2 << 31 - 1) == 0)
# assert (sol.reverse(-2^31+1)==2^31-1)
