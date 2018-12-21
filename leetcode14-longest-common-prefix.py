"""
https://leetcode-cn.com/problems/longest-common-prefix/
《 最长公共前缀》

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ''
        if len(strs) == 0:  # 特殊处理空
            return common_prefix

        i = 0
        while True:
            stop = False
            str1 = strs[0]
            if i >= len(str1):
                break
            c = str1[i]
            for j in range(1, len(strs)):
                str2 = strs[j]
                if i >= len(str2) \
                        or c != str2[i]:
                    stop = True
                    break
            if stop:
                break
            else:
                common_prefix += c
                i += 1
        return common_prefix


sol = Solution()
assert (sol.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl')
assert (sol.longestCommonPrefix(["dog", "racecar", "car"]) == '')
assert (sol.longestCommonPrefix(["dog", "dogg", ""]) == '')
assert (sol.longestCommonPrefix(["dog"]) == 'dog')
assert (sol.longestCommonPrefix(["dog", "dog1", "dog2"]) == 'dog')
assert (sol.longestCommonPrefix(["dog", "dog", "dog"]) == 'dog')
assert (sol.longestCommonPrefix(['']) == '')
assert (sol.longestCommonPrefix([]) == '')
