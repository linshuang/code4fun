"""
https://leetcode-cn.com/problems/generate-parentheses/
《括号生成》

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        递归：分成左括号和右括号，一开始有n个左括号待利用，0个右括号。
        每次递归分成使用剩余的左括号或者剩余的右括号，每使用左括号则增加一个右括号。
        当左右括号均为0时则递归终止
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generateCore(n, 0, result, '')
        return result

    def generateCore(self, left, right, result, str):
        """
        递归地生成括号组合
        :param left: 剩余多少个左括号
        :param right: 累计了多少个右括号
        :param result: 结果列表
        :param str: 当前已经拼出的字符串
        :return:
        """
        if left == 0:
            if right != 0:
                l = [')' for x in range(right)]
                str += ''.join(l)
            result.append(str)
            return

        self.generateCore(left - 1, right + 1, result, str + '(')
        if right > 0:
            self.generateCore(left, right - 1, result, str + ')')


sol = Solution()
print(sol.generateParenthesis(3))
