"""
https://leetcode-cn.com/problems/divide-two-integers/
《两数相除》

给定两个整数，被除数 dividend 和除数 divisor。
将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2

说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
本题中，如果除法结果溢出，则返回 2^31 − 1。
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        a/b=k+c，k对应的二进制码code总是可以将k分解为2^n*code[n]+2^(n-1)*code[n-1]+2^0*code[0]
        故a=(2^n*code[n]+2^(n-1)*code[n-1]+2^0*code[0])*b+c
        也就可以通过对b的多次移位得到a-c，而每次移位的位数组成的二进制码即为k
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0
        divisor_abs2 = divisor_abs
        # 循环中不断的将除数进行移位，得到最接近剩余被除数的除数
        # 一次循环即得到商的一部分的数值
        while dividend_abs >= divisor_abs2:
            q = 1
            while dividend_abs >= divisor_abs2:  # 这里循环对除数移位，从而得到一个接近被除数的除数
                divisor_abs2 = divisor_abs2 << 1
                q <<= 1
            divisor_abs2 = divisor_abs2 >> 1  # 退位
            dividend_abs -= divisor_abs2  # 剩余的数值，即为新的被除数
            divisor_abs2 = divisor_abs  # 重置除数

            q >>= 1
            quotient += q  # 累积商

        # 计算正负号
        factor = -1
        if (dividend > 0 and divisor>0) or(dividend <0 and divisor<0):
            factor = 1

        if quotient >= 2147483648 and factor==1:
            quotient=2147483647

        return quotient * factor

sol = Solution()
# assert sol.divide(10, 3)==3
# assert sol.divide(24, 3)==8
# assert sol.divide(24, 1)==24
# assert sol.divide(255, 5)==51
# assert sol.divide(7, -3)==-2
assert sol.divide(-2147483648,-1)==2147483647