# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/simplify-path/description/
《简化路径》

给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:
你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
"""


class Solution:
    def simplifyPath(self, path):
        """
        将目录用/进行分割，利用栈处理各个目录，然后对栈里的内容进行拼接
        :type path: str
        :rtype: str
        """
        spath = ""
        stack = []  # 用这个列表模拟栈的行为
        dirs = path.split('/')
        for dir in dirs:
            if dir == '.':  # 点不做任何处理
                continue
            elif dir == '..':  # ..从栈里pop出之前的非..的目录；或者入..
                if len(stack) > 0 and stack[-1] != '..':
                    stack.pop(len(stack) - 1)
                else:
                    stack.append('..')
            elif dir == '':  # 斜杠不处理
                continue
            else:  # 普通目录入栈
                stack.append(dir)
        # 拼接栈里的结果
        for i in range(len(stack)):
            item = stack[i]
            spath += ('/' + item)
        # 特殊处理空栈
        if len(stack) == 0:
            return '/'
        # 去掉最后的/
        if len(spath) > 1 and spath[-1] == "/":
            return spath[0:len(spath) - 1]
        return spath


sol = Solution()
print(sol.simplifyPath("/home/../../.."))
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/a/./b/../../c/"))
print(sol.simplifyPath("/"))
print(sol.simplifyPath("///"))
