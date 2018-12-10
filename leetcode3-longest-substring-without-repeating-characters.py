"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
�����ظ��ַ�����Ӵ���

����һ���ַ����������ҳ����в������ظ��ַ��� ��Ӵ� �ĳ��ȡ�
ʾ�� 1:
����: "abcabcbb"
���: 3
����: ��Ϊ���ظ��ַ�����Ӵ��� "abc"�������䳤��Ϊ 3��

ʾ�� 2:
����: "bbbbb"
���: 1
����: ��Ϊ���ظ��ַ�����Ӵ��� "b"�������䳤��Ϊ 1��

ʾ�� 3:
����: "pwwkew"
���: 3
����: ��Ϊ���ظ��ַ�����Ӵ��� "wke"�������䳤��Ϊ 3��
     ��ע�⣬��Ĵ𰸱����� �Ӵ� �ĳ��ȣ�"pwke" ��һ�������У������Ӵ���
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        0. ����ijΪ0��������ƶ�j
        1. �����j��Ԫ����s[i:j]�е�λ��pos
        2. λ��pos��Ϊ-1����iΪpos+1+i
        3. �����Ը�����󳤶�
        4. �ƶ�j�ظ�����1-3
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
