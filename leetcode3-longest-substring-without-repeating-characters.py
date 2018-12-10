"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
《无重复字符的最长子串》

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        0. 设置ij为0，向后逐步移动j
        1. 计算第j个元素在s[i:j]中的位置pos
        2. 位置pos不为-1更改i为pos+1+i
        3. 否则尝试更新最大长度
        4. 移动j重复步骤1-3
        :type s: str
        :rtype: int
        """
        i = j = 0
        longest = 0
        for j in range(0, len(s)):
            idx = s[i:j].find(s[j])
            if idx >= 0:
                i = idx + 1 + i
                continue
            if (j - i + 1) > longest:
                longest = (j - i + 1)
        return longest


sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))
# print(sol.lengthOfLongestSubstring("bbbbb"))
# print(sol.lengthOfLongestSubstring("abcdef"))
# print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("bbtablud"))
