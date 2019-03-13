"""
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
《串联所有单词的子串》

给定一个字符串 s 和一些长度相同的单词 words。
找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []
        w_len = len(words[0])

        # 去重,计数
        word_set = set()
        word_count_map = {}
        for word in words:
            word_set.add(word)
            if word not in word_count_map:
                word_count_map[word] = 0
            word_count_map[word] += 1

        # 找出每个单词word在s中的位置
        w_in_s_idx_map = {}  # 记录 (单词在s的位置,单词)
        for word in word_set:
            offset = 0
            str = s
            while True:
                idx = str.find(word)
                if idx < 0:
                    break
                str = str[idx + 1:]
                w_in_s_idx_map[idx + offset] = word
                offset += (idx + 1)

            if len(str) == len(s):  # 没有找到，快速退出
                return []

        result = []
        # 遍历每个位置
        for k in w_in_s_idx_map.keys():
            next_index = k + w_len  # 下一个索引
            # 以w_len为步长，逐步查验单词是否在
            word_count2 = {w: 0 for w in word_set}  # 记录已经匹配过的单词
            word_count2[w_in_s_idx_map[k]] = 1
            ii = 1 # 记录当前已经处理了多少个单词
            while ii < len(words):
                if next_index in w_in_s_idx_map:
                    w = w_in_s_idx_map[next_index]
                    word_count2[w]+=1
                    if word_count2[w] > word_count_map[w]:
                        break
                    next_index += w_len
                    ii += 1
                else:
                    break
            if len(words) == ii:
                result.append(k)
        return result


sol = Solution()
# print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
# print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
# print(sol.findSubstring("", []))
# print(sol.findSubstring("a", ["a"]))
# print(sol.findSubstring("a", ["a"]))
print(sol.findSubstring("aaaaaaaa", ["aa","aa","aa"]))
