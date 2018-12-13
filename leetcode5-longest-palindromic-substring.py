# -!- coding: utf-8 -!-

"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
《最长回文子串》

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        1. 遍历串上每个字符c
        2. 从c开始向左右扩散，计算以该字符c为中心的最大回文串（奇）
        3. 从c和c的前一字符开始向左右扩散，计算以或该字符c和其前一同为中心的最大回文串（偶）
        4. 每次扩散时，比较并记录当前最长的回文串，最终得到最长回文串

        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 0:
            return ''
        longest = s[0]
        mat = [[0 if i != j else 1 for j in range(l)] for i in range(l)]
        for i in range(l):
            # 奇偶性由composition处理
            composition = ((0, 0), (1, 0))
            for left_right in composition:
                left_start = i - left_right[0]
                right_start = i + left_right[1]
                for j in range(0, min(i, l - i - 1) + 1):
                    # 若 S[i] == S[j]，那么只要 S[i+1] 至 S[j-1] 是回文子串，S[i] 至 S[j] 就是回文子串；
                    # 如果S[i+1] 至 S[j-1] 不是回文子串，则 S[i] 至 S[j] 也不是回文子串。
                    left = left_start - j
                    right = right_start + j
                    if left < 0 or right >= l:
                        break
                    if mat[left][right] == 1:
                        print('>>>')
                        continue
                    if s[left] == s[right] and (abs(right-left)<=1 or mat[left + 1][right - 1] == 1):
                        mat[left][right] = 1
                        if (right - left + 1) > len(longest):
                            longest = s[left:right + 1]
                    else:
                        break

        return longest


sol = Solution()
assert (sol.longestPalindrome('aaaaaabaa') == "aaaaaa")
assert (sol.longestPalindrome('a') == "a")
assert (sol.longestPalindrome('ab') == "a")
assert (sol.longestPalindrome('aaacaaabaa') == "aaacaaa")
assert (sol.longestPalindrome('qwertrewq') == "qwertrewq")
assert (sol.longestPalindrome('qwerttrewq') == "qwerttrewq")
assert (sol.longestPalindrome('cbbd') == "bb")
