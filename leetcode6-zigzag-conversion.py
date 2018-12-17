# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/zigzag-conversion/
《 Z 字形变换》

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        寻找并总结规律，获得输出的每位字符对应原字符串的位置
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zig_zag_str = ''
        for row in range(numRows):
            zig_zag = max(2 * numRows - 2,1)
            zig = zig_zag - 2 * row
            zag = 2 * row
            idx = row
            i = 0
            while True:
                i += 1
                if i % 2 == 0:
                    idx += zig
                    if zig == 0:
                        if zag == 0:
                            break
                        continue
                if i % 2 == 1 and i != 1:
                    idx += zag
                    if zag == 0:
                        if zig == 0:
                            break
                        continue
                if idx < len(s):
                    zig_zag_str += s[idx]
                else:
                    break
        print(zig_zag_str)
        return zig_zag_str


sol = Solution()
# assert (sol.convert("LEETCODEISHIRING", 3) == "LCIRETOESIIGEDHN")
# assert (sol.convert("LEETCODEISHIRING", 4) == "LDREOEIIECIHNTSG")
# assert (sol.convert("LEETCODEISHIRING", 100) == "LEETCODEISHIRING")
# assert (sol.convert("LEETCODEISHIRING", 16) == "LEETCODEISHIRING")
# assert (sol.convert("LEETCODEISHIRING", 15) == "LEETCODEISHIRIGN")
# assert (sol.convert("", 15) == "")
# assert (sol.convert("1", 1) == "1")
assert (sol.convert("AB", 1) == "AB")
# assert (sol.convert("ABC", 2) == "ACB")
